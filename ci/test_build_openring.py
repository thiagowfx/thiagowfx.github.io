import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class BuildOpenringTest(unittest.TestCase):
    def make_repo(self, openring_body: str) -> tuple[Path, dict[str, str]]:
        root = Path(self.directory.name)
        (root / "ci").mkdir()
        (root / "data").mkdir()
        (root / "layouts" / "partials").mkdir(parents=True)
        shutil.copy(Path(__file__).with_name("build_openring.sh"), root / "ci")
        (root / "data" / "blogroll.yaml").write_text(
            "blogs:\n  - feed: https://example.com/feed.xml\n", encoding="utf-8"
        )

        binary_directory = root / "bin"
        binary_directory.mkdir()
        openring = binary_directory / "openring"
        openring.write_text(f"#!/usr/bin/env bash\n{openring_body}\n", encoding="utf-8")
        openring.chmod(0o755)
        environment = os.environ.copy()
        environment["PATH"] = f"{binary_directory}:{environment['PATH']}"
        return root, environment

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.directory.cleanup()

    def test_writes_openring_output(self):
        root, environment = self.make_repo('echo "<article>generated</article>"')

        result = subprocess.run(
            ["bash", str(root / "ci" / "build_openring.sh")],
            cwd=root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (root / "layouts" / "partials" / "openring.html").read_text(
                encoding="utf-8"
            ),
            "<article>generated</article>\n",
        )

    def test_writes_stub_when_openring_fails(self):
        root, environment = self.make_repo("exit 1")

        result = subprocess.run(
            ["bash", str(root / "ci" / "build_openring.sh")],
            cwd=root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "OpenRing generation will be enabled on deploy",
            (root / "layouts" / "partials" / "openring.html").read_text(
                encoding="utf-8"
            ),
        )


if __name__ == "__main__":
    unittest.main()
