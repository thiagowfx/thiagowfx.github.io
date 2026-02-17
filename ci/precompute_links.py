#!/usr/bin/env python3
"""Pre-compute post relationships for Hugo templates.

This script scans all blog posts and computes:
- backlinks: posts that link to each post via ref shortcodes
- related: top 2 related posts by title words, tags, categories, and links
- previously: older posts with shared tags (jwz-style)
- graph: nodes and edges for the graph visualization

Output is written to data/links.json for Hugo to consume via $.Site.Data.links
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

POSTS_DIR = Path("content/posts")
OUTPUT_FILE = Path("data/links.json")

# Regex to match Hugo ref shortcodes: {{< ref "filename" >}} or {{< ref 'filename' >}}
REF_PATTERN = re.compile(r'\{\{<\s*ref\s+[\'"]([^\'"#]+)(?:#[^\'"]+)?[\'"]\s*>\}\}')


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}

    # Find the closing ---
    end = content.find("---", 3)
    if end == -1:
        return {}

    frontmatter = content[3:end].strip()
    result = {}

    for line in frontmatter.split("\n"):
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()

        # Handle YAML lists (simple case)
        if key in ("tags", "categories"):
            if value.startswith("[") and value.endswith("]"):
                # Inline list: [tag1, tag2]
                result[key] = [
                    t.strip().strip("\"'") for t in value[1:-1].split(",") if t.strip()
                ]
            elif not value:
                # Multi-line list follows
                result[key] = []
            else:
                result[key] = [value.strip("\"'")]
        elif key == "title":
            result[key] = value.strip("\"'")
        elif key == "date":
            # Parse ISO date format
            result[key] = value.strip("\"'")

    # Handle multi-line tags/categories
    in_list = None
    for line in frontmatter.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- ") and in_list:
            result[in_list].append(stripped[2:].strip("\"'"))
        elif stripped in ("tags:", "categories:"):
            in_list = stripped[:-1]
            if in_list not in result:
                result[in_list] = []
        elif ":" in stripped and not stripped.startswith("-"):
            in_list = None

    return result


def extract_refs(content: str) -> list[str]:
    """Extract referenced post filenames from ref shortcodes."""
    refs = []
    for match in REF_PATTERN.finditer(content):
        ref = match.group(1)
        # Extract just the filename if it's a path
        filename = Path(ref).name
        refs.append(filename)
    return refs


def parse_post(file_path: Path) -> dict | None:
    """Parse a markdown post file and extract metadata."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

    frontmatter = parse_frontmatter(content)
    if not frontmatter.get("title"):
        return None

    # Get filename without extension as ID
    # For page bundles (index.md), use parent directory name to avoid ID collisions
    if file_path.name == "index.md":
        post_id = file_path.parent.name
    else:
        post_id = file_path.stem

    # Parse date (normalize to naive datetime for comparison)
    date_str = frontmatter.get("date", "")
    try:
        # Handle various date formats
        if "T" in date_str:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            # Convert to naive datetime
            date = date.replace(tzinfo=None)
        elif date_str:
            date = datetime.strptime(date_str[:10], "%Y-%m-%d")
        else:
            # Extract date from filename (YYYY-MM-DD-title)
            match = re.match(r"(\d{4}-\d{2}-\d{2})", post_id)
            if match:
                date = datetime.strptime(match.group(1), "%Y-%m-%d")
            else:
                date = datetime.min
    except ValueError:
        date = datetime.min

    # Compute Hugo page path (relative to content/)
    # For content/posts/coding/2024-01-01-foo.md -> /posts/coding/2024-01-01-foo
    # For content/posts/2024-01-01-foo/index.md -> /posts/2024-01-01-foo
    rel_path = file_path.relative_to(Path("content"))
    if rel_path.name == "index.md":
        # Page bundle: use parent directory
        hugo_path = "/" + str(rel_path.parent)
    else:
        # Regular file: remove .md extension
        hugo_path = "/" + str(rel_path.with_suffix(""))

    return {
        "id": post_id,
        "hugo_path": hugo_path,
        "title": frontmatter.get("title", ""),
        "date": date,
        "date_str": date.strftime("%Y-%m-%d") if date != datetime.min else "",
        "tags": frontmatter.get("tags", []),
        "categories": frontmatter.get("categories", []),
        "outlinks": extract_refs(content),
        "path": str(file_path),
    }


def extract_title_words(title: str, min_length: int = 4) -> set[str]:
    """Extract significant words from a title."""
    words = set()
    for word in title.lower().split():
        # Remove non-alphanumeric characters
        clean = re.sub(r"[^a-z0-9]+", "", word)
        if len(clean) >= min_length:
            words.add(clean)
    return words


