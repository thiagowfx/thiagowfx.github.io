#!/usr/bin/env python3
"""Detect duplicate LeetCode posts by problem number.

This script checks for multiple posts about the same LeetCode problem
to prevent accidentally creating duplicates.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

def extract_problem_number(filepath):
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

def main():
    """Check for duplicate LeetCode problem numbers."""
    content_dir = Path('content/posts')

    # Map problem number to list of files
    problems = defaultdict(list)

    for filepath in content_dir.glob('*leetcode*.md'):
        problem_num = extract_problem_number(filepath)
        if problem_num is not None:
            problems[problem_num].append(filepath.name)

    # Check for duplicates
    has_duplicates = False
    for problem_num in sorted(problems.keys()):
        if len(problems[problem_num]) > 1:
            has_duplicates = True
            print(f"❌ Duplicate LeetCode #{problem_num}:")
            for filename in sorted(problems[problem_num]):
                print(f"   - {filename}")

    if has_duplicates:
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()
