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

    def test_every_file_of_source_notes_has_a_card(self):
        self.assertEqual(checker.notes_without_card(), [])


class CardIndex(unittest.TestCase):
    def test_every_folder_has_a_title(self):
        # The index takes each folder's title from the Folders table in the checklists README.
        _builder_spec = importlib.util.spec_from_file_location("build_prompts", ROOT / "scripts" / "build_prompts.py")
        builder = importlib.util.module_from_spec(_builder_spec)
        _builder_spec.loader.exec_module(builder)
        titles = builder.folder_titles()
        folders = {path.parent.relative_to(checker.CARDS).as_posix() for path in checker.card_files() if path.parent.name != "core"}
        folders |= {folder.split("/", 1)[0] for folder in folders}
        for folder in sorted(folders):
            with self.subTest(folder=folder):
                self.assertIn(folder, titles, "add the folder and its title to the Folders table in the checklists README")

    def test_top_level_index_stays_short(self):
        # Every review reads the top-level index. Past this size it needs a third level (see the checklists README).
        size = (checker.CARDS / "INDEX.md").stat().st_size
        self.assertLess(size, 20000, f"the top-level card index is {size} bytes")


if __name__ == "__main__":
    unittest.main()
