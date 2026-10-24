"""Format checks for checklist cards. Run with: python3 -m unittest discover -s tests

The rules live in scripts/check_card.py, which agents and contributors can run on one card.
"""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("check_card", ROOT / "scripts" / "check_card.py")
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)


class CardFormat(unittest.TestCase):
    def test_there_are_cards(self):
        self.assertTrue(any(path.parent.name == "core" for path in checker.card_files()))

    def test_every_card(self):
        for path in checker.card_files():
            with self.subTest(card=str(path.relative_to(checker.CARDS))):
                self.assertEqual(checker.problems(path), [])

    def test_ids_are_unique(self):
        self.assertEqual(checker.duplicate_ids(checker.card_files()), [])


class CardIndex(unittest.TestCase):
    def test_every_folder_has_a_title(self):
        # The index takes each folder's title from the heading of its README.md.
        folders = {path.parent for path in checker.card_files() if path.parent.name != "core"}
        folders |= {checker.CARDS / folder.relative_to(checker.CARDS).parts[0] for folder in folders}
        for folder in sorted(folders):
            with self.subTest(folder=str(folder.relative_to(checker.CARDS))):
                readme = folder / "README.md"
                self.assertTrue(readme.is_file(), "a folder of cards needs a README.md whose heading is its title")
                self.assertTrue(readme.read_text(encoding="utf-8").startswith("# "))

    def test_top_level_index_stays_short(self):
        # Every review reads the top-level index. If it grows past this, give it a third level:
        # fields, then subfields, then cards (see the checklists README).
        size = (checker.CARDS / "INDEX.md").stat().st_size
        self.assertLess(size, 20000, f"the top-level card index is {size} bytes")


if __name__ == "__main__":
    unittest.main()
