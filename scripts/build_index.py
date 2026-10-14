#!/usr/bin/env python3
"""Build the index of posted reviews (README.md on the reviews branch).

Usage:
    build_index.py <checkout of the reviews branch> [--check]

Reads every <paper-id>/<paper-version>/<reviewer>-<date>/run.json and writes
README.md from the header in scripts/reviews-branch/README.header.md plus one
table row per review.

The index lists reviews. It does not rank papers and shows no verdict counts.

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HEADER = Path(__file__).resolve().parent / "reviews-branch" / "README.header.md"
COLUMNS = ["Paper", "Version", "Reviewer", "Date", "Model", "Effort", "Review", "Sources checked", "Person checked", "Status", "Folder"]


def cell(value):
    return " ".join(str(value).replace("|", "/").split()) or "-"


def paper_link(paper):
    title = cell(paper.get("title", ""))
    identifier = str(paper.get("identifier", "")).strip()
    lowered = identifier.casefold()
    if lowered.startswith("doi:"):
        url = "https://doi.org/" + identifier[4:]
    elif lowered.startswith("arxiv:"):
        url = "https://arxiv.org/abs/" + identifier[6:]
    elif lowered.startswith(("http://", "https://")):
        url = identifier
    else:
        return title
    return f"[{title}]({url})"


def row(folder, root):
    run = json.loads((folder / "run.json").read_text(encoding="utf-8"))
    paper, review = run.get("paper", {}), run.get("review", {})
    models = [m for m in run.get("models", []) if isinstance(m, dict)]
    relative = folder.relative_to(root).as_posix()
    checked = str(run.get("human_check", "")).strip()
    return {
        "sort": (relative.split("/")[0], str(review.get("finished", "")), relative),
        "cells": [
            paper_link(paper),
            cell(paper.get("version", "")),
            cell(run.get("reviewer", "")),
            cell(review.get("finished", "")),
            cell("; ".join(str(m.get("id", "")) for m in models)),
            cell("; ".join(str(m.get("effort", "")) for m in models)),
            cell(review.get("mode", "")),
            cell(review.get("citation_verification", "")),
            "no" if checked.casefold() in ("", "none") else "yes",
            cell(review.get("status", "")),
            f"[open]({relative}/06_synthesis.md)",
        ],
    }


def build(root):
    rows, skipped = [], []
    for run_file in sorted(root.glob("*/*/*/run.json")):
        if any(part.startswith(".") for part in run_file.relative_to(root).parts):
            continue
        try:
            rows.append(row(run_file.parent, root))
        except (json.JSONDecodeError, OSError, AttributeError) as exc:
            skipped.append(f"{run_file.relative_to(root)}: {exc}")
    rows.sort(key=lambda item: item["sort"])
    lines = [HEADER.read_text(encoding="utf-8").rstrip(), ""]
    if rows:
        lines.append("| " + " | ".join(COLUMNS) + " |")
        lines.append("|" + "---|" * len(COLUMNS))
        lines.extend("| " + " | ".join(item["cells"]) + " |" for item in rows)
    else:
        lines.append("No reviews have been posted yet.")
    return "\n".join(lines) + "\n", len(rows), skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root")
    parser.add_argument("--check", action="store_true", help="exit 1 if README.md is out of date; write nothing")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    text, count, skipped = build(root)
    for line in skipped:
        print(f"skipped {line}", file=sys.stderr)
    target = root / "README.md"
    current = target.read_text(encoding="utf-8") if target.is_file() else None
    if args.check:
        if current != text:
            sys.exit("README.md is out of date")
        print(f"index is up to date ({count} review(s))")
        return
    if current != text:
        target.write_text(text, encoding="utf-8")
    print(f"index lists {count} review(s)")


if __name__ == "__main__":
    main()