def compute_related_posts(
    post: dict, all_posts: list[dict], outlinks_set: set[str], backlinks_set: set[str]
) -> list[str]:
    """Compute top 2 related posts by scoring."""
    title_words = extract_title_words(post["title"])
    post_tags = set(post["tags"])
    post_categories = set(post["categories"])

    scored = []
    for other in all_posts:
        if other["id"] == post["id"]:
            continue

        score = 0

        # Title word overlap
        other_title_words = extract_title_words(other["title"])
        for word in title_words:
            if word in other["title"].lower():
                score += 1

        # Shared tags (+1 each)
        shared_tags = post_tags & set(other["tags"])
        score += len(shared_tags)

        # Shared categories (+2 each)
        shared_categories = post_categories & set(other["categories"])
        score += len(shared_categories) * 2

        # Bidirectional links (+5)
        other_id = other["id"]
        if other_id in outlinks_set or other_id in backlinks_set:
            score += 5

        if score > 0:
            # Use score * 10^12 + timestamp for sorting (higher score wins, then newer)
            sort_key = score * 10**12 + int(other["date"].timestamp())
            scored.append((other["id"], score, sort_key))

    # Sort by sort_key descending and take top 2
    scored.sort(key=lambda x: x[2], reverse=True)
    return [s[0] for s in scored[:2]]


def compute_previously(post: dict, all_posts: list[dict], limit: int = 5) -> list[str]:
    """Compute previously links (older posts with shared tags)."""
    if not post["tags"]:
        return []

    post_tags = set(post["tags"])
    post_date = post["date"]

    scored = []
    for other in all_posts:
        if other["id"] == post["id"]:
            continue
        if other["date"] >= post_date:
            continue  # Must be older

        shared_tags = post_tags & set(other["tags"])
        score = len(shared_tags)

        if score > 0:
            scored.append((other["id"], score, other["date"]))

    # Sort by score desc, then by date desc (most recent first among same score)
    scored.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return [s[0] for s in scored[:limit]]


def main():
    if not POSTS_DIR.exists():
        print(f"Error: Posts directory not found at {POSTS_DIR}", file=sys.stderr)
        sys.exit(1)

    # Parse all posts
    print("Parsing posts...", file=sys.stderr)
    posts = []
    for md_file in POSTS_DIR.rglob("*.md"):
        if md_file.name == "_index.md":
            continue
        post = parse_post(md_file)
        if post:
            posts.append(post)

    print(f"Found {len(posts)} posts", file=sys.stderr)

    # Build outlinks index: post_id -> set of linked post_ids
    outlinks_index = {}
    for post in posts:
        outlinks_index[post["id"]] = set(post["outlinks"])

    # Build backlinks index: post_id -> set of posts that link to it
    print("Computing backlinks...", file=sys.stderr)
    backlinks_index = defaultdict(set)
    for post in posts:
        for linked_id in post["outlinks"]:
            backlinks_index[linked_id].add(post["id"])

    # Sort posts by date for related/previously calculations
    posts_by_date = sorted(posts, key=lambda p: p["date"], reverse=True)

    # Pre-compute valid post IDs for filtering outlinks
    valid_post_ids = {p["id"] for p in posts}

    # Build date lookup for sorting
    date_by_id = {p["id"]: p["date"] for p in posts}

    # Compute relationships for each post
    print("Computing relationships...", file=sys.stderr)
    links_data = {}
    for post in posts:
        post_id = post["id"]
        backlinks = backlinks_index.get(post_id, set())

        # Sort backlinks by date (newest first)
        backlinks_with_date = [
            (bid, next((p["date"] for p in posts if p["id"] == bid), datetime.min))
            for bid in backlinks
        ]
        backlinks_with_date.sort(key=lambda x: x[1], reverse=True)
        sorted_backlinks = [b[0] for b in backlinks_with_date]

        related = compute_related_posts(
            post, posts_by_date, outlinks_index.get(post_id, set()), backlinks
        )

        previously = compute_previously(post, posts_by_date)

        # Sort outlinks by date (newest first), filtered to valid posts
        valid_outlinks = [oid for oid in outlinks_index.get(post_id, set()) if oid in valid_post_ids]
        valid_outlinks.sort(key=lambda oid: date_by_id.get(oid, datetime.min), reverse=True)

        links_data[post_id] = {
            "hugo_path": post["hugo_path"],
            "backlinks": sorted_backlinks,
            "outlinks": valid_outlinks,
            "related": related,
            "previously": previously,
        }

    # Build graph data (nodes and edges)
    print("Building graph data...", file=sys.stderr)
    nodes = []
    edges = []

    for post in posts:
        nodes.append(
            {
                "id": post["id"],
                "hugo_path": post["hugo_path"],
                "title": post["title"],
                "date": post["date_str"],
            }
        )

    for post in posts:
        for target_id in post["outlinks"]:
            # Only add edge if target exists
            if any(p["id"] == target_id for p in posts):
                edges.append({"source": post["id"], "target": target_id})

    # Build ID -> hugo_path lookup table
    path_lookup = {post["id"]: post["hugo_path"] for post in posts}

    # Combine all data
    output = {
        "posts": links_data,
        "paths": path_lookup,
        "graph": {
            "nodes": nodes,
            "edges": edges,
        },
    }

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, separators=(",", ":"))

    print(f"Written {OUTPUT_FILE}", file=sys.stderr)
    print(f"  {len(posts)} posts", file=sys.stderr)
    print(f"  {len(edges)} edges", file=sys.stderr)


if __name__ == "__main__":
    main()
