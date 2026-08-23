import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path

from check_duplicate_coding_posts import (
    extract_bytebytego_slug,
    extract_leetcode_number,
    main,
)


class CheckDuplicateCodingPostsTest(unittest.TestCase):
    def test_extracts_problem_ids_from_filename_and_title(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            leetcode = root / "post.md"
            bytebytego = root / "another.md"
            leetcode.write_text('title: "LeetCode #42: Trapping Rain Water"\n', encoding="utf-8")
            bytebytego.write_text('title: "ByteByteGo: Triplet Sum"\n', encoding="utf-8")

            self.assertEqual(extract_leetcode_number(leetcode), 42)
            self.assertEqual(extract_bytebytego_slug(bytebytego), "triplet-sum")
            self.assertEqual(
                extract_leetcode_number(root / "2026-01-01-leetcode-7-reverse.md"), 7
            )

    def test_main_rejects_duplicate_problem_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            posts = root / "content" / "posts" / "coding"
            posts.mkdir(parents=True)
            for name in (
                "2026-01-01-leetcode-1-first.md",
                "2026-01-02-leetcode-1-second.md",
            ):
                (posts / name).write_text("---\n", encoding="utf-8")

            previous = Path.cwd()
            try:
                os.chdir(root)
                output = io.StringIO()
                with contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as error:
                    main()
            finally:
                os.chdir(previous)

            self.assertEqual(error.exception.code, 1)
            self.assertIn("Duplicate LeetCode #1", output.getvalue())


if __name__ == "__main__":
    unittest.main()
