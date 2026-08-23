import tempfile
import unittest
from pathlib import Path

from remove_more_markers import fix_file, main, remove_more_markers


class RemoveMoreMarkersTest(unittest.TestCase):
    def test_removes_dedicated_and_inline_markers(self):
        self.assertEqual(
            remove_more_markers("Before\n<!--more-->\nAfter <!--more--> text\n"),
            "Before\nAfter  text\n",
        )

    def test_fix_file_returns_changed_state(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("Before\n<!--more-->\nAfter\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertFalse(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
