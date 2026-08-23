import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("forbid-external-images.py")
SPEC = importlib.util.spec_from_file_location("forbid_external_images", SCRIPT)
assert SPEC and SPEC.loader
forbid_external_images = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(forbid_external_images)


class ForbidExternalImagesTest(unittest.TestCase):
    def test_rejects_external_images_and_reports_line(self):
        with tempfile.TemporaryDirectory() as directory:
            layout = Path(directory) / "layout.html"
            layout.write_text(
                '<p>local</p>\n<img src="https://example.com/image.png">\n', encoding="utf-8"
            )

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertFalse(forbid_external_images.check_file(str(layout)))

            self.assertIn(f"{layout}:2: External image URL found", output.getvalue())

    def test_accepts_local_and_allowed_external_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            layout = Path(directory) / "layout.html"
            layout.write_text(
                '<img src="/images/local.png">\n'
                '<script src="https://cdn.jsdelivr.net/chart.js"></script>\n',
                encoding="utf-8",
            )

            self.assertTrue(forbid_external_images.check_file(str(layout)))
            with patch("sys.argv", ["forbid-external-images.py", str(layout)]):
                self.assertEqual(forbid_external_images.main(), 0)


if __name__ == "__main__":
    unittest.main()
