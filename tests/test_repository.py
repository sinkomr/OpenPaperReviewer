"""Tests for packaging, generated files and the maintenance scripts.

Run with: python3 -m unittest discover -s tests
"""
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"
SKILL = PLUGIN / "skills" / "open-paper-reviewer"
REFERENCES = SKILL / "references"
FIXTURE = ROOT / "tests" / "fixtures" / "good-review"


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Packaging(unittest.TestCase):
    def setUp(self):
        self.claude = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.codex = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")

    def test_one_name_and_version_everywhere(self):
        frontmatter = re.match(r"^---\n(.*?)\n---", self.skill_text, re.DOTALL).group(1)
        skill_name = re.search(r"^name: (.+)$", frontmatter, re.MULTILINE).group(1).strip()
        skill_version = re.search(r'^\s+version: "(.+)"$', frontmatter, re.MULTILINE).group(1)
        self.assertEqual({self.claude["name"], self.codex["name"], skill_name, SKILL.name}, {"open-paper-reviewer"})
        self.assertEqual({self.claude["version"], self.codex["version"], skill_version}, {self.claude["version"]})

    def test_marketplaces_point_at_the_plugin_folder(self):
        claude_market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        codex_market = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(claude_market["plugins"][0]["name"], "open-paper-reviewer")
        self.assertEqual(claude_market["plugins"][0]["source"], "./plugin")
        self.assertEqual(codex_market["plugins"][0]["name"], "open-paper-reviewer")
        self.assertEqual(codex_market["plugins"][0]["source"]["path"], "./plugin")
        self.assertEqual(claude_market["name"], codex_market["name"])

    def test_skill_frontmatter_is_portable(self):
        frontmatter = re.match(r"^---\n(.*?)\n---", self.skill_text, re.DOTALL).group(1)
        keys = set(re.findall(r"^([a-z-]+):", frontmatter, re.MULTILINE))
        self.assertTrue(keys <= {"name", "description", "license", "allowed-tools", "metadata"}, keys)
        description = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE).group(1)
        self.assertLessEqual(len(description), 1024)
        self.assertNotRegex(description, r"[<>]")

    def test_plugin_folder_meets_directory_limits(self):
        # The files that would be published: tracked, or new and not ignored. Ignored local
        # clutter such as Finder's .DS_Store never reaches the repository.
        listed = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "--", "plugin"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        files = [ROOT / line for line in listed if "results" not in Path(line).parts and (ROOT / line).is_file()]
        self.assertTrue(files, "git lists no plugin files")
        self.assertLessEqual(len(files), 512)
        for path in files:
            with self.subTest(file=str(path.relative_to(PLUGIN))):
                self.assertNotIn(path.name, (".DS_Store", "Thumbs.db", "desktop.ini"))
                self.assertLess(path.stat().st_size, 256 * 1024)
                self.assertIn(path.suffix, (".md", ".json", ".py", ".sh", ".svg", ".yaml", ".yml", ""), "only text and image files belong in the plugin")
        self.assertTrue((PLUGIN / "LICENSE").is_file())
        readme_words = re.sub(r"```.*?```", "", (PLUGIN / "README.md").read_text(encoding="utf-8"), flags=re.DOTALL).split()
        self.assertGreaterEqual(len(readme_words), 40)

    def test_every_file_the_skill_names_exists(self):
        for relative in re.findall(r"`((?:references|scripts)/[\w./<>-]+)`", self.skill_text):
            if "<" in relative:
                continue
            with self.subTest(path=relative):
                self.assertTrue((SKILL / relative).exists(), f"SKILL.md names {relative}, which does not exist")


