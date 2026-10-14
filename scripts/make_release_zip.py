#!/usr/bin/env python3
"""Build the plugin zip that is attached to a release.

Usage:
    make_release_zip.py

Writes dist/open-paper-reviewer-<version>.zip containing the plugin folder, for
people who install by uploading a file (claude.ai: Customize > Plugins > Upload
plugin). Eval results, caches and system files are left out.

Standard library only.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"
SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_PARTS = {"__pycache__", "results", "__MACOSX"}


def main():
    version = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    target = ROOT / "dist" / f"open-paper-reviewer-{version}.zip"
    target.parent.mkdir(exist_ok=True)
    count = 0
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            relative = path.relative_to(PLUGIN)
            if not path.is_file() or path.name in SKIP_NAMES or SKIP_PARTS & set(relative.parts) or path.suffix == ".pyc":
                continue
            archive.write(path, relative.as_posix())
            count += 1
    print(f"wrote {target.relative_to(ROOT)}: {count} files, {target.stat().st_size // 1024} KiB")


if __name__ == "__main__":
    main()
