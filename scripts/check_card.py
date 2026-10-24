#!/usr/bin/env python3
"""Check checklist cards against the card format.

Usage:
    check_card.py [card.md ...]

With no arguments, checks every card and also that no two cards share an id.
Prints each problem and exits 1 if there are any. The rules are those in
plugin/skills/open-paper-reviewer/references/checklists/README.md; the tests
use the same function.

This checks format only. Whether each source supports its item is checked by
opening the source; scripts/check_card_sources.py checks that each record exists.

Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "plugin" / "skills" / "open-paper-reviewer" / "references" / "checklists"
FRONTMATTER_KEYS = ["id", "name", "type", "field", "applies_when", "version"]
LABELS = ["Question.", "Why it matters.", "Resolved by.", "Benchmark."]
LOADED_WORDS = ["fatal", "red flag", "suspicious", "killer", "fraud", "misconduct"]
PREFIX = {"core": "C-", "technique": "T-", "claim": "CL-"}
ITEMS = {"core": (2, 4), "technique": (5, 8), "claim": (5, 8)}
APPLIES_WHEN_WORDS = 45


def parse(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return None, [], {}
    meta = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"')
    sections = re.split(r"^## ", match.group(2), flags=re.MULTILINE)[1:]
    items, sources = [], {}
    for section in sections:
        title, _, content = section.partition("\n")
        if title.strip() == "Sources":
            for row in content.splitlines():
                cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
                if len(cells) >= 5 and cells[0].isdigit():
                    sources[int(cells[0])] = {"reference": cells[1], "identifier": cells[2], "access": cells[3], "where": cells[4]}
        else:
            items.append((title.strip(), content))
    return meta, items, sources


def card_files():
    return sorted(path for path in CARDS.rglob("*.md") if path.name not in ("README.md", "INDEX.md"))


def problems(path):
    """Return a list of format problems for one card."""
    path = Path(path).resolve()
    meta, items, sources = parse(path)
    if meta is None:
        return ["no frontmatter block between --- lines"]
    found = [f"missing frontmatter key {key!r}" for key in FRONTMATTER_KEYS if key not in meta]
    if found:
        return found

    folder = path.parent.relative_to(CARDS).as_posix()
    kind = meta["type"]
    if kind not in PREFIX:
        return [f"type must be core, technique or claim, not {kind!r}"]
    if kind == "core":
        if folder != "core" or meta["field"] != "any":
            found.append("a core card lives in core/ and has field: any")
    else:
        if folder == "core":
            found.append("only core cards live in core/")
        if meta["field"] != folder:
            found.append(f"field must be the card's folder, {folder!r}, not {meta['field']!r}")
    if not meta["id"].startswith(PREFIX[kind]) or not re.fullmatch(r"[A-Z]+-[A-Z0-9-]+", meta["id"]):
        found.append(f"a {kind} card's id is upper case and starts with {PREFIX[kind]}")
    if re.search(r"[()]", meta["name"]):
        found.append("the card name has no parentheses; put abbreviations in the opening sentence")
    if len(meta["applies_when"].split()) > APPLIES_WHEN_WORDS:
        found.append(f"applies_when is over {APPLIES_WHEN_WORDS} words; it goes into the folder index that reviews read")

    low, high = ITEMS[kind]
    if not low <= len(items) <= high:
        found.append(f"a {kind} card has {low} to {high} items, found {len(items)}")

    used = set()
    for number, (title, content) in enumerate(items, 1):
        if not title.startswith(f"{number}. "):
            found.append(f"item heading should start '{number}. ': {title!r}")
        missing = [label for label in LABELS if content.count(f"**{label}**") != 1]
        if missing:
            found.append(f"item {number} needs exactly one of each line: {', '.join(missing)}")
            continue
        benchmark = content.split("**Benchmark.**", 1)[1].strip().splitlines()[0]
        cited = [int(value) for value in re.findall(r"\[(\d+)\]", benchmark)]
        if not cited:
            if kind != "core":
                found.append(f"item {number} of a {kind} card needs a benchmark source")
            elif not benchmark.startswith("None needed"):
                found.append(f"item {number}: benchmark must cite a source or say 'None needed'")
        for value in cited:
            if value not in sources:
                found.append(f"item {number} cites [{value}], which is not in Sources")
        used.update(cited)
    unused = sorted(set(sources) - used)
    if unused:
        found.append(f"sources that no item cites: {unused}")

    for number, source in sources.items():
        if source["access"] not in ("full text", "abstract"):
            found.append(f"source {number}: access must be 'full text' or 'abstract'")
        if not re.match(r"^(doi:10\.\d{4,9}/\S+|https://\S+)$", source["identifier"]):
            found.append(f"source {number}: identifier must be doi:... or an https URL")
        if not re.search(r"\([^()]*\b(19|20)\d{2}\b[^()]*\)", source["reference"]):
            found.append(f"source {number}: reference needs a year in parentheses")
        if len(source["where"]) <= 20:
            found.append(f"source {number}: say where the source supports the item")

    text = path.read_text(encoding="utf-8")
    lowered = text.casefold()
    for word in LOADED_WORDS:
        if word in lowered:
            found.append(f"loaded word {word!r}: cards ask questions, they do not accuse")
    for quoted in re.findall(r'"([^"\n]+)"', text):
        if len(quoted.split()) >= 15:
            found.append(f"quotation of 15 words or more: {quoted[:60]!r}")
    return found


def duplicate_ids(paths):
    seen, found = {}, []
    for path in paths:
        meta, _, _ = parse(path)
        if meta and "id" in meta:
            if meta["id"] in seen:
                found.append(f"id {meta['id']} is used by {seen[meta['id']]} and {path.relative_to(CARDS)}")
            seen.setdefault(meta["id"], path.relative_to(CARDS))
    return found


def main():
    paths = [Path(arg) for arg in sys.argv[1:]] or card_files()
    bad = 0
    for path in paths:
        for problem in problems(path):
            bad += 1
            print(f"{path}: {problem}")
    if not sys.argv[1:]:
        for problem in duplicate_ids(paths):
            bad += 1
            print(problem)
    print(f"{len(paths)} card(s) checked, {bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
