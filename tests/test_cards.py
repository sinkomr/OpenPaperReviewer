"""Format checks for checklist cards. Run with: python3 -m unittest discover -s tests"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "plugin" / "skills" / "open-paper-reviewer" / "references" / "checklists"
FRONTMATTER_KEYS = ["id", "name", "type", "field", "applies_when", "version"]
LABELS = ["Question.", "Why it matters.", "Resolved by.", "Benchmark."]
LOADED_WORDS = ["fatal", "red flag", "suspicious", "killer", "fraud", "misconduct"]


def parse(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        raise AssertionError(f"{path.name}: no frontmatter")
    meta = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"')
    body = match.group(2)
    sections = re.split(r"^## ", body, flags=re.MULTILINE)[1:]
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
    return sorted(path for path in CARDS.rglob("*.md") if path.name != "README.md")


class CardFormat(unittest.TestCase):
    def test_there_are_cards(self):
        self.assertTrue(any(path.parent.name == "core" for path in card_files()))

    def test_every_card(self):
        seen_ids = set()
        for path in card_files():
            with self.subTest(card=str(path.relative_to(CARDS))):
                meta, items, sources = parse(path)
                self.assertEqual([key for key in FRONTMATTER_KEYS if key not in meta], [], "missing frontmatter keys")
                self.assertNotIn(meta["id"], seen_ids, "duplicate card id")
                seen_ids.add(meta["id"])

                folder = path.parent.name
                if folder == "core":
                    self.assertEqual((meta["type"], meta["field"]), ("core", "any"))
                    self.assertTrue(meta["id"].startswith("C-"))
                    self.assertTrue(2 <= len(items) <= 4, f"a core card has two to four items, found {len(items)}")
                else:
                    self.assertEqual((meta["type"], meta["field"]), ("technique", folder))
                    self.assertTrue(meta["id"].startswith("T-"))
                    self.assertTrue(5 <= len(items) <= 8, f"a technique card has five to eight items, found {len(items)}")

                used = set()
                for number, (title, content) in enumerate(items, 1):
                    self.assertTrue(title.startswith(f"{number}. "), f"item heading should start '{number}. ': {title!r}")
                    for label in LABELS:
                        self.assertEqual(content.count(f"**{label}**"), 1, f"item {number} needs exactly one '{label}' line")
                    benchmark = content.split("**Benchmark.**", 1)[1].strip().splitlines()[0]
                    cited = [int(value) for value in re.findall(r"\[(\d+)\]", benchmark)]
                    if not cited:
                        self.assertEqual(folder, "core", f"item {number} of a technique card needs a benchmark source")
                        self.assertTrue(benchmark.startswith("None needed"), f"item {number}: benchmark must cite a source or say 'None needed'")
                    for value in cited:
                        self.assertIn(value, sources, f"item {number} cites [{value}], which is not in Sources")
                    used.update(cited)
                self.assertEqual(sorted(set(sources) - used), [], "sources that no item cites")

                for number, source in sources.items():
                    self.assertIn(source["access"], ("full text", "abstract"), f"source {number}: access must be 'full text' or 'abstract'")
                    self.assertRegex(source["identifier"], r"^(doi:10\.\d{4,9}/\S+|https://\S+)$", f"source {number}: identifier must be doi:... or an https URL")
                    self.assertRegex(source["reference"], r"\([^()]*\b(19|20)\d{2}\b[^()]*\)", f"source {number}: reference needs a year in parentheses")
                    self.assertTrue(len(source["where"]) > 20, f"source {number}: say where the source supports the item")

                lowered = path.read_text(encoding="utf-8").casefold()
                for word in LOADED_WORDS:
                    self.assertNotIn(word, lowered, f"loaded word {word!r}: cards ask questions, they do not accuse")
                for quoted in re.findall(r'"([^"\n]+)"', path.read_text(encoding="utf-8")):
                    self.assertLess(len(quoted.split()), 15, f"quotation of 15 words or more: {quoted[:60]!r}")


if __name__ == "__main__":
    unittest.main()
