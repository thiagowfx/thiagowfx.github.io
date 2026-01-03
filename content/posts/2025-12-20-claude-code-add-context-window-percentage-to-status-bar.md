---
title: "Claude Code: add context window % to status line"
date: 2025-12-20T15:42:11-03:00
tags:
  - ai
  - dev
---

> Claude code now officially supports showing context window information like
> percentage of usage in status line ([via Ashik Nesin](https://aiengineerguide.com/blog/show-context-window-information-in-claude-code-statusline/)):

```
> /statusline Add a progress bar showing the percentage of context currently used

⏺ statusline-setup(Configure statusline progress bar)
  ⎿  Done (3 tool uses · 7.4k tokens · 44s)

⏺ I've configured your statusline to include a context usage progress bar. Your status line will now show something like:

  .claude (git:main) [Claude 3.5 Sonnet] [██████░░░░ 60%]

  The progress bar displays:
  - Filled blocks (█) for used context
  - Empty blocks (░) for remaining context
  - Percentage showing exact usage

  The context calculation includes input tokens, cache creation tokens, and cache read tokens relative to the total context window size.
```

My updated
[`.claude/statusline.sh`](https://github.com/thiagowfx/.dotfiles/blob/8ab831db16c8e042f024081744e723c5abf790c7/claude/.claude/statusline.sh).

[The
diff](https://github.com/thiagowfx/.dotfiles/commit/8ab831db16c8e042f024081744e723c5abf790c7).
