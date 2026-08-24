import tempfile
import unittest
from pathlib import Path

from normalize_parenthetical_equals import fix_file, main, normalize_parenthetical_equals


class NormalizeParentheticalEqualsTest(unittest.TestCase):
    def test_removes_space_between_open_parenthesis_and_equals_in_prose(self):
        content = "London ( = capital of the UK).\nAlready correct (=capital).\nTabs (\t=work too).\n"
        expected = "London (=capital of the UK).\nAlready correct (=capital).\nTabs (=work too).\n"

        self.assertEqual(normalize_parenthetical_equals(content), expected)

    def test_skips_frontmatter_fenced_code_and_inline_code(self):
        content = """---
title: Keep ( = unchanged
---
Change ( = this.
`inline ( = code`
```text
fenced ( = code
```
~~~text
fenced ( = code
~~~
"""
        expected = content.replace("Change ( = this.", "Change (=this.")

        self.assertEqual(normalize_parenthetical_equals(content), expected)

    def test_fix_file_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("Before ( = after.\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertFalse(fix_file(post))
            self.assertEqual(post.read_text(encoding="utf-8"), "Before (=after.\n")
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
