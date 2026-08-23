import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_i18n


class CheckI18nTest(unittest.TestCase):
    def test_load_catalog_rejects_invalid_values(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = Path(directory) / "bad.toml"
            catalog.write_text('valid = "text"\nempty = ""\n', encoding="utf-8")

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertIsNone(check_i18n.load_catalog(catalog))

            self.assertIn("Values must be non-empty strings: empty", output.getvalue())

    def test_main_checks_keys_and_order(self):
        with tempfile.TemporaryDirectory() as directory:
            i18n = Path(directory)
            reference = i18n / "en.toml"
            reference.write_text('first = "First"\nsecond = "Second"\n', encoding="utf-8")
            (i18n / "ordered.toml").write_text(
                'first = "Primeiro"\nsecond = "Segundo"\n', encoding="utf-8"
            )
            (i18n / "reordered.toml").write_text(
                'second = "Segundo"\nfirst = "Primeiro"\n', encoding="utf-8"
            )

            output = io.StringIO()
            with (
                patch.object(check_i18n, "I18N_DIR", i18n),
                patch.object(check_i18n, "REFERENCE_CATALOG", reference),
                contextlib.redirect_stdout(output),
            ):
                self.assertEqual(check_i18n.main(), 1)

            self.assertIn("Key order must match", output.getvalue())


if __name__ == "__main__":
    unittest.main()
