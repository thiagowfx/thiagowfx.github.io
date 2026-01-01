#!/usr/bin/env python3
"""
Sort tags in blog post frontmatter alphabetically.

This script processes markdown files in content/posts/, parses the YAML frontmatter,
extracts the tags array, sorts them alphabetically, and writes the corrected content
back to the file.
"""

import os
import re
import sys
from pathlib import Path


def sort_tags_in_file(file_path):
    """Sort tags alphabetically in a markdown file and return whether changes were made."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find frontmatter between --- and ---
    match = re.match(r"^(---\n.*?\n---)", content, re.DOTALL)
    if not match:
        return False

    frontmatter = match.group(1)
    rest_of_content = content[len(frontmatter) :]

    # Extract and sort tags
    tags_pattern = r"(tags:\s*\n)((?:\s*-\s+\S+\n?)+)"
    tags_match = re.search(tags_pattern, frontmatter)

    if not tags_match:
        return False

    indent = "  "  # Default indentation
    tags_intro = tags_match.group(1)
    tags_text = tags_match.group(2)

    # Extract tag names
    tags = re.findall(r"-\s+(\S+)", tags_text)

    if len(tags) <= 1:
        return False  # No need to sort single or empty tags

    # Sort tags
    sorted_tags = sorted(tags)

    # Check if already sorted
    if tags == sorted_tags:
        return False

    # Build new tags section with proper indentation
    new_tags_text = "\n".join([f"{indent}- {tag}" for tag in sorted_tags]) + "\n"
    new_tags_section = tags_intro + new_tags_text

    # Replace old tags with sorted tags
    new_frontmatter = (
        frontmatter[: tags_match.start()]
        + new_tags_section
        + frontmatter[tags_match.end() :]
    )
    new_content = new_frontmatter + rest_of_content

    # Write back to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    if len(sys.argv) > 1:
        # Process specific files provided as arguments
        file_paths = [Path(f) for f in sys.argv[1:]]
    else:
        # Process all markdown files in content/posts/
        posts_dir = Path("content/posts")
        if not posts_dir.exists():
            print(f"Error: {posts_dir} directory not found")
            return 1

        file_paths = list(posts_dir.glob("**/*.md"))

    modified_count = 0
    for file_path in file_paths:
        if sort_tags_in_file(file_path):
            print(f"Fixed: {file_path}")
            modified_count += 1

    if modified_count > 0:
        print(f"\nSorted tags in {modified_count} file(s)")
        return 0
    else:
        print("No files needed tag sorting")
        return 0


if __name__ == "__main__":
    sys.exit(main())
