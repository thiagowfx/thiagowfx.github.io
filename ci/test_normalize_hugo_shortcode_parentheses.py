import tempfile
import unittest
from pathlib import Path

from normalize_hugo_shortcode_parentheses import (
    fix_file,
    main,
    normalize_hugo_shortcode_parentheses,
)


class NormalizeHugoShortcodeParenthesesTest(unittest.TestCase):
    def test_removes_one_duplicate_pair_from_complete_shortcodes(self):
        content = 'See (({{< ref "post" >}})) and (({{% note %}})).\n'
        expected = 'See ({{< ref "post" >}}) and ({{% note %}}).\n'
        self.assertEqual(normalize_hugo_shortcode_parentheses(content), expected)

    def test_reports_unresolved_shortcodes(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("first\n(({{< broken\n", encoding="utf-8")

            self.assertEqual(fix_file(post), (False, [2]))
            self.assertEqual(main([str(post)]), 1)


if __name__ == "__main__":
    unittest.main()
