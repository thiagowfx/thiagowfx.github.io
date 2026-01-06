#!/usr/bin/env python3
"""Detect duplicate coding problem posts by problem number.

This script checks for multiple posts about the same LeetCode or ByteByteGo problem
to prevent accidentally creating duplicates.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

def extract_leetcode_number(filepath):
    """Extract LeetCode problem number from filename or content."""
    filename = Path(filepath).name

    # Match pattern like: 2025-12-02-leetcode-3-longest-substring...md
    match = re.search(r'leetcode-(\d+)', filename)
    if match:
        return int(match.group(1))

    # Also check the title in the file content
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match: title: "LeetCode #123" or similar
            title_match = re.search(r'title:.*?[Ll]eetcode\s+#?(\d+)', content)
            if title_match:
                return int(title_match.group(1))
    except (IOError, UnicodeDecodeError):
        pass

    return None

def extract_bytebytego_slug(filepath):
    """Extract ByteByteGo problem slug from filename or content."""
    filename = Path(filepath).name

    # Match pattern like: 2025-12-02-bytebytego-triplet-sum...md
    match = re.search(r'bytebytego-(.+?)(?:\.md)?$', filename)
    if match:
        return match.group(1).lower()

    # Also check the title in the file content
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match: title: "ByteByteGo: Problem Name"
            title_match = re.search(r'title:.*?ByteByteGo:\s*(.+?)(?:\n|")', content)
            if title_match:
                slug = title_match.group(1).lower()
                slug = re.sub(r'[^a-z0-9]+', '-', slug)
                return slug.strip('-')
    except (IOError, UnicodeDecodeError):
        pass

    return None

def main():
    """Check for duplicate LeetCode and ByteByteGo problem posts."""
    content_dir = Path('content/posts')

    # Map problem number/slug to list of files
    leetcode_problems = defaultdict(list)
    bytebytego_problems = defaultdict(list)
    has_duplicates = False

    for filepath in content_dir.glob('**/coding/*leetcode*.md'):
        problem_num = extract_leetcode_number(filepath)
        if problem_num is not None:
            leetcode_problems[problem_num].append(filepath.name)

    for filepath in content_dir.glob('**/coding/*bytebytego*.md'):
        problem_slug = extract_bytebytego_slug(filepath)
        if problem_slug is not None:
            bytebytego_problems[problem_slug].append(filepath.name)

    # Check for LeetCode duplicates
    for problem_num in sorted(leetcode_problems.keys()):
        if len(leetcode_problems[problem_num]) > 1:
            has_duplicates = True
            print(f"❌ Duplicate LeetCode #{problem_num}:")
            for filename in sorted(leetcode_problems[problem_num]):
                print(f"   - {filename}")

    # Check for ByteByteGo duplicates
    for problem_slug in sorted(bytebytego_problems.keys()):
        if len(bytebytego_problems[problem_slug]) > 1:
            has_duplicates = True
            print(f"❌ Duplicate ByteByteGo '{problem_slug}':")
            for filename in sorted(bytebytego_problems[problem_slug]):
                print(f"   - {filename}")

    if has_duplicates:
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()
