#!/usr/bin/env python3
"""Check for broken Hugo ref shortcode links in markdown files."""

import os
import re
import sys
from pathlib import Path
from typing import List, Set, Tuple

# Find all markdown files in content/posts/
POSTS_DIR = Path("content/posts")


def find_all_markdown_files(root_dir: Path) -> List[Path]:
    """Find all markdown files in a directory and its subdirectories."""
    return list(root_dir.rglob("*.md"))


def extract_ref_links(file_path: Path) -> List[Tuple[str, int, str]]:
    """Extract Hugo ref shortcode links from a markdown file.

    Returns:
        List of tuples: (referenced_filename, line_number, full_match)
    """
    links = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                # Match {{< ref "filename#anchor?" >}} or {{< ref 'filename#anchor?' >}}
                matches = re.finditer(r'\{\{<\s*ref\s+[\'"](.*?)[\'"]\s*>\}\}', line)
                for match in matches:
                    referenced = match.group(1)
                    links.append((referenced, line_num, match.group(0)))
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return links


def find_post_file(filename: str, posts_dir: Path) -> Path | None:
    """Find a post file by its filename in the posts directory.

    Args:
        filename: The filename (YYYY-MM-DD-title) from the ref shortcode
        posts_dir: The posts directory to search in

    Returns:
        Path to the file if found, None otherwise
    """
    # Try direct filename match in posts directory and subdirectories
    for md_file in posts_dir.rglob("*.md"):
        if md_file.stem == filename:
            return md_file

    # Try with year/month subdirectory pattern (e.g., /2025/01/mindmaps-in-markdown/)
    # The filename itself contains the date, so we extract year and month
    match = re.match(r"(\d{4})-(\d{2})", filename)
    if match:
        year, month = match.groups()
        potential_path = posts_dir / year / month / f"{filename}.md"
        if potential_path.exists():
            return potential_path

    return None


