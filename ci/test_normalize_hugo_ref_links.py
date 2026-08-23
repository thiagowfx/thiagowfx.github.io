import tempfile
import unittest
from pathlib import Path

from normalize_hugo_ref_links import fix_file, main, normalize_hugo_ref_links


class NormalizeHugoRefLinksTest(unittest.TestCase):
    def test_normalizes_prefix_suffix_fragment_and_quote_style(self):
        content = (
            '{{< ref "content/posts/2026-01-01-post.md#heading" >}}\n'
            "{{% ref 'content/posts/other.md' %}}\n"
        )
        self.assertEqual(
            normalize_hugo_ref_links(content),
            '{{< ref "2026-01-01-post#heading" >}}\n{{% ref \'other\' %}}\n',
        )

    def test_fix_file_reports_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text('{{< ref "content/posts/target.md" >}}\n', encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertEqual(post.read_text(encoding="utf-8"), '{{< ref "target" >}}\n')
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
