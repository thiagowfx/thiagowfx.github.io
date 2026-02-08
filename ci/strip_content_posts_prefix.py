#!/usr/bin/env python3
"""Strip content/posts/ prefix from Hugo ref shortcode links."""

import re
import sys
from pathlib import Path


def fix_file(filename):
    """Fix a single file, return True if modified."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = strip_prefix(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def strip_prefix(content):
    """Strip content/posts/ prefix from Hugo ref shortcode links."""
    return re.sub(
        r'(\{\{[<|%]\s*ref\s+["\'])content/posts/([^"\']+)(["\'])',
        r'\1\2\3',
        content,
    )


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
