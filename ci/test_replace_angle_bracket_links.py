import tempfile
import unittest
from pathlib import Path

from replace_angle_bracket_links import fix_file, main, replace_angle_bracket_links


class ReplaceAngleBracketLinksTest(unittest.TestCase):
    def test_replaces_prose_links_but_skips_frontmatter_and_code(self):
        content = """---
title: "[title](<https://example.com>)"
---
[prose](<https://example.com/path>)
```markdown
[code](<https://example.com>)
```
"""
        expected = content.replace(
            "[prose](<https://example.com/path>)", "[prose](https://example.com/path)"
        )
        self.assertEqual(replace_angle_bracket_links(content), expected)

    def test_fix_file_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("[text](<https://example.com>)\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertFalse(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
