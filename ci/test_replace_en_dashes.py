import unittest

from replace_en_dashes import replace_dashes


class ReplaceDashesTest(unittest.TestCase):
    def test_replaces_dashes_at_line_start_after_prose_wrap(self):
        self.assertEqual(
            replace_dashes("First line\n-- continued line.\n"),
            "First line\n– continued line.\n",
        )

    def test_replaces_dashes_inside_prose(self):
        self.assertEqual(replace_dashes("Before -- after.\n"), "Before – after.\n")

    def test_skips_frontmatter_and_code(self):
        content = """---
title: Keep -- unchanged
---
`inline -- code`
```shell
command -- flag
```
"""
        self.assertEqual(replace_dashes(content), content)


if __name__ == '__main__':
    unittest.main()
