#!/usr/bin/env python3
"""Check that a pull request to the reviews branch touches exactly one review folder.

Usage (run inside a checkout of the pull request):
    check_review_pr.py --base origin/reviews

Prints the review folder, relative to the repository root, and exits 0. Exits 1
with a message if the pull request changes anything outside a single folder of
the form <paper-id>/<paper-version>/<reviewer>-<date>/.

File names in a pull request are untrusted, so every path component is checked
against a strict pattern before it is used anywhere.

Standard library only.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")
FILE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}\.(md|json|txt)$")


def review_folder(paths):
    """Return the single review folder that every changed path sits in, or raise ValueError."""
    if not paths:
        raise ValueError("the pull request changes no files")
    folders = set()
    for path in paths:
        parts = path.split("/")
        if len(parts) < 4:
            raise ValueError(f"{path!r} is outside a review folder; a review lives at <paper-id>/<paper-version>/<reviewer>-<date>/")
        if any(not COMPONENT.match(part) or part.startswith(".") for part in parts[:-1]):
            raise ValueError(f"{path!r} has a folder name with characters that are not allowed")
        if not FILE_NAME.match(parts[-1]):
            raise ValueError(f"{path!r} is not a .md, .json or .txt file with a plain name")
        folders.add("/".join(parts[:3]))
    if len(folders) > 1:
        raise ValueError("the pull request touches more than one review folder: " + ", ".join(sorted(folders)))
    return folders.pop()


def changed_paths(base):
    out = subprocess.run(
        ["git", "diff", "--name-only", "-z", f"{base}...HEAD"], capture_output=True, check=True
    ).stdout.decode("utf-8", errors="replace")
    return [path for path in out.split("\0") if path]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", required=True, help="the base ref, for example origin/reviews")
    args = parser.parse_args()
    try:
        print(review_folder(changed_paths(args.base)))
    except ValueError as exc:
        sys.exit(f"check_review_pr: {exc}")
    except subprocess.CalledProcessError as exc:
        sys.exit(f"check_review_pr: git failed: {exc.stderr.decode(errors='replace').strip()}")


if __name__ == "__main__":
    main()
