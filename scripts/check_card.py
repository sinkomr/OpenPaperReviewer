#!/usr/bin/env python3
"""Check checklist cards against the card format.

Usage:
    check_card.py [card.md ...]

With no arguments, checks every card, that no two cards share an id, and that
every file in card-sources/ belongs to a card. Prints each problem and exits 1
if there are any. The rules are those in
plugin/skills/open-paper-reviewer/references/checklists/README.md; the tests
use the same function.

Each card lists its sources by number, reference and identifier. What its author
found where in each source is kept in card-sources/, at the card's own path, so
that reviews do not load it. Both files are checked together.

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
SOURCE_NOTES = ROOT / "card-sources"
FRONTMATTER_KEYS = ["id", "name", "type", "field", "applies_when", "version"]
LABELS = ["Question.", "Why it matters.", "Resolved by.", "Benchmark."]
LOADED_WORDS = ["fatal", "red flag", "suspicious", "killer", "fraud", "misconduct"]
PREFIX = {"core": "C-", "technique": "T-", "claim": "CL-"}
ITEMS = {"core": (2, 4), "technique": (5, 8), "claim": (5, 8)}
APPLIES_WHEN_WORDS = 45


def table_rows(text, columns):
    for row in text.splitlines():
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if row.startswith("|") and len(cells) >= columns and cells[0].isdigit():
            yield int(cells[0]), cells[1:columns]


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
            for number, (reference, identifier) in table_rows(content, 3):
                sources[number] = {"reference": reference, "identifier": identifier}
        else:
            items.append((title.strip(), content))
    return meta, items, sources


def notes_path(card):
    return SOURCE_NOTES / Path(card).resolve().relative_to(CARDS)


def parse_notes(path):
    """Rows of a card's file in card-sources/: number -> identifier, access, where it supports the item."""
    if not path.is_file():
        return None
    return {
        number: {"identifier": identifier, "access": access, "where": where}
        for number, (identifier, access, where) in table_rows(path.read_text(encoding="utf-8"), 4)
    }


def card_files():
    return sorted(path for path in CARDS.rglob("*.md") if path.name not in ("README.md", "INDEX.md"))


def wording_problems(text):
    found = []
    lowered = text.casefold()
    for word in LOADED_WORDS:
        if word in lowered:
            found.append(f"loaded word {word!r}: cards ask questions, they do not accuse")
    for quoted in re.findall(r'"([^"\n]+)"', text):
        if len(quoted.split()) >= 15:
            found.append(f"quotation of 15 words or more: {quoted[:60]!r}")
    return found


def problems(path):
    """Return a list of format problems for one card and its file of source notes."""
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
        found.append("the card name has no parentheses; define an abbreviation at its first use in an item, or in an Abbreviations line under the title")
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
        if not re.match(r"^(doi:10\.\d{4,9}/\S+|https://\S+)$", source["identifier"]):
            found.append(f"source {number}: identifier must be doi:... or an https URL")
        if not re.search(r"\([^()]*\b(19|20)\d{2}\b[^()]*\)", source["reference"]):
            found.append(f"source {number}: reference needs a year in parentheses")
    found += wording_problems(path.read_text(encoding="utf-8"))

    notes_file = notes_path(path)
    notes = parse_notes(notes_file)
    where = notes_file.relative_to(ROOT).as_posix()
    if notes is None:
        found.append(f"{where} is missing: it says where each source supports its item")
        return found
    if sorted(notes) != sorted(sources):
        found.append(f"{where} lists sources {sorted(notes)}, but the card lists {sorted(sources)}")
    for number, note in notes.items():
        if number in sources and note["identifier"] != sources[number]["identifier"]:
            found.append(f"{where}: source {number} has identifier {note['identifier']!r}, but the card has {sources[number]['identifier']!r}")
        if note["access"] not in ("full text", "abstract"):
            found.append(f"{where}: source {number}: access must be 'full text' or 'abstract'")
        if len(note["where"]) <= 20:
            found.append(f"{where}: source {number}: say where the source supports the item")
    found += [f"{where}: {problem}" for problem in wording_problems(notes_file.read_text(encoding="utf-8"))]
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


def notes_without_card():
    cards = {path.relative_to(CARDS) for path in card_files()}
    return sorted(path.relative_to(ROOT).as_posix() for path in SOURCE_NOTES.rglob("*.md")
                  if path.name != "README.md" and path.relative_to(SOURCE_NOTES) not in cards)


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
        for orphan in notes_without_card():
            bad += 1
            print(f"{orphan}: no card has this path")
    print(f"{len(paths)} card(s) checked, {bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