class MethodConsistency(unittest.TestCase):
    def setUp(self):
        self.rubric = json.loads((REFERENCES / "rubric.json").read_text(encoding="utf-8"))
        self.templates = {path.stem: path.read_text(encoding="utf-8") for path in (REFERENCES / "templates").glob("*.md")}
        self.phases = {path.name: path.read_text(encoding="utf-8") for path in sorted((REFERENCES / "phases").glob("*.md"))}

    def test_eight_phases_in_order(self):
        self.assertEqual([name[:2] for name in self.phases], [f"{n:02d}" for n in range(8)])
        for name, text in self.phases.items():
            with self.subTest(phase=name):
                self.assertRegex(text, r"^# Phase \d: ")
                self.assertRegex(text, r"(?m)^Purpose: ")

    def test_templates_use_the_rubric_values(self):
        block, entry = self.templates["claim-block"], self.templates["claim-entry"]
        for item in self.rubric["verdict"] + self.rubric["severity"] + self.rubric["confidence"]:
            self.assertIn(item["value"], block)
        for item in self.rubric["claim_type"]:
            self.assertIn(item["value"], entry)
        for item in self.rubric["citation_verdict"]:
            self.assertIn(item["value"], self.templates["reference-deep-dive"])
        for item in self.rubric["citation_error"]:
            self.assertIn(item["value"], self.templates["claims-and-citations"])

    def test_phases_name_only_templates_that_exist(self):
        known = set(self.templates)
        for name, text in self.phases.items():
            for mentioned in re.findall(r"`([a-z]+(?:-[a-z]+)+)` template", text):
                with self.subTest(phase=name, template=mentioned):
                    self.assertIn(mentioned, known)

    def test_phase_files_are_free_of_tool_specific_instructions(self):
        for name, text in self.phases.items():
            with self.subTest(phase=name):
                self.assertNotRegex(text, r"(?i)\b(claude|codex|chatgpt|sub-?agent|scripts/|validate_review|\.py\b)")

    def test_generated_files_are_up_to_date(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_prompts.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class ReviewPullRequests(unittest.TestCase):
    def setUp(self):
        self.module = load(ROOT / "scripts" / "check_review_pr.py")

    def test_one_review_folder_is_accepted(self):
        paths = ["arxiv-0000.00000/v2/someone-2026-01-15/run.json", "arxiv-0000.00000/v2/someone-2026-01-15/03_scrutiny/group_A.md"]
        self.assertEqual(self.module.review_folder(paths), "arxiv-0000.00000/v2/someone-2026-01-15")

    def test_other_changes_are_refused(self):
        folder = "arxiv-0000.00000/v2/someone-2026-01-15"
        bad = [
            [],
            ["README.md"],
            [".github/workflows/validate-review.yml"],
            [f"{folder}/run.json", "arxiv-1111.11111/v1/other-2026-01-15/run.json"],
            [f"{folder}/paper.pdf"],
            [f"{folder}/.hidden/run.json"],
            [f"{folder}/$(touch x).md"],
            ['arxiv-0000.00000/v2/some one"; rm -rf ~/run.json'],
            ["a/b/run.json"],
        ]
        for paths in bad:
            with self.subTest(paths=paths):
                with self.assertRaises(ValueError):
                    self.module.review_folder(paths)


class ReviewIndex(unittest.TestCase):
    def test_index_lists_a_review_without_verdict_counts(self):
        module = load(ROOT / "scripts" / "build_index.py")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "https-example.org-fictional-mulch-study" / "v1" / "example-reviewer-2026-01-15"
            shutil.copytree(FIXTURE, folder)
            text, count, skipped = module.build(root)
        self.assertEqual((count, skipped), (1, []))
        self.assertIn("example-model-1", text)
        self.assertIn("| high |", text)
        self.assertIn("[open](https-example.org-fictional-mulch-study/v1/example-reviewer-2026-01-15/06_synthesis.md)", text)
        for word in ("Supported", "Unsupported", "Contradicted", "Critical"):
            self.assertNotIn(word, text.split("is not a ranking.")[-1], "the index must not show verdicts")

    def test_empty_index(self):
        module = load(ROOT / "scripts" / "build_index.py")
        with tempfile.TemporaryDirectory() as tmp:
            text, count, _ = module.build(Path(tmp))
        self.assertEqual(count, 0)
        self.assertIn("No reviews have been posted yet.", text)


if __name__ == "__main__":
    unittest.main()
