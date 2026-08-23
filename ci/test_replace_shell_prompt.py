import tempfile
import unittest
from pathlib import Path

from replace_shell_prompt import fix_file, main, replace_prompts_in_code_blocks


class ReplaceShellPromptTest(unittest.TestCase):
    def test_replaces_prompts_in_shell_fences_only(self):
        content = """Prose ❯ stays.
```shell
❯ shell
```
```python
❯ python
```
```zsh
❯ zsh
```
"""
        expected = content.replace("❯ shell", "% shell").replace("❯ zsh", "% zsh")
        self.assertEqual(replace_prompts_in_code_blocks(content), expected)

    def test_fix_file_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / "post.md"
            post.write_text("```bash\n❯ command\n```\n", encoding="utf-8")

            self.assertTrue(fix_file(post))
            self.assertFalse(fix_file(post))
            self.assertEqual(main([str(post)]), 0)


if __name__ == "__main__":
    unittest.main()
