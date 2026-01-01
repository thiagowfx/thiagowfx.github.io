#!/usr/bin/env python3
"""
Forbid external image URLs in layout files.
Images should be served locally from static/ directory.
"""

import re
import sys
from pathlib import Path

# Pattern to match external image URLs in src attributes
# Matches: src="http..." or src='http...' or src={{ ... | absURL }}
EXTERNAL_IMAGE_PATTERN = re.compile(
    r'src\s*=\s*["\']https?://',
    re.IGNORECASE
)

# Allowed external domains (empty by default - all external images should be local)
ALLOWED_EXTERNAL_DOMAINS = set()


def check_file(filepath: str) -> bool:
    """Check if file contains external image URLs."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return True  # Skip binary files

    lines = content.split('\n')
    errors = []

    for line_num, line in enumerate(lines, 1):
        if EXTERNAL_IMAGE_PATTERN.search(line):
            errors.append(f"{filepath}:{line_num}: External image URL found: {line.strip()}")

    if errors:
        for error in errors:
            print(error)
        return False

    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: forbid-external-images.py <file1> [file2] ...")
        return 0

    all_ok = True
    for filepath in sys.argv[1:]:
        if not check_file(filepath):
            all_ok = False

    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
