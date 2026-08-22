---
title: "LLM: Devise a plan"
date: 2026-08-22T13:07:58+02:00
tags:
  - ai
  - dev
---

There's no need for
[plan](https://opencode.ai/docs/#:~:text=OpenCode%20has%20a%20Plan%20mode%20that%20disables%20its%20ability%20to%20make%20changes%20and%20instead%20suggest%20how%20it%E2%80%99ll%20implement%20the%20feature.)
[mode](https://code.claude.com/docs/en/common-workflows#plan-before-editing).

[Sandboxing]({{< ref "2026-02-26-cco-claude-condom-sandbox" >}}) + prompt
engineering is enough.

End your prompt with

> Devise a plan

...and let the 2026 Gen AI models flow by themselves.

Here'a a sample session:

**User**:

```
some of my blog posts e.g. https://perrotta.dev/2026/07/anki-archive-a-deck/ have
"connections"

this is great, but it includes _only_ direct links

I wanted to expand connections to include a couple of posts that share tags too

They should be visually distinct from direct links (direct links should stand out better)

*Devise a plan*
```

**Assistant**:

```
[...]

Current Connections graph reads only backlinks and outlinks. Existing related
data mixes links, tags, categories, and title words. It cannot guarantee two
tag-based results.

 Plan:

 1. Precompute tag connections
     - Add tag_related to ci/precompute_links.py.
     - Select up to two posts with shared tags.
     - Exclude current post, backlinks, and outlinks.
     - Rank by shared-tag count, then newest date.
     - Store post IDs in data/links.json.

 2. Extend mini graph
     - Read tag_related in layouts/partials/mini-graph.html.
     - Keep incoming links on left.
     - Keep outgoing links on right.
     - Place tag connections below current post.
     - Use no arrows because tag relationships have no direction.
     - Include shared tag names in each SVG <title>.

[...]

 6. Verify
     - Add focused tests for ranking, direct-link exclusion, deduplication, and
       fewer-than-two matches.
     - Regenerate data/links.json.
     - Run hugo.
     - Inspect /2026/07/anki-archive-a-deck/ on desktop and mobile.
     - Confirm direct Anki workflow link stands out.
     - Confirm two non-direct Anki/tag posts appear as muted tag connections.
     - Confirm posts without tags or direct links still render correctly.
```
