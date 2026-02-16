#!/usr/bin/env python3
"""Replace ' - ' with em dashes in Markdown prose (outside code blocks and frontmatter)."""

import re
import sys
from pathlib import Path


def fix_file(filename):
    """Fix a single file, return True if modified."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = replace_dashes(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def replace_dashes(content):
    """Replace ' - ' with ' — ' in prose, skipping frontmatter and code blocks."""
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    in_code_block = False
    frontmatter_count = 0

    for line in lines:
        if line.strip() == '---' and frontmatter_count < 2:
            frontmatter_count += 1
            in_frontmatter = frontmatter_count == 1
            if frontmatter_count == 2:
                in_frontmatter = False
            result.append(line)
            continue

        if line.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if not in_frontmatter and not in_code_block:
            line = line.replace(' - ', ' — ')

        result.append(line)

    return '\n'.join(result)


def main(argv=None):
    argv = argv or sys.argv[1:]

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
