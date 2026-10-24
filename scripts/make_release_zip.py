#!/usr/bin/env python3
"""Build the zips that are attached to a release.

Usage:
    make_release_zip.py

Writes two files to dist/:

- open-paper-reviewer-plugin-<version>.zip: the plugin folder, for plugin
  uploads (claude.ai and Cowork plugin upload, OpenAI's plugin portal).
- open-paper-reviewer-skill-<version>.zip: the skill alone, for skill uploads.
  It holds one top-level folder, open-paper-reviewer/, with SKILL.md directly
  inside it, a copy of the licence, and no plugin manifest.

The regression cases (evals/), caches and system files are left out of both:
they are for developing the skill, not for using it.

Standard library only.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"
SKILL_NAME = "open-paper-reviewer"
SKILL = PLUGIN / "skills" / SKILL_NAME
SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_PARTS = {"__pycache__", "results", "__MACOSX"}
SKIP_TOP = {"evals"}


def version():
    return json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]


def included(folder):
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder)
        if (not path.is_file() or path.name in SKIP_NAMES or relative.parts[0] in SKIP_TOP
                or SKIP_PARTS & set(relative.parts) or path.suffix == ".pyc"):
            continue
        yield path, relative


def build_plugin_zip(target):
    count = 0
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, relative in included(PLUGIN):
            archive.write(path, relative.as_posix())
            count += 1
    return count


def build_skill_zip(target):
    count = 0
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, relative in included(SKILL):
            archive.write(path, f"{SKILL_NAME}/{relative.as_posix()}")
            count += 1
        archive.write(PLUGIN / "LICENSE", f"{SKILL_NAME}/LICENSE")
        count += 1
    return count


def main():
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for kind, build in (("plugin", build_plugin_zip), ("skill", build_skill_zip)):
        target = dist / f"{SKILL_NAME}-{kind}-{version()}.zip"
        count = build(target)
        print(f"wrote {target.relative_to(ROOT)}: {count} files, {target.stat().st_size // 1024} KiB")


if __name__ == "__main__":
    main()
