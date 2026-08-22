---
title: "hugo: tag-based post connections"
date: 2026-08-22T13:29:06+02:00
tags:
  - bloggify
  - coding
  - dev
  - meta
---

[Previously]({{< ref "2026-08-22-llm-devise-a-plan" >}}).

**Problem statement**: post connections showed only direct links, while posts
with the same tags remained disconnected in the graph of this blog.

I added a second kind of edge. The pre-computation picks up to two posts with
the **most shared tags**, breaks ties by date, and excludes direct links:

```python {filename="ci/precompute_links.py"}
def compute_tag_related_posts(
    post: dict,
    all_posts: list[dict],
    outlinks_set: set[str],
    backlinks_set: set[str],
    limit: int = 2,
) -> list[str]:
    """Compute tag connections, excluding posts with direct links."""
    post_tags = set(post["tags"])
    if not post_tags:
        return []

    direct_ids = outlinks_set | backlinks_set
    scored = []
    for other in all_posts:
        other_id = other["id"]
        if other_id == post["id"] or other_id in direct_ids:
            continue

        shared_tags = post_tags & set(other["tags"])
        if shared_tags:
            scored.append((other_id, len(shared_tags), other["date"]))

    scored.sort(key=lambda item: (item[1], item[2], item[0]), reverse=True)
    return [item[0] for item in scored[:limit]]
```

Direct links remain directional, solid, and prominent. Shared-tag links are
symmetric, dashed, and muted:

```css {filename="layouts/partials/style.html"}
.mini-graph .mini-graph-direct-edge {
  fill: none;
  stroke: var(--link-color);
  stroke-width: 2.25;
  stroke-opacity: 0.9;
}

.mini-graph .mini-graph-tag-edge {
  fill: none;
  stroke: var(--color-gray);
  stroke-width: 1;
  stroke-dasharray: 4 4;
  stroke-opacity: 0.65;
}
```

The original [Anki post]({{< ref "2026-07-27-anki-archive-a-deck" >}}) now gets
one direct link and two tag connections:

```json
{
  "outlinks": ["2024-12-23-anki-workflow"],
  "tag_related": [
    "2026-04-15-anki-flashcards-with-claude-code",
    "2026-04-13-anki-api-access"
  ]
}
```

```shell
% python3 ci/test_precompute_links.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

There's a limit of 2 shared tag post edges for the sake of not visually
polluting the presentation.

I've been loving how this little blog is evolving into my beloved (public)
digital garden.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
