import tempfile
import unittest
from pathlib import Path

from replace_console_code_fences import fix_file, main, replace_console_code_fences


class ReplaceConsoleCodeFencesTest(unittest.TestCase):
    def test_replaces_console_fences_only(self):
        self.assertEqual(
            replace_console_code_fences("```console\n% command\n```\n```shell\n% keep\n```\n"),
            "```shell\n% command\n```\n```shell\n% keep\n```\n",
        )

    def test_fix_file_reports_change(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("```console\noutput\n```\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