def validate_heading_anchor(file_path: Path, anchor: str) -> bool:
    """Check if a heading anchor exists in a markdown file.

    Args:
        file_path: Path to the markdown file
        anchor: The anchor text (without the #)

    Returns:
        True if anchor exists, False otherwise
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # Match headings: # Heading, ## Heading, ### Heading, etc.
                # Hugo converts headings to lowercase with hyphens
                heading_match = re.match(r"^#+\s+(.+)$", line)
                if heading_match:
                    # Convert heading to slug format (lowercase, spaces to hyphens)
                    heading_text = heading_match.group(1).strip()
                    # Remove any extra markdown syntax like **bold** or *italic*
                    heading_text = re.sub(r"[*_]+", "", heading_text)
                    # Convert to slug
                    slug = (
                        re.sub(r"[^a-zA-Z0-9]+", "-", heading_text).strip("-").lower()
                    )

                    if slug == anchor:
                        return True
    except Exception as e:
        print(f"Error reading {file_path} for anchor validation: {e}", file=sys.stderr)

    return False


def check_broken_links(posts_dir: Path) -> Tuple[int, List[Path]]:
    """Check for broken internal links in all posts.

    Returns:
        Tuple of (number_of_broken_links, list_of_files_with_issues)
    """
    all_markdown_files = find_all_markdown_files(posts_dir)

    # Build a set of all post filenames (without .md extension)
    # for quick lookup
    all_posts = set()
    for f in all_markdown_files:
        if f.name != "_index.md":
            all_posts.add(f.stem)

    broken_links = []
    files_with_issues = set()

    for file_path in all_markdown_files:
        # Skip _index files
        if file_path.name == "_index.md":
            continue

        ref_links = extract_ref_links(file_path)

        for referenced, line_num, full_match in ref_links:
            # Skip references that start with / - these are taxonomy or special page references
            # which Hugo's ref shortcode handles internally and don't correspond to markdown files
            if referenced.startswith("/"):
                continue

            # Extract filename and optional anchor
            if "#" in referenced:
                filename, anchor = referenced.split("#", 1)
            else:
                filename = referenced
                anchor = None

            # Handle path fragments like "posts/2024-12-31-title"
            # Extract the actual filename from the path
            filename = Path(filename).name

            # Check if file exists
            target_file = find_post_file(filename, posts_dir)

            if not target_file:
                broken_links.append(
                    {
                        "source_file": file_path,
                        "line": line_num,
                        "reference": full_match,
                        "target": referenced,
                        "error": "File not found",
                    }
                )
                files_with_issues.add(file_path)
            elif anchor:
                # Check if anchor exists
                if not validate_heading_anchor(target_file, anchor):
                    broken_links.append(
                        {
                            "source_file": file_path,
                            "line": line_num,
                            "reference": full_match,
                            "target": referenced,
                            "error": f"Anchor '#{anchor}' not found in {target_file.name}",
                        }
                    )
                    files_with_issues.add(file_path)

    return len(broken_links), sorted(files_with_issues)


def main():
    if not POSTS_DIR.exists():
        print(f"Error: Posts directory not found at {POSTS_DIR}", file=sys.stderr)
        sys.exit(1)

    broken_count, files_with_issues = check_broken_links(POSTS_DIR)

    if broken_count == 0:
        print(f"✓ No broken internal links found")
        sys.exit(0)
    else:
        print(f"✗ Found {broken_count} broken internal link(s):", file=sys.stderr)
        print(file=sys.stderr)

        # Only check files that have issues
        for file_path in files_with_issues:
            ref_links = extract_ref_links(file_path)

            file_has_issues = False
            for referenced, line_num, full_match in ref_links:
                # Skip references that start with / - these are taxonomy or special page references
                if referenced.startswith("/"):
                    continue

                # Extract filename and optional anchor
                if "#" in referenced:
                    filename, anchor = referenced.split("#", 1)
                else:
                    filename = referenced
                    anchor = None

                # Handle path fragments like "posts/2024-12-31-title"
                filename = Path(filename).name

                # Check if file exists
                target_file = find_post_file(filename, POSTS_DIR)

                if not target_file:
                    print(f"{file_path}:{line_num}: {full_match}", file=sys.stderr)
                    print(f"  ✗ File not found: {referenced}", file=sys.stderr)
                    file_has_issues = True
                elif anchor:
                    # Check if anchor exists
                    if not validate_heading_anchor(target_file, anchor):
                        print(f"{file_path}:{line_num}: {full_match}", file=sys.stderr)
                        print(
                            f"  ✗ Anchor '#{anchor}' not found in {target_file.name}",
                            file=sys.stderr,
                        )
                        file_has_issues = True

            if file_has_issues:
                print(file=sys.stderr)

        print(
            f"\nTotal: {broken_count} broken link(s) in {len(files_with_issues)} file(s)",
            file=sys.stderr,
        )
        sys.exit(1)

    broken_count, files_with_issues = check_broken_links(POSTS_DIR)

    if broken_count == 0:
        print(f"✓ No broken internal links found")
        sys.exit(0)
    else:
        print(f"✗ Found {broken_count} broken internal link(s):", file=sys.stderr)
        print(file=sys.stderr)

        # Re-run to get detailed output
        all_markdown_files = find_all_markdown_files(POSTS_DIR)

        for file_path in all_markdown_files:
            if file_path.name == "_index.md":
                continue

            ref_links = extract_ref_links(file_path)

            file_has_issues = False
            for referenced, line_num, full_match in ref_links:
                if "#" in referenced:
                    filename, anchor = referenced.split("#", 1)
                else:
                    filename = referenced
                    anchor = None

                target_file = find_post_file(filename, POSTS_DIR)

                if not target_file:
                    print(f"{file_path}:{line_num}: {full_match}", file=sys.stderr)
                    print(f"  ✗ File not found: {referenced}", file=sys.stderr)
                    file_has_issues = True
                elif anchor and not validate_heading_anchor(target_file, anchor):
                    print(f"{file_path}:{line_num}: {full_match}", file=sys.stderr)
                    print(f"  ✗ Anchor '#{anchor}' not found", file=sys.stderr)
                    file_has_issues = True

            if file_has_issues:
                print(file=sys.stderr)

        print(
            f"\nTotal: {broken_count} broken link(s) in {len(files_with_issues)} file(s)",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
