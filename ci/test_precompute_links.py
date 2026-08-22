import unittest
from datetime import datetime

from precompute_links import compute_tag_related_posts


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
            compute_tag_related_posts(post("untagged", [], "2026-07-27"), posts, set(), set()),
            [],
        )


if __name__ == "__main__":
    unittest.main()
