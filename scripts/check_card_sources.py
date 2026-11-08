#!/usr/bin/env python3
"""Check the bibliographic records behind the sources listed in checklist cards.

Usage:
    check_card_sources.py [card.md ...] [--strict]

With no arguments, checks every card. For each source a card lists
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

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load("verify_citations", SKILL / "scripts" / "verify_citations.py")
card_checker = load("check_card", ROOT / "scripts" / "check_card.py")


def rows(path):
    """Each source of a card: number, reference, identifier, and the access recorded in card-sources/."""
    _, _, sources = card_checker.parse(path)
    notes = card_checker.parse_notes(card_checker.notes_path(path)) or {}
    for number, source in sources.items():
        yield number, source["reference"], source["identifier"], notes.get(number, {}).get("access", "access not recorded")


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

    paths = [Path(card) for card in args.cards] or card_checker.card_files()
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
