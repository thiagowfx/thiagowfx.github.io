import unittest
from pathlib import Path


class ScriptCoverageTest(unittest.TestCase):
    def test_each_ci_script_has_a_matching_unit_test(self):
        ci = Path(__file__).parent
        scripts = [
            path
            for pattern in ("*.py", "*.sh")
            for path in ci.glob(pattern)
            if not path.name.startswith("test_")
        ]
        missing = [
            path.name
            for path in scripts
            if not (ci / f"test_{path.stem.replace('-', '_')}.py").is_file()
        ]

        self.assertEqual(missing, [], f"scripts without unit tests: {', '.join(missing)}")


if __name__ == "__main__":
    unittest.main()
