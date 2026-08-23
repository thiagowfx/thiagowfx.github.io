import tempfile
import unittest
from pathlib import Path

from check_broken_internal_links import (
    check_broken_links,
    extract_ref_links,
    validate_heading_anchor,
)


class CheckBrokenInternalLinksTest(unittest.TestCase):
    def test_finds_missing_posts_and_anchors(self):
        with tempfile.TemporaryDirectory() as directory:
            posts = Path(directory)
            target = posts / "2026-01-01-target.md"
            source = posts / "2026-01-02-source.md"
            target.write_text("## Existing **heading**\n", encoding="utf-8")
            source.write_text(
                '{{< ref "2026-01-01-target#existing-heading" >}}\n'
                '{{< ref "2026-01-01-target#missing" >}}\n'
                '{{< ref "missing-post" >}}\n'
                '{{< ref "/tags/coding" >}}\n',
                encoding="utf-8",
            )

            self.assertEqual(
                extract_ref_links(source)[0],
                (
                    "2026-01-01-target#existing-heading",
                    1,
                    '{{< ref "2026-01-01-target#existing-heading" >}}',
                ),
            )
            self.assertTrue(validate_heading_anchor(target, "existing-heading"))
            self.assertEqual(check_broken_links(posts), (2, [source]))

    def test_accepts_valid_links_in_nested_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            posts = Path(directory)
            nested = posts / "coding"
            nested.mkdir()
            (nested / "2026-01-01-target.md").write_text("# Target\n", encoding="utf-8")
            (posts / "source.md").write_text(
                '{{< ref "posts/coding/2026-01-01-target" >}}\n', encoding="utf-8"
            )

            self.assertEqual(check_broken_links(posts), (0, []))


if __name__ == "__main__":
    unittest.main()
