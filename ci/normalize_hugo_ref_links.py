#!/usr/bin/env python3
"""Normalize targets in Hugo ref shortcode links."""

import re
import sys
from pathlib import Path


HUGO_REF_RE = re.compile(
    r'(?P<prefix>\{\{[<%]\s*ref\s+)(?P<quote>["\'])'
    r'(?P<target>[^"\']+)(?P=quote)'
)


def fix_file(filename):
    """Fix a single file, return True if modified."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = normalize_hugo_ref_links(content)

    if modified != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False


def normalize_hugo_ref_links(content):
    """Strip content/posts/ prefixes and .md suffixes from Hugo ref targets."""

    def normalize(match):
        target = match.group('target')
        target = target.removeprefix('content/posts/')

        path, separator, fragment = target.partition('#')
        path = path.removesuffix('.md')
        target = path + separator + fragment

        quote = match.group('quote')
        return f"{match.group('prefix')}{quote}{target}{quote}"

    return HUGO_REF_RE.sub(normalize, content)


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
