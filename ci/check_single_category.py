#!/usr/bin/env python3
"""
Enforce that each post has exactly one category.
"""

import sys
import yaml
from pathlib import Path


def check_file(filepath):
    """Check if a post has exactly one category."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract frontmatter
    if not content.startswith('---'):
        print(f"{filepath}: Missing frontmatter")
        return False
    
    # Find the end of frontmatter
    try:
        _, frontmatter_text, _ = content.split('---', 2)
    except ValueError:
        print(f"{filepath}: Invalid frontmatter")
        return False
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        print(f"{filepath}: Failed to parse YAML: {e}")
        return False
    
    if frontmatter is None:
        print(f"{filepath}: Empty frontmatter")
        return False
    
    categories = frontmatter.get('categories', [])
    
    if not isinstance(categories, list):
        print(f"{filepath}: 'categories' must be a list")
        return False
    
    if len(categories) == 0:
        print(f"{filepath}: Missing 'categories' field")
        return False
    
    if len(categories) > 1:
        print(f"{filepath}: Multiple categories found: {categories}. Only one category is allowed.")
        return False
    
    return True


def main():
    """Check all provided files."""
    if not sys.argv[1:]:
        print("No files provided")
        return 0
    
    failed = False
    for filepath in sys.argv[1:]:
        if not check_file(filepath):
            failed = True
    
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
