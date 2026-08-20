#!/usr/bin/env python3
"""Remove duplicate parentheses around Hugo shortcodes."""

import re
import sys
from pathlib import Path


DOUBLE_PARENS_SHORTCODE_RE = re.compile(
    r'\(\((?P<shortcode>\{\{<[^{}\n]*>\}\}|\{\{%[^{}\n]*%\}\})\)\)'
)
UNRESOLVED_RE = re.compile(r'\(\(\{\{[<%]')


def normalize_hugo_shortcode_parentheses(content):
    """Remove one pair of duplicate parentheses around complete shortcodes."""
    return DOUBLE_PARENS_SHORTCODE_RE.sub(r'(\g<shortcode>)', content)


def fix_file(filename):
    """Fix one file and return its changed state and unresolved line numbers."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = normalize_hugo_shortcode_parentheses(content)
    changed = modified != content

    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)

    unresolved = [
        line_number
        for line_number, line in enumerate(modified.splitlines(), 1)
        if UNRESOLVED_RE.search(line)
    ]
    return changed, unresolved


def main(argv=None):
    argv = argv or sys.argv[1:]

    if not argv:
        markdown_files = list(Path('.').glob('**/*.md'))
        if not markdown_files:
            return 0
        argv = [str(f) for f in markdown_files]

    ret = 0
    for filename in argv:
        changed, unresolved = fix_file(filename)
        if changed:
            print(f"Fixed: {filename}")
            ret = 1
        for line_number in unresolved:
            print(
                f"{filename}:{line_number}: duplicate parentheses could not be removed automatically"
            )
            ret = 1

    return ret


if __name__ == '__main__':
    sys.exit(main())
