#!/usr/bin/env python3
"""Replace ❯ with % in shell prompts within code blocks."""

import re
import sys
from pathlib import Path


def fix_file(filename):
    """Fix a single file, return True if modified."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = replace_prompts_in_code_blocks(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def replace_prompts_in_code_blocks(content):
    """Replace ❯ with % in shell, bash, zsh, sh code blocks."""
    # Match shell-specific code blocks
    # Pattern: ```(shell|bash|zsh|sh)\n[content]\n```
    pattern = r'(```(?:shell|bash|zsh|sh))\n(.*?)\n(```)'

    def replace_in_block(match):
        prefix = match.group(1)
        code = match.group(2)
        suffix = match.group(3)

        code = code.replace('❯', '%')

        return f'{prefix}\n{code}\n{suffix}'

    return re.sub(pattern, replace_in_block, content, flags=re.DOTALL)


def main(argv=None):
    argv = argv or sys.argv[1:]

    # If no args, find all markdown files and fix them
    if not argv:
        markdown_files = list(Path('content/posts').glob('*.md'))
        if not markdown_files:
            return 0
        argv = [str(f) for f in markdown_files]

    for filename in argv:
        fix_file(filename)

    return 0


if __name__ == '__main__':
    sys.exit(main())
