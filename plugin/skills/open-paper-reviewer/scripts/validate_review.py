#!/usr/bin/env python3
"""Check an OpenPaperReviewer review folder against the method's rules.

Usage:
    validate_review.py <review-folder> [--posting] [--check-path] [--json]

    --posting      also apply the rules for a review posted to the public repository
    --check-path   also check that the folder sits at <paper-id>/<paper-version>/<reviewer>-<date>/
    --json         print the result as JSON

Standard library only. Reads files, writes nothing, contacts nothing.
Allowed values come from references/rubric.json beside this script's folder.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
RUBRIC_PATH = SKILL_DIR / "references" / "rubric.json"

CLAIM_ID = re.compile(r"^[A-Z]-\d{2}$")
CITATION_ID = re.compile(r"^C-\d{3}$")
HANDLE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PUBLIC_ID = re.compile(r"^(doi:10\.\d{4,9}/\S+|arxiv:\S+|https?://\S+)$", re.IGNORECASE)
VERIFICATION_LINE = re.compile(r"citation verification\W{1,12}(all|partial|none)\b", re.IGNORECASE)
ESTABLISHES_HEADING = re.compile(r"^#{1,6}\s+.*what the paper establishes", re.IGNORECASE | re.MULTILINE)
CONCERNS_HEADING = re.compile(r"^#{1,6}\s+.*concerns", re.IGNORECASE | re.MULTILINE)
# Rubric rule: a headline claim that does not stand is Critical; if a narrower form of it stands, it is Major.
HEADLINE_SEVERITY = {"Unsupported": "Critical", "Contradicted": "Critical", "Partially Supported": "Major"}

PLACEHOLDERS = {"", "unknown", "unk", "?", "tbd", "todo", "n/a", "na", "not sure", "unspecified"}
PHASES = [str(number) for number in range(8)]
PHASE_STEMS = [
    "01_checklist_and_references",
    "02_claims_registry",
    "03_scrutiny",
    "04_references",
    "05_methods",
    "06_synthesis",
    "07_verification",
]
USED_FOR_LABELS = {"checklist", "references", "methods", "synthesis"}
VERIFIED = {"confirmed", "corrected"}
OPENED = {"full_text", "abstract"}
POSTING_SUFFIXES = {".md", ".json", ".txt"}
POSTING_MAX_FILE = 512 * 1024
POSTING_MAX_TOTAL = 3 * 1024 * 1024


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, message):
        self.errors.append(f"{where}: {message}")

    def warn(self, where, message):
        self.warnings.append(f"{where}: {message}")


def values(rubric, key):
    return [entry["value"] if isinstance(entry, dict) else entry for entry in rubric[key]]


def is_blank(value, extra=()):
    return not isinstance(value, str) or value.strip().casefold() in PLACEHOLDERS.union(extra)


def word_count(text):
    return len(text.split())


def valid_date(text):
    try:
        date.fromisoformat(text)
    except ValueError:
        return False
    return True


def check_enum(report, where, value, allowed):
    if isinstance(value, bool) or value not in allowed:
        report.error(where, f"{value!r} is not one of: {', '.join(str(item) for item in allowed)}")
        return False
    return True


def load_json(path, report):
    if not path.is_file():
        report.error(path.name, "file is missing")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        report.error(path.name, f"not valid JSON ({exc})")
        return None


def phase_text(folder, stem):
    """Text of a phase stored as <stem>.md and/or markdown files under <stem>/; None if absent."""
    parts = []
    single = folder / f"{stem}.md"
    if single.is_file():
        parts.append(single.read_text(encoding="utf-8", errors="replace"))
    directory = folder / stem
    if directory.is_dir():
        for path in sorted(directory.rglob("*.md")):
            parts.append(path.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(parts) if parts else None


def check_run(run, rubric, posting, report):
    where = "run.json"
    if not isinstance(run, dict):
        report.error(where, "must be a JSON object")
        return
    sources = values(rubric, "value_source")

    method = run.get("method") if isinstance(run.get("method"), dict) else {}
    if method.get("name") != "OpenPaperReviewer":
        report.error(where, 'method.name must be "OpenPaperReviewer"')
    if is_blank(method.get("version")):
        report.error(where, "method.version is missing")
    check_enum(report, f"{where} method.entry", method.get("entry"), values(rubric, "method_entry"))
    if not isinstance(method.get("modified"), bool):
        report.error(where, "method.modified must be true or false")
    elif method["modified"]:
        report.warn(where, "method.modified is true: prompt.md must contain the full modified instructions")

    paper = run.get("paper") if isinstance(run.get("paper"), dict) else {}
    for key in ("title", "identifier", "version"):
        if is_blank(paper.get(key)):
            report.error(where, f"paper.{key} is missing")
    if not isinstance(paper.get("public"), bool):
        report.error(where, "paper.public must be true or false")

    review = run.get("review") if isinstance(run.get("review"), dict) else {}
    dates = {}
    for key in ("started", "finished"):
        value = review.get(key)
        if isinstance(value, str) and ISO_DATE.match(value) and valid_date(value):
            dates[key] = date.fromisoformat(value)
        else:
            report.error(where, f"review.{key} must be a date written YYYY-MM-DD")
    if len(dates) == 2 and dates["finished"] < dates["started"]:
        report.error(where, "review.finished is earlier than review.started")
    mode_ok = check_enum(report, f"{where} review.mode", review.get("mode"), values(rubric, "mode"))
    check_enum(report, f"{where} review.intake", review.get("intake"), values(rubric, "intake"))
    check_enum(report, f"{where} review.status", review.get("status"), values(rubric, "review_status"))
    check_enum(
        report,
        f"{where} review.citation_verification",
        review.get("citation_verification"),
        values(rubric, "verification"),
    )
    concerns = review.get("concerns")
    if not isinstance(concerns, list) or any(not isinstance(item, str) or not item.strip() for item in concerns):
        report.error(where, "review.concerns must be a list of non-empty strings (an empty list for a standard review)")
    elif mode_ok:
        if review["mode"] == "focused" and not concerns:
            report.error(where, "a focused review must list the concerns that were given")
        if review["mode"] == "standard" and concerns:
            report.error(where, "a standard review has no concerns; set review.mode to focused")
    if review.get("intake") == "not_interactive" and review.get("mode") == "focused":
        report.error(where, "a run that could not ask the intake question is a standard review")

    tool = run.get("tool") if isinstance(run.get("tool"), dict) else {}
    if is_blank(tool.get("name")):
        report.error(where, "tool.name is missing")
    version = tool.get("version")
    if not isinstance(version, str) or not version.strip():
        report.error(where, 'tool.version is missing: record the version the tool reports or the user gives, or "unknown"')
    elif not re.search(r"\d", version):
        # Some tools do not show their version to the model. Unlike the model and effort, this does not block posting.
        report.warn(where, "tool.version is not known; add it before posting if the person running the review can find it")

    models = run.get("models")
    if not isinstance(models, list) or not models:
        report.error(where, "models must list at least one model")
    else:
        covered = set()
        for index, model in enumerate(models):
            label = f"{where} models[{index}]"
            if not isinstance(model, dict):
                report.error(label, "must be an object")
                continue
            if is_blank(model.get("name")):
                report.error(label, "name is missing")
            if is_blank(model.get("id")):
                report.error(label, "id is missing: record the model identifier the tool reports, or ask the user for it")
            if is_blank(model.get("effort"), extra={"none"}):
                report.error(
                    label,
                    'effort is missing: record the reasoning-effort setting, or "none exposed" if the tool has no such setting',
                )
            check_enum(report, f"{label} id_source", model.get("id_source"), sources)
            check_enum(report, f"{label} effort_source", model.get("effort_source"), sources)
            phases = model.get("phases")
            if not isinstance(phases, list) or not phases or any(phase not in PHASES for phase in phases):
                report.error(label, 'phases must list the phases this model ran, as strings "0" to "7"')
            else:
                covered.update(phases)
        missing = [phase for phase in PHASES if phase not in covered]
        if missing:
            report.error(where, "no model is recorded for phase(s) " + ", ".join(missing))

    if run.get("prompt_file") != "prompt.md":
        report.error(where, 'prompt_file must be "prompt.md"')
    if not isinstance(run.get("web_access"), bool):
        report.error(where, "web_access must be true or false")

    if posting:
        if paper.get("public") is not True:
            report.error(where, "only reviews of publicly available papers can be posted (paper.public must be true)")
        identifier = paper.get("identifier")
        if isinstance(identifier, str) and not PUBLIC_ID.match(identifier.strip()):
            report.error(where, "paper.identifier must start with doi:, arXiv: or http(s):// for a posted review")
        if not (isinstance(run.get("reviewer"), str) and HANDLE.match(run["reviewer"])):
            report.error(where, "reviewer must be the poster's GitHub handle")
        if is_blank(run.get("human_check")):
            report.error(where, 'human_check is missing: say what a person checked, or "none"')
        if is_blank(run.get("conflicts_of_interest")):
            report.error(where, 'conflicts_of_interest is missing: declare them, or "none"')


def check_claims(data, rubric, report):
    where = "claims.json"
    claims = data.get("claims") if isinstance(data, dict) else None
    if not isinstance(claims, list) or not claims:
        report.error(where, 'must be an object with a non-empty "claims" list')
        return []
    limits = rubric["limits"]
    checked, seen = [], set()
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            report.error(f"{where} claims[{index}]", "must be an object")
            continue
        claim_id = claim.get("id")
        id_ok = isinstance(claim_id, str) and bool(CLAIM_ID.match(claim_id))
        label = f"{where} {claim_id}" if id_ok else f"{where} claims[{index}]"
        if not id_ok:
            report.error(label, "id must look like A-01")
        elif claim_id in seen:
            report.error(label, "duplicate id")
        else:
            seen.add(claim_id)
            if claim.get("group") != claim_id[0]:
                report.error(label, "group must be the letter the id starts with")

        text = claim.get("text")
        if is_blank(text):
            report.error(label, "text is missing")
        elif word_count(text) > limits["claim_quote_words"]:
            report.error(
                label,
                f"text is {word_count(text)} words; the limit is {limits['claim_quote_words']}. "
                "Quote the core of the claim and trim with an ellipsis",
            )
        if is_blank(claim.get("location")):
            report.error(label, "location is missing")
        check_enum(report, f"{label} type", claim.get("type"), values(rubric, "claim_type"))
        check_enum(report, f"{label} tier", claim.get("tier"), values(rubric, "tier"))
        if not isinstance(claim.get("headline"), bool):
            report.error(label, "headline must be true or false")

        verdict, severity = claim.get("verdict"), claim.get("severity")
        if check_enum(report, f"{label} verdict", verdict, values(rubric, "verdict")):
            if verdict == "Supported":
                if severity is not None:
                    report.error(label, "severity must be null when the verdict is Supported")
            elif severity is None:
                report.error(label, "severity is required unless the verdict is Supported")
            elif check_enum(report, f"{label} severity", severity, values(rubric, "severity")) and claim.get("headline") is True:
                required = HEADLINE_SEVERITY.get(verdict)
                if required and severity != required:
                    report.error(
                        label,
                        f"severity must be {required}, not {severity}, for a headline claim judged {verdict} (rubric: a headline "
                        "claim that does not stand is Critical; if a narrower form of it stands, it is Major)",
                    )
        check_enum(report, f"{label} confidence", claim.get("confidence"), values(rubric, "confidence"))

        for key in ("blocked_by", "basis"):
            entries = claim.get(key, [])
            if not isinstance(entries, list) or any(not isinstance(item, str) or not item.strip() for item in entries):
                report.error(label, f"{key} must be a list of non-empty strings")
        summary = claim.get("summary")
        if is_blank(summary):
            report.error(label, "summary is missing")
        elif word_count(summary) > limits["summary_words"]:
            report.error(label, f"summary is {word_count(summary)} words; the limit is {limits['summary_words']}")
        if id_ok:
            checked.append(claim)
    return checked


def check_citations(data, rubric, claim_ids, report):
    where = "citations.json"
    citations = data.get("citations") if isinstance(data, dict) else None
    if not isinstance(citations, list):
        report.error(where, 'must be an object with a "citations" list')
        return None
    if not citations:
        report.warn(where, "the review cites no outside sources")
    limit = rubric["limits"]["citation_quote_words"]
    index = {}
    for position, citation in enumerate(citations):
        if not isinstance(citation, dict):
            report.error(f"{where} citations[{position}]", "must be an object")
            continue
        citation_id = citation.get("id")
        id_ok = isinstance(citation_id, str) and bool(CITATION_ID.match(citation_id))
        label = f"{where} {citation_id}" if id_ok else f"{where} citations[{position}]"
        if not id_ok:
            report.error(label, "id must look like C-001")
        elif citation_id in index:
            report.error(label, "duplicate id")
        if is_blank(citation.get("reference")):
            report.error(label, "reference is missing")
        for key in ("identifier", "url"):
            if citation.get(key) is not None and not isinstance(citation.get(key), str):
                report.error(label, f"{key} must be a string or null")

        used_for = citation.get("used_for")
        if not isinstance(used_for, list) or not used_for or any(not isinstance(item, str) for item in used_for):
            report.error(label, "used_for must list the claim ids or sections that rely on this source")
        else:
            for item in used_for:
                if item not in USED_FOR_LABELS and item not in claim_ids:
                    report.error(
                        label,
                        f"used_for entry {item!r} is neither a claim id in claims.json nor one of: "
                        + ", ".join(sorted(USED_FOR_LABELS)),
                    )

        access_ok = check_enum(report, f"{label} access", citation.get("access"), values(rubric, "access"))
        status_ok = check_enum(report, f"{label} status", citation.get("status"), values(rubric, "citation_status"))
        if access_ok and status_ok and citation["status"] in VERIFIED:
            if citation["access"] not in OPENED:
                report.error(label, "a confirmed or corrected source must have been opened (access full_text or abstract)")
            quote = citation.get("quote")
            if is_blank(quote):
                report.error(label, "quote is required for a confirmed or corrected source")
            elif word_count(quote) > limit:
                report.error(label, f"quote is {word_count(quote)} words; the limit is {limit}")
            if is_blank(citation.get("identifier")) and is_blank(citation.get("url")):
                report.error(label, "give the identifier or the URL where the source was read")
        found_error = citation.get("error")
        if found_error is not None:
            check_enum(report, f"{label} error", found_error, values(rubric, "citation_error"))
        if status_ok:
            if citation["status"] == "corrected" and found_error is None:
                report.error(label, "a corrected source must say what kind of error was found (error)")
            if citation["status"] == "confirmed" and found_error is not None:
                report.error(label, "a confirmed source has no error; use status corrected if one was fixed")
        if id_ok and citation_id not in index:
            index[citation_id] = citation
    return index


def check_claim_links(claims, citations, report):
    ids = {claim["id"] for claim in claims}
    for claim in claims:
        label = f"claims.json {claim['id']}"
        blocked = claim.get("blocked_by", [])
        if isinstance(blocked, list):
            for other in blocked:
                if other == claim["id"]:
                    report.error(label, "a claim cannot be blocked by itself")
                elif isinstance(other, str) and other not in ids:
                    report.error(label, f"blocked_by names {other}, which is not a claim id")
            if blocked and claim.get("verdict") == "Supported":
                report.error(label, "a claim that is blocked by another cannot be Supported")

        basis = claim.get("basis", [])
        if not isinstance(basis, list):
            continue
        checkable = False
        for entry in basis:
            if not isinstance(entry, str):
                continue
            entry = entry.strip()
            if entry.casefold().startswith("paper:"):
                checkable = checkable or bool(entry[6:].strip())
                continue
            if not CITATION_ID.match(entry):
                report.error(label, f'basis entry {entry!r} must be "paper: <location>" or a citation id such as C-001')
            elif citations is not None and entry not in citations:
                report.error(label, f"basis cites {entry}, which is not in citations.json")
            if citations and entry in citations and citations[entry].get("status") in VERIFIED:
                checkable = True
        if (claim.get("verdict") == "Contradicted" or claim.get("severity") == "Critical") and not checkable:
            report.error(
                label,
                "Contradicted or Critical needs a basis anyone can check: a location in the paper, "
                "or a citation that is confirmed or corrected",
            )


def computed_verification(citations, web_access=True):
    relied = [item for item in citations.values() if item.get("status") != "removed"]
    if not relied:
        # Nothing to verify. A run that could not have verified anything says "none".
        return "none" if web_access is False else "all"
    if all(item.get("status") in VERIFIED for item in relied):
        return "all"
    if not any(item.get("status") in VERIFIED for item in relied):
        return "none"
    return "partial"


def check_prompt(folder, report):
    path = folder / "prompt.md"
    if not path.is_file():
        report.error("prompt.md", "file is missing: the prompt used must be recorded")
        return
    sections, current = {}, None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("## "):
            current = line[3:].strip().casefold()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    for wanted in ("request", "method"):
        names = [name for name in sections if name.startswith(wanted)]
        if not names:
            report.error("prompt.md", f'section "## {wanted.capitalize()}" is missing')
        elif not "".join(sections[names[0]]).strip():
            report.error("prompt.md", f'section "## {wanted.capitalize()}" is empty')


def check_phase_files(folder, posting, report):
    for stem in PHASE_STEMS:
        if phase_text(folder, stem) is None:
            report.error(stem, f"phase output is missing (expected {stem}.md or a {stem}/ folder of .md files)")
    has_extraction = phase_text(folder, "00_extraction") is not None
    if posting and has_extraction:
        report.error("00_extraction", "must not be posted: it reproduces the paper's abstract")
    if not posting and not has_extraction:
        report.error("00_extraction", "phase output is missing (expected 00_extraction.md)")


def mentions(text, claim_id):
    return re.search(r"(?<![A-Za-z0-9])" + re.escape(claim_id) + r"(?![0-9])", text) is not None


def check_ids_in_phases(folder, claims, report):
    registry = phase_text(folder, "02_claims_registry") or ""
    scrutiny = phase_text(folder, "03_scrutiny") or ""
    for claim in claims:
        if registry and not mentions(registry, claim["id"]):
            report.error(f"claims.json {claim['id']}", "does not appear in the claims registry")
        if scrutiny and not mentions(scrutiny, claim["id"]):
            report.error(f"claims.json {claim['id']}", "has no block in the scrutiny files")


def check_synthesis(folder, run, claims, citations, report):
    text = phase_text(folder, "06_synthesis")
    if text is None:
        return
    where = "06_synthesis"
    if not ESTABLISHES_HEADING.search(text):
        report.error(where, 'a section headed "What the paper establishes" is required')
    absent = [claim["id"] for claim in claims if not mentions(text, claim["id"])]
    if absent:
        report.error(where, "the verdict table must list every claim; missing: " + ", ".join(absent))
    stated = VERIFICATION_LINE.search(text)
    if not stated:
        report.error(where, 'the header must carry the line "Citation verification: all | partial | none"')
    if citations is not None:
        expected = computed_verification(citations, run.get("web_access"))
        if stated and stated.group(1).casefold() != expected:
            report.error(where, f"says citation verification is {stated.group(1)!r}; citations.json makes it {expected!r}")
        review = run.get("review", {})
        recorded = review.get("citation_verification") if isinstance(review, dict) else None
        if isinstance(recorded, str) and recorded in ("all", "partial", "none") and recorded != expected:
            report.error("run.json", f"review.citation_verification is {recorded!r}; citations.json makes it {expected!r}")
    for model in run.get("models") or []:
        if not isinstance(model, dict):
            continue
        model_id, effort = model.get("id"), model.get("effort")
        if isinstance(model_id, str) and model_id.strip() and model_id not in text:
            report.error(where, f"the header must name the model used ({model_id})")
        if isinstance(effort, str) and effort.strip() and effort.casefold() not in text.casefold():
            report.error(where, f"the header must state the reasoning effort used ({effort})")
    review = run.get("review")
    if isinstance(review, dict) and review.get("mode") == "focused" and not CONCERNS_HEADING.search(text):
        report.error(where, "a focused review needs a section answering the concerns given at intake")


def check_posting_files(folder, report):
    total = 0
    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(folder).as_posix()
        if any(part.startswith(".") for part in path.relative_to(folder).parts):
            report.error(relative, "hidden files cannot be posted")
            continue
        if path.suffix.lower() not in POSTING_SUFFIXES:
            report.error(relative, "only .md, .json and .txt files can be posted (never the paper itself)")
        size = path.stat().st_size
        total += size
        if size > POSTING_MAX_FILE:
            report.error(relative, f"file is {size // 1024} KiB; the limit is {POSTING_MAX_FILE // 1024} KiB")
    if total > POSTING_MAX_TOTAL:
        report.error("review folder", f"total size is {total // 1024} KiB; the limit is {POSTING_MAX_TOTAL // 1024} KiB")


def slug(text):
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9.]+", "-", text.strip().casefold())).strip("-")


def expected_path(run):
    paper, review = run.get("paper", {}), run.get("review", {})
    return (
        slug(str(paper.get("identifier", ""))),
        slug(str(paper.get("version", ""))),
        f"{run.get('reviewer', '')}-{review.get('finished', '')}",
    )


def check_posting_path(folder, run, report):
    if not run:
        return
    actual = folder.resolve().parts[-3:]
    wanted = expected_path(run)
    if tuple(actual) != wanted:
        report.error("review folder", f"must be at {'/'.join(wanted)}/ ; found {'/'.join(actual)}/")


def validate(folder, posting=False, check_path=False):
    report = Report()
    folder = Path(folder)
    if not folder.is_dir():
        report.error(str(folder), "not a folder")
        return report
    rubric = json.loads(RUBRIC_PATH.read_text(encoding="utf-8"))

    run = load_json(folder / "run.json", report)
    claims_data = load_json(folder / "claims.json", report)
    citations_data = load_json(folder / "citations.json", report)

    if run is not None:
        check_run(run, rubric, posting, report)
    run = run if isinstance(run, dict) else {}
    claims = check_claims(claims_data, rubric, report) if claims_data is not None else []
    claim_ids = {claim["id"] for claim in claims}
    citations = check_citations(citations_data, rubric, claim_ids, report) if citations_data is not None else None
    check_claim_links(claims, citations, report)
    check_prompt(folder, report)
    check_phase_files(folder, posting, report)
    check_ids_in_phases(folder, claims, report)
    check_synthesis(folder, run, claims, citations, report)
    if posting:
        check_posting_files(folder, report)
    if check_path:
        check_posting_path(folder, run, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder")
    parser.add_argument("--posting", action="store_true")
    parser.add_argument("--check-path", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = validate(args.folder, posting=args.posting, check_path=args.check_path)
    if args.json:
        print(json.dumps({"ok": not report.errors, "errors": report.errors, "warnings": report.warnings}, indent=2))
    else:
        for line in report.errors:
            print(f"ERROR    {line}")
        for line in report.warnings:
            print(f"WARNING  {line}")
        if report.errors:
            print(f"FAILED: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
        else:
            print(f"OK: review folder is valid ({len(report.warnings)} warning(s))")
    sys.exit(1 if report.errors else 0)


if __name__ == "__main__":
    main()
