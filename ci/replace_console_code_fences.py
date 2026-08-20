#!/usr/bin/env python3
"""Replace console code fences with shell code fences."""

import sys
from pathlib import Path


CONSOLE_CODE_FENCE = '```console'
SHELL_CODE_FENCE = '```shell'


def replace_console_code_fences(content):
    """Replace console code fences with shell code fences."""
    return content.replace(CONSOLE_CODE_FENCE, SHELL_CODE_FENCE)


def fix_file(filename):
    """Fix one file and return True when content changed."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = replace_console_code_fences(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def main(argv=None):
    argv = argv or sys.argv[1:]

    if not argv:
        markdown_files = list(Path('.').glob('**/*.md'))
        if not markdown_files:
            return 0
        argv = [str(f) for f in markdown_files]

    ret = 0
    for filename in argv:
        if fix_file(filename):
            print(f"Fixed: {filename}")
            ret = 1

    return ret


if __name__ == '__main__':
    sys.exit(main())
