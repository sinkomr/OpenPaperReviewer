#!/usr/bin/env python3
"""Look up the records behind citations and report the ones that do not match.

Usage:
    verify_citations.py <citations.json> [--json] [--strict] [--timeout 20]
    verify_citations.py --identifier doi:10.xxxx/yyyy [--reference "Authors, Title, Venue (year)"]

For each entry with a DOI or an arXiv identifier, this fetches the public
record (Crossref for DOIs, the arXiv API for arXiv ids) and compares the first
author, year and title with the reference text given for the entry.

It checks records only. Whether a source supports the statement it is cited
for still has to be judged by reading the source.

Standard library only. Contacts api.crossref.org and export.arxiv.org, and
sends nothing but the identifiers themselves.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = "OpenPaperReviewer-verify-citations/0.1 (https://github.com/sinkomr/OpenPaperReviewer)"
DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.IGNORECASE)
ARXIV_NEW = re.compile(r"\b(\d{4}\.\d{4,5})(v\d+)?\b")
ARXIV_OLD = re.compile(r"\b([a-z-]+(?:\.[A-Z]{2})?/\d{7})(v\d+)?\b")
ATOM = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_PAUSE = 3.0
CROSSREF_PAUSE = 0.2


def fold(text):
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def parse_identifier(*candidates):
    """Return ("doi", value), ("arxiv", value) or (None, None) from identifier and URL strings."""
    for raw in candidates:
        if not isinstance(raw, str) or not raw.strip():
            continue
        text = raw.strip()
        lowered = text.casefold()
        if "arxiv" in lowered:
            match = ARXIV_NEW.search(text) or ARXIV_OLD.search(text)
            if match:
                return "arxiv", match.group(1)
        match = DOI.search(text)
        if match:
            return "doi", match.group(0).rstrip(".,;)")
    return None, None


def fetch(url, timeout, retries=2):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/atom+xml"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            # The registries ask clients to slow down with 429 or 503; wait and try again.
            if exc.code not in (429, 503) or attempt == retries:
                raise
            time.sleep(5 * (attempt + 1))


def crossref_record(doi, timeout):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    message = json.loads(fetch(url, timeout)).get("message", {})
    authors = message.get("author") or []
    # Online-first and print years often differ; a reference may use either.
    years = []
    for key in ("published-print", "issued", "published-online", "published"):
        parts = (message.get(key) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0] and int(parts[0][0]) not in years:
            years.append(int(parts[0][0]))
    notices = []
    for update in message.get("updated-by") or []:
        kind = update.get("type") or "update"
        target = update.get("DOI")
        notices.append(f"{kind} (doi:{target})" if target else kind)
    return {
        "title": " ".join(message.get("title") or []),
        "first_author": (authors[0].get("family") or authors[0].get("name") or "") if authors else "",
        "author_count": len(authors),
        "years": years,
        "venue": " ".join(message.get("container-title") or []),
        "notices": notices,
    }


def arxiv_record(arxiv_id, timeout):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    root = ET.fromstring(fetch(url, timeout))
    entry = root.find("atom:entry", ATOM)
    if entry is None or entry.find("atom:published", ATOM) is None:
        return None
    names = [node.findtext("atom:name", default="", namespaces=ATOM) for node in entry.findall("atom:author", ATOM)]
    first = names[0].split()[-1] if names and names[0].split() else ""
    return {
        "title": " ".join((entry.findtext("atom:title", default="", namespaces=ATOM)).split()),
        "first_author": first,
        "author_count": len(names),
        "years": [int(entry.findtext("atom:published", default="0000", namespaces=ATOM)[:4])],
        "venue": "arXiv",
        "notices": [],
    }


def title_in_reference(title, reference):
    """True if the record's title appears in the reference text; None if it cannot be told.

    Many citation styles omit titles, so a title that is not found is never
    counted as a mismatch.
    """
    folded_title, folded_reference = fold(title), fold(reference)
    if not folded_title:
        return None
    if folded_title in folded_reference:
        return True
    title_words = [word for word in folded_title.split() if len(word) > 2]
    if len(title_words) < 3:
        return None
    reference_words = set(folded_reference.split())
    shared = sum(1 for word in title_words if word in reference_words)
    return True if shared / len(title_words) >= 0.7 else None


def compare(record, reference):
    folded = fold(reference)
    author = fold(record["first_author"])
    checks = {
        "first_author": (author in folded) if author else None,
        "year": any(str(year) in reference for year in record["years"]) if record["years"] else None,
        "title": title_in_reference(record["title"], reference),
    }
    mismatched = [name for name in ("first_author", "year") if checks[name] is False]
    return checks, mismatched


def check_one(entry_id, reference, kind, value, timeout):
    result = {"id": entry_id, "identifier": f"{kind}:{value}" if kind else None, "reference": reference}
    if not kind:
        result.update(result="no identifier", detail="no DOI or arXiv identifier to look up")
        return result
    try:
        record = crossref_record(value, timeout) if kind == "doi" else arxiv_record(value, timeout)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            result.update(result="not found", detail="the registry has no record for this identifier")
        else:
            result.update(result="lookup failed", detail=f"HTTP {exc.code}")
        return result
    except (urllib.error.URLError, TimeoutError, ET.ParseError, json.JSONDecodeError, ValueError) as exc:
        result.update(result="lookup failed", detail=str(exc))
        return result
    if record is None:
        result.update(result="not found", detail="the registry has no record for this identifier")
        return result
    result["record"] = record
    if not (reference or "").strip():
        result.update(result="found", detail="no reference text was given to compare with")
        return result
    checks, mismatched = compare(record, reference)
    result["checks"] = checks
    if mismatched:
        result.update(result="mismatch", detail="does not match the reference text: " + ", ".join(mismatched))
    else:
        notes = [
            "first author agrees" if checks["first_author"] else "the record lists no authors",
            "year agrees" if checks["year"] else "the record gives no year",
            "title agrees" if checks["title"] else "title not found in the reference text (compare by hand if the reference gives one)",
        ]
        result.update(result="matches", detail="; ".join(notes))
    if record["notices"]:
        result["detail"] += "; notices on the record: " + "; ".join(record["notices"])
    return result


def run(entries, timeout):
    results = []
    for entry_id, reference, kind, value in entries:
        results.append(check_one(entry_id, reference, kind, value, timeout))
        if kind:
            time.sleep(ARXIV_PAUSE if kind == "arxiv" else CROSSREF_PAUSE)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("citations", nargs="?", help="path to citations.json")
    parser.add_argument("--identifier", help="check a single DOI or arXiv identifier")
    parser.add_argument("--reference", default="", help="reference text to compare a single identifier with")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any record is a mismatch or is not found")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()

    if args.identifier:
        kind, value = parse_identifier(args.identifier)
        entries = [("-", args.reference, kind, value)]
    elif args.citations:
        try:
            with open(args.citations, encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            sys.exit(f"cannot read {args.citations}: {exc}")
        items = data.get("citations") if isinstance(data, dict) else data
        if not isinstance(items, list):
            sys.exit('expected an object with a "citations" list')
        entries = []
        for item in items:
            if not isinstance(item, dict) or item.get("status") == "removed":
                continue
            kind, value = parse_identifier(item.get("identifier"), item.get("url"))
            entries.append((item.get("id", "?"), item.get("reference", ""), kind, value))
    else:
        parser.error("give a citations.json file or --identifier")

    results = run(entries, args.timeout)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for item in results:
            print(f"{item['id']:<7} {item['result']:<14} {item.get('identifier') or '-'}")
            print(f"        {item['detail']}")
            record = item.get("record")
            if record:
                others = f" and {record['author_count'] - 1} more" if record["author_count"] > 1 else ""
                years = "/".join(str(year) for year in record["years"]) or "no year"
                print(f"        record: {record['first_author'] or 'no author listed'}{others}; {years}; {record['venue']}; {record['title'][:90]}")
        counts = {}
        for item in results:
            counts[item["result"]] = counts.get(item["result"], 0) + 1
        print("summary: " + ", ".join(f"{count} {name}" for name, count in sorted(counts.items())))
    if args.strict and any(item["result"] in ("mismatch", "not found") for item in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
