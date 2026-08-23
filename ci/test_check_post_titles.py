import tempfile
import unittest
from pathlib import Path

from check_post_titles import check_file, extract_title, main


class CheckPostTitlesTest(unittest.TestCase):
    def test_accepts_supported_title_formats(self):
        cases = {
            "2026-01-01-leetcode-1-two-sum.md": "LeetCode #1: Two Sum",
            "2026-01-01-bytebytego-triplet-sum.md": "ByteByteGo: Triplet Sum",
            "2026-01-01-aoc-day-1.md": "AoC 2026 Day 1: Historian Hysteria",
        }
        with tempfile.TemporaryDirectory() as directory:
            for filename, title in cases.items():
                path = Path(directory) / filename
                path.write_text(f'---\ntitle: "{title}"\n---\n', encoding="utf-8")
                self.assertIsNone(check_file(path))
                self.assertEqual(extract_title(path), title)

    def test_rejects_bad_title_and_ignores_unrelated_files(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "leetcode-1.md"
            unrelated = Path(directory) / "notes.md"
            bad.write_text("---\ntitle: Two Sum\n---\n", encoding="utf-8")
            unrelated.write_text("no front matter", encoding="utf-8")

            self.assertIn("title must match", check_file(bad))
            self.assertIsNone(check_file(unrelated))
            self.assertEqual(main([str(bad)]), 1)
            self.assertEqual(main([str(unrelated)]), 0)


if __name__ == "__main__":
    unittest.main()
