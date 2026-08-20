#!/usr/bin/env python3
"""Remove Hugo more markers from blog posts."""

import sys
from pathlib import Path


MORE_MARKER = '<!--more-->'


def remove_more_markers(content):
    """Remove Hugo more markers and their dedicated lines."""
    result = []

    for line in content.splitlines(keepends=True):
        if line.strip() == MORE_MARKER:
            continue
        result.append(line.replace(MORE_MARKER, ''))

    return ''.join(result)


def fix_file(filename):
    """Fix one file and return True when content changed."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = remove_more_markers(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def main(argv=None):
    argv = argv or sys.argv[1:]

    if not argv:
        markdown_files = list(Path('content/posts').glob('*.md'))
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
