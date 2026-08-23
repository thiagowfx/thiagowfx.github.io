import tempfile
import unittest
from pathlib import Path

from remove_utm_parameters import (
    fix_file,
    remove_utm_parameters,
    split_trailing_punctuation,
    strip_utm_parameters,
)


class RemoveUtmParametersTest(unittest.TestCase):
    def test_removes_tracking_parameters_and_preserves_other_url_parts(self):
        self.assertEqual(
            strip_utm_parameters(
                "https://example.com/path?utm_source=newsletter&keep=1#section"
            ),
            "https://example.com/path?keep=1#section",
        )
        self.assertEqual(
            remove_utm_parameters(
                "See https://example.com/?keep=1&amp;utm_medium=email).\n"
            ),
            "See https://example.com/?keep=1).\n",
        )
        self.assertEqual(split_trailing_punctuation("https://example.com/test)."), (
            "https://example.com/test",
            ").",
        ))

    def test_reports_unresolved_tokens_outside_urls(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text(
                "utm_source remains\nhttps://example.com/?utm_source=test\n", encoding="utf-8"
            )

            self.assertEqual(fix_file(post), (True, [1]))
            self.assertEqual(
                post.read_text(encoding="utf-8"), "utm_source remains\nhttps://example.com/\n"
            )


if __name__ == "__main__":
    unittest.main()
