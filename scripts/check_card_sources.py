#!/usr/bin/env python3
"""Check the bibliographic records behind the sources listed in checklist cards.

Usage:
    check_card_sources.py [card.md ...] [--strict]

With no arguments, checks every card. For each row of a card's Sources table
that has a DOI, looks the record up (Crossref, then the DOI resolver for DOIs
that Crossref does not hold) and compares the first author and year with the
reference text. For URL identifiers, checks only that the URL answers.

This confirms that a source exists and is described correctly. It cannot
confirm that the source supports the card item: that needs a person or a model
to open the source and read the passage the card points to.

Standard library only. Contacts api.crossref.org, doi.org and the listed URLs.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "open-paper-reviewer"
CARDS = SKILL / "references" / "checklists"

_spec = importlib.util.spec_from_file_location("verify_citations", SKILL / "scripts" / "verify_citations.py")
verify = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify)


def rows(path):
    in_sources = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_sources = line.strip() == "## Sources"
            continue
        if not in_sources:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0].isdigit():
            yield int(cells[0]), cells[1], cells[2], cells[3]


def doi_resolves(doi, timeout):
    url = "https://doi.org/api/handles/" + urllib.parse.quote(doi, safe="/")
    try:
        return json.loads(verify.fetch(url, timeout)).get("responseCode") == 1
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError):
        return False


def url_answers(url, timeout):
    request = urllib.request.Request(url, headers={"User-Agent": verify.USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status < 400
    except urllib.error.HTTPError as exc:
        return exc.code in (401, 403)  # the page exists but refuses scripted access
    except (urllib.error.URLError, TimeoutError, ValueError):
        return False


def check(reference, identifier, timeout):
    kind, value = verify.parse_identifier(identifier)
    if kind == "arxiv":
        result = verify.check_one("-", reference, kind, value, timeout)
        time.sleep(verify.ARXIV_PAUSE)
        return result["result"], result["detail"]
    if kind == "doi":
        result = verify.check_one("-", reference, kind, value, timeout)
        if result["result"] == "not found" and doi_resolves(value, timeout):
            return "resolves", "the DOI resolves but Crossref holds no record to compare (check by hand)"
        return result["result"], result["detail"]
    if identifier.startswith("https://"):
        return ("answers", "the URL answers") if url_answers(identifier, timeout) else ("unreachable", "the URL did not answer")
    return "no identifier", "nothing to look up"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cards", nargs="*")
    parser.add_argument("--strict", action="store_true", help="exit 1 on any mismatch, missing record or unreachable URL")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()

    paths = [Path(card) for card in args.cards] or sorted(p for p in CARDS.rglob("*.md") if p.name != "README.md")
    bad, total, cache = 0, 0, {}
    for path in paths:
        print(path.relative_to(ROOT) if path.is_absolute() and ROOT in path.parents else path)
        for number, reference, identifier, access in rows(path):
            total += 1
            key = (reference, identifier)
            if key not in cache:
                cache[key] = check(reference, identifier, args.timeout)
                time.sleep(verify.CROSSREF_PAUSE)
            outcome, detail = cache[key]
            if outcome in ("mismatch", "not found", "unreachable", "lookup failed", "no identifier"):
                bad += 1
            print(f"  [{number}] {outcome:<13} {identifier}  ({access})")
            if outcome not in ("matches", "answers"):
                print(f"        {detail}")
    print(f"{total} source row(s) checked, {bad} need attention")
    if args.strict and bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
