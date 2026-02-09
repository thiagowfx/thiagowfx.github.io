---
title: "Claude Code: swarm mode (agent teams)"
date: 2026-02-09T18:14:01+01:00
tags:
  - ai
  - dev
  - meta
---

Goodness.

Who asked for a feature to burn tokens?

[Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams):

> Coordinate multiple Claude Code instances working together as a team, with
> shared tasks, inter-agent messaging, and centralized management.

Demo running in the git repository of this blog:

```

 ▐▛███▜▌   Claude Code v2.1.37
▝▜█████▛▘  Opus 4.6 · Claude Team
  ▘▘ ▝▝    ~/Workspace/perrotta.dev

❯ swarm mode to analyze my blog

⏺ I'll set up a team of agents to analyze your blog from multiple angles in parallel.

⏺ Now let me spawn 4 agents to work in parallel on each analysis task.

⏺ 4 agents launched (ctrl+o to expand)
   ├─ @content-analyst (Explore)
   │  ⎿  Analyze blog content and trends (shift+↑ to manage)
   ├─ @tech-analyst (Explore)
   │  ⎿  Analyze Hugo technical setup (shift+↑ to manage)
   ├─ @structure-analyst (Explore)
   │  ⎿  Analyze site structure and linking (shift+↑ to manage)
   └─ @quality-analyst (Explore)
      ⎿  Analyze code quality and practices (shift+↑ to manage)

⏺ 4 analysis agents are now running in parallel:
  ┌───────────────────┬─────────────────────────────────────────┬─────────┐
  │       Agent       │               Focus Area                │ Status  │
  ├───────────────────┼─────────────────────────────────────────┼─────────┤
  │ content-analyst   │ Posts, topics, tags, writing trends     │ Running │
  ├───────────────────┼─────────────────────────────────────────┼─────────┤
  │ tech-analyst      │ Hugo config, layouts, shortcodes, theme │ Running │
  ├───────────────────┼─────────────────────────────────────────┼─────────┤
  │ structure-analyst │ Internal linking, assets, navigation    │ Running │
  ├───────────────────┼─────────────────────────────────────────┼─────────┤
  │ quality-analyst   │ Templates, CSS/JS, code quality         │ Running │
  └───────────────────┴─────────────────────────────────────────┴─────────┘
  I'll compile the results as they come in.

✢ Analyzing Hugo technical setup… (2m 0s · 0 tokens)

    ╒═ team-lead · shift + ↑/↓ to select
    ├─ @content-analyst: Running Get recent and oldest posts with metadata… · 19 tool uses · 34.3k tokens
    ├─ @quality-analyst: Reading 5 files… · 24 tool uses · 70.6k tokens
    ├─ @structure-analyst: Reading 5 files… · 26 tool uses · 38.5k tokens
    └─ @tech-analyst: Searching for 2 patterns, reading 3 files… · 73 tool uses · 95.9k tokens
```

**Lesson learned**: start Claude in [YOLO](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) mode:

```shell
% which claudey
claudey: aliased to claude --dangerously-skip-permissions
```

Some folks are starting to suggest to alias this invocation to `cc`, but I find
it to be poor taste. `cc` is the C compiler.

