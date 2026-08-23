import tempfile
import unittest
from pathlib import Path

from replace_em_dashes import fix_file, main, replace_dashes


class ReplaceEmDashesTest(unittest.TestCase):
    def test_replaces_prose_but_skips_frontmatter_code_and_math(self):
        content = """---
title: Keep a - b
---
Change a - b.
- list item
`inline a - b`
```
code a - b
```
"""
        expected = content.replace("Change a - b.", "Change a — b.")
        self.assertEqual(replace_dashes(content), expected)

    def test_fix_file_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("Before a - b.\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertFalse(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
