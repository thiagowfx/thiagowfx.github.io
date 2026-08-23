import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from check_single_category import check_file, main


class CheckSingleCategoryTest(unittest.TestCase):
    def test_accepts_zero_or_one_category(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("---\ncategories:\n  - coding\n---\n", encoding="utf-8")
            self.assertTrue(check_file(post))

    def test_rejects_multiple_categories_and_invalid_type(self):
        with tempfile.TemporaryDirectory() as directory:
            multiple = Path(directory) / "multiple.md"
            scalar = Path(directory) / "scalar.md"
            multiple.write_text(
                "---\ncategories:\n  - coding\n  - dev\n---\n", encoding="utf-8"
            )
            scalar.write_text("---\ncategories: coding\n---\n", encoding="utf-8")

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(check_file(multiple))
                self.assertFalse(check_file(scalar))
                with patch("sys.argv", ["check_single_category.py", str(multiple)]):
                    self.assertEqual(main(), 1)


if __name__ == "__main__":
    unittest.main()
