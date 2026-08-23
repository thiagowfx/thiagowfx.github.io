import json
import os
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from precompute_links import (
    compute_previously,
    compute_related_posts,
    compute_tag_related_posts,
    extract_refs,
    main,
    parse_frontmatter,
)


def post(post_id: str, tags: list[str], date: str) -> dict:
    return {
        "id": post_id,
        "tags": tags,
        "date": datetime.fromisoformat(date),
    }


class ComputeTagRelatedPostsTest(unittest.TestCase):
    def test_ranks_shared_tag_count_then_date_and_excludes_direct_links(self):
        current = post("current", ["anki", "dev", "pkm"], "2026-07-27")
        posts = [
            current,
            post("outlink", ["anki", "dev", "pkm"], "2026-07-26"),
            post("backlink", ["anki", "dev", "pkm"], "2026-07-25"),
            post("three-tags", ["anki", "dev", "pkm"], "2026-04-15"),
            post("two-tags-newer", ["anki", "pkm"], "2026-07-20"),
            post("two-tags-older", ["anki", "dev"], "2026-01-01"),
            post("unrelated", ["linux"], "2026-07-28"),
        ]

        result = compute_tag_related_posts(
            current, posts, {"outlink"}, {"backlink", "outlink"}
        )

        self.assertEqual(result, ["three-tags", "two-tags-newer"])

    def test_returns_available_matches_up_to_limit(self):
        current = post("current", ["anki"], "2026-07-27")
        posts = [current, post("match", ["anki"], "2026-01-01")]

        self.assertEqual(compute_tag_related_posts(current, posts, set(), set()), ["match"])
        self.assertEqual(
            compute_tag_related_posts(
                post("untagged", [], "2026-07-27"), posts, set(), set()
            ),
            [],
        )

    def test_parses_frontmatter_refs_and_other_relationships(self):
        content = """---
title: "Current Post"
date: 2026-07-27
tags:
  - anki
categories: [dev]
---
{{< ref "posts/older#section" >}}
"""
        self.assertEqual(
            parse_frontmatter(content),
            {
                "title": "Current Post",
                "date": "2026-07-27",
                "tags": ["anki"],
                "categories": ["dev"],
            },
        )
        self.assertEqual(extract_refs(content), ["older"])

        current = {
            **post("current", ["anki"], "2026-07-27"),
            "title": "Anki workflow",
            "categories": ["dev"],
        }
        older = {
            **post("older", ["anki"], "2026-01-01"),
            "title": "Anki notes",
            "categories": ["dev"],
        }
        self.assertEqual(compute_related_posts(current, [current, older], set(), set()), ["older"])
        self.assertEqual(compute_previously(current, [current, older]), ["older"])

    def test_main_writes_backlinks_outlinks_and_graph(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            posts = root / "content" / "posts"
            posts.mkdir(parents=True)
            (posts / "2026-01-01-first.md").write_text(
                "---\ntitle: First\ndate: 2026-01-01\ntags: [dev]\n---\n",
                encoding="utf-8",
            )
            (posts / "2026-01-02-second.md").write_text(
                "---\ntitle: Second\ndate: 2026-01-02\ntags: [dev]\n---\n"
                '{{< ref "2026-01-01-first" >}}\n',
                encoding="utf-8",
            )

            previous = Path.cwd()
            try:
                os.chdir(root)
                main()
            finally:
                os.chdir(previous)

            output = json.loads((root / "data" / "links.json").read_text(encoding="utf-8"))
            self.assertEqual(
                output["posts"]["2026-01-01-first"]["backlinks"],
                ["2026-01-02-second"],
            )
            self.assertEqual(
                output["posts"]["2026-01-02-second"]["outlinks"],
                ["2026-01-01-first"],
            )
            self.assertEqual(
                output["graph"]["edges"],
                [
                    {
                        "source": "2026-01-02-second",
                        "target": "2026-01-01-first",
                    }
                ],
            )


if __name__ == "__main__":
    unittest.main()