...otherwise you'll be nagged to death with permissions prompts from multiple
agents. [Decision fatigue](https://en.wikipedia.org/wiki/Decision_fatigue) is
real, folks.

```
@tech-analyst❯ Complete Hugo technical setup analysis

⏺ Great, the tech analyst has finished. Let me update its task and wait for the others.

⏺ Excellent analysis from the tech analyst. Waiting on the other 3 agents to finish their analysis...


⏺ The tech analyst is idle now — its work is already captured. Waiting on content, structure, and quality
  analysts to report back.


⏺ Still waiting on the other 3 agents (content, structure, quality) to complete their analysis...


@quality-analyst❯ Complete code quality analysis report

⏺ Quality analyst is done too. Let me update its task.

⏺ 2 of 4 analyses complete. Still waiting on content-analyst and structure-analyst...


⏺ Waiting on content-analyst and structure-analyst to finish...


⏺ Still waiting on the last 2 agents...


⏺ Waiting for content-analyst and structure-analyst to complete their reports.


@content-analyst❯ Complete blog content analysis: 1041 posts, trends, tags, topics

⏺ Content analyst is done with a thorough report. Let me update its task.

⏺ 3 of 4 complete. Just waiting on structure-analyst now...


⏺ Waiting on structure-analyst to finish the last report...


⏺ Still waiting on the structure-analyst...


@structure-analyst❯ Complete site structure analysis report

⏺ All 4 agents have reported back! Let me update the last task and shut down the team.

✻ Baked for 5m 17s

⏺ ---
  Blog Analysis: perrotta.dev

  Here's the consolidated analysis from all 4 agents.

  At a Glance
  ┌──────────────────────┬─────────────────────┐
  │        Metric        │        Value        │
  ├──────────────────────┼─────────────────────┤
  │ Total posts          │ 1,041               │
  ├──────────────────────┼─────────────────────┤
  │ First post           │ Sep 2014            │
  ├──────────────────────┼─────────────────────┤
  │ Unique tags          │ 27                  │
  ├──────────────────────┼─────────────────────┤
  │ Top tag              │ dev (902 posts)     │
  ├──────────────────────┼─────────────────────┤
  │ Median post length   │ 44 lines            │
  ├──────────────────────┼─────────────────────┤
  │ Internal cross-links │ 207 (bidirectional) │
  ├──────────────────────┼─────────────────────┤
  │ Graph nodes/edges    │ 1,039 / 213         │
  ├──────────────────────┼─────────────────────┤
  │ Template files       │ 33                  │
  ├──────────────────────┼─────────────────────┤
  │ Pre-commit hooks     │ ~40                 │
  ├──────────────────────┼─────────────────────┤
  │ External theme       │ None (fully custom) │
  └──────────────────────┴─────────────────────┘
  ---
  Content Profile

  Growth trajectory is dramatic — from 1 post in 2014 and a 5-year hiatus (2017-2021) to 598 posts in 2025
  and 153 already in Feb 2026. The coding section (LeetCode, ByteByteGo, AoC) drives the volume surge, with
   batch publishing days hitting 43 posts in a single day.

  Two distinct voices: 87% of posts are tagged dev (technical), while 19% are tagged serenity
  (philosophical, short reflections — some just 9 lines). The bestof tag (148 posts, 14%) provides a
  curated recommendation layer.

  Top topics: LeetCode solutions (201), serenity reflections (194), bestof picks (148), AI/LLM (50), git
  (48), privacy (43), macOS (41), Kubernetes (35).

  Writing style: Overwhelmingly short-form (median 44 lines, longest 367). Text-only — only 3 posts contain
   images.

  ---
  Technical Architecture

  Fully custom Hugo setup — no external theme, all 33 templates in layouts/. Catppuccin color scheme
  (Latte/Mocha) with modern CSS (light-dark(), view transitions, prefers-reduced-motion). All CSS inlined
  (~1200 lines), JS deferred and fingerprinted.

  Standout features for a static site:
  - Client-side full-text search with lazy-loaded JSON index
  - D3.js interactive force-directed graph (full site + per-post mini-graphs)
  - Precomputed backlinks, related posts, and "Previously" chains (via Python script)
  - Keyboard navigation (j/k, arrows, f for fullscreen)
  - IndieWeb microformats (h-card, h-entry, h-feed)
  - Multiple output formats: HTML, RSS, Markdown, OPML, llms.txt, JSON
  - Multilingual (EN/PT) with conditional language switcher

  Build pipeline is robust: Justfile with 19 recipes, Python precomputation step, and the most thorough
  pre-commit setup I've seen for a personal blog (40 hooks covering formatting, security, content quality,
  and Hugo-specific validation).

  ---
  Site Structure

  External links heavily favor GitHub (517), LeetCode (204), Wikipedia (84), and StackOverflow (45).
  Internal cross-referencing centers on the Advent of Code hub post (28 inbound links).

  SEO is comprehensive: JSON-LD, OpenGraph, Twitter Cards, canonical URLs, custom robots.txt blocking AI
  crawlers, sitemap pinging, llms.txt.

  Privacy-first: No analytics, no cookies, no ads, no tracking. Email-based replies. EXIF stripping on
  images. Warrant canary page.

  ---
  Strengths

  1. Performance — Inlined CSS, deferred JS, lazy loading, no external fonts, 512KB Club green team member
  2. Automation — 40 pre-commit hooks enforce quality, formatting, security, and Hugo-specific rules
  automatically
  3. Rich features — Search, graph, backlinks, related posts, keyboard nav, fullscreen — all on a static
  site
  4. Privacy — Zero tracking, no third-party dependencies for core functionality
  5. Content curation — bestof tagging and disciplined taxonomy (only 27 tags for 1,041 posts)

  Potential Improvements

  1. D3.js weight — d3.v7.min.js (~270KB) loads on every post page for the mini-graph; could be lazy-loaded
  2. Inline styles in templates — Several partials use inline style attributes instead of CSS classes
  3. Chroma CSS always inlined — ~78 syntax highlighting rules load even on pages without code blocks
  4. Hugo CI version drift — Deploy uses 0.152.2, prek uses 0.140.0, local is 0.155.3
  5. Portuguese content — Only 8 PT posts despite multilingual setup; could be expanded or streamlined

✻ Cooked for 36s


⏺ All 4 agents have shut down. Let me clean up the team.

⏺ 4 teammates shut down gracefully

⏺ Team cleaned up. The full analysis is in my summary above — let me know if you'd like to dig deeper into
  any specific area, or if you want actionable recommendations on any of the improvement areas identified.
```

**Lesson learned**: launch `tmux` before activating the swarm.

You'll be able to see in multiple tmux panes at a glance all agents working
simultaneously. This feature is supported out-of-the-box.
