---
title: "claude --resume"
date: 2025-09-02T14:12:07+02:00
tags:
  - dev
---

**Problem statement**: when working with [`Claude
Code`](https://www.anthropic.com/claude-code), how to resume a session after
terminating the `claude` process?

Of course we could simply prompt the LLM agent again, but that is both (i) slow
and (ii) expensive. And I do not want to get into the intricacies of [prompt
caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching).

The ability to [resume old
sessions](https://github.com/anthropics/claude-code/issues/371) was recently
added. The tool has great defaults: by default, you see only sessions pertaining
to the directory you're working on.

For example, when I run it in my blog directory:

```
% claude --resume
     Modified    Created     # Messages Git Branch     Summary
❯ 1. 1 week ago  1 week ago         148 master         I would like to create a second RSS feed, for...…
  2. 1 week ago  1 week ago         113 master         Ensure images respect the page width and do n...…
  3. 1 week ago  1 week ago          31 master         Update XSLT. By: should be properly linkified…
  4. 1 week ago  1 week ago          12 master         Add space after By: and Published: in the XSL...…
  5. 1 week ago  1 week ago          20 master         Hugo XML Link Syntax Troubleshooting…
  6. 1 week ago  1 week ago         119 rss            Create a XSLT for my RSS feed (this is a hugo...…
  7. 1 week ago  1 week ago          42 rss            Hugo RSS XSLT Theme Styling and Design Match…
```

When I run it from another directory:

```
% claude --resume
     Modified    Created     # Messages Git Branch     Summary
❯ 1. 4m ago      8m ago              14 thiagowfx/miss Print out the dates in YYYY-MM-DD form in the...…
  2. 5m ago      12m ago             78 thiagowfx/miss Angular Date Filter Component Implementation…
  3. 14m ago     22m ago             78 thiagowfx/miss Do not allow whitespace in instance names in ...…
  4. 22m ago     46m ago            191 thiagowfx/miss Whitespace Trim Testing: Comprehensive React Unit Suite…
```
