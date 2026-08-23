import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from sort_tags import main, sort_tags_in_file


class SortTagsTest(unittest.TestCase):
    def test_sorts_multiline_tags_and_preserves_post(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text(
                "---\ntitle: Post\ntags:\n  - linux\n  - coding\n---\nBody\n",
                encoding="utf-8",
            )

            self.assertTrue(sort_tags_in_file(post))
            self.assertEqual(
                post.read_text(encoding="utf-8"),
                "---\ntitle: Post\ntags:\n  - coding\n  - linux\n---\nBody\n",
            )
            self.assertFalse(sort_tags_in_file(post))

    def test_main_processes_explicit_files(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("---\ntags:\n  - b\n  - a\n---\n", encoding="utf-8")

            with (
                patch("sys.argv", ["sort_tags.py", str(post)]),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
