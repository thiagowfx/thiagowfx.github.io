import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from check_required_frontmatter import check_file, main


class CheckRequiredFrontmatterTest(unittest.TestCase):
    def test_accepts_required_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text(
                "---\ntitle: Example\ndate: 2026-01-01\n---\nBody\n", encoding="utf-8"
            )
            self.assertTrue(check_file(post))

    def test_rejects_missing_and_invalid_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.md"
            invalid = Path(directory) / "invalid.md"
            missing.write_text("Body\n", encoding="utf-8")
            invalid.write_text("---\ntitle: [\n---\n", encoding="utf-8")

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(check_file(missing))
                self.assertFalse(check_file(invalid))
                with patch(
                    "sys.argv",
                    ["check_required_frontmatter.py", str(missing), str(invalid)],
                ):
                    self.assertEqual(main(), 1)


if __name__ == "__main__":
    unittest.main()
