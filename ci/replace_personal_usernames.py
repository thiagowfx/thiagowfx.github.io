#!/usr/bin/env python3
"""Replace personal usernames with generic thiago@ in blog posts."""

import sys
from pathlib import Path


def fix_file(filename):
    """Fix a single file, return True if modified."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = content
    modified = modified.replace('thiago.perrotta@', 'thiago@')
    modified = modified.replace('tperrotta@', 'thiago@')

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


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
