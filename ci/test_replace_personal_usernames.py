import tempfile
import unittest
from pathlib import Path

from replace_personal_usernames import fix_file, main


class ReplacePersonalUsernamesTest(unittest.TestCase):
    def test_replaces_both_personal_usernames(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text(
                "thiago.perrotta@host\ntperrotta@host\nother@host\n", encoding="utf-8"
            )

            self.assertTrue(fix_file(post))
            self.assertEqual(
                post.read_text(encoding="utf-8"),
                "thiago@host\nthiago@host\nother@host\n",
            )
            self.assertFalse(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
