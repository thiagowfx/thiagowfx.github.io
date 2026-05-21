---
title: "prove_it: verification hooks for Claude Code"
date: 2026-05-21T19:10:09+02:00
tags:
  - ai
  - dev
---

**Problem statement**: [Claude Code](https://claude.com/claude-code) likes to
declare "done" without running tests. _Said no overconfident LLM ever_.

[`prove_it`](https://github.com/searlsco/prove_it) by [Justin
Searls](https://justin.searls.co/) is a config-driven hook framework that
intercepts Claude's lifecycle events (`SessionStart`, `PreToolUse`, `Stop`) and
runs whatever tasks you configure — tests, linters, AI reviewers — blocking
the `Stop` until they pass.

I like this concept in spirit.

Installation:

```shell
% brew install searlsco/tap/prove_it
% prove_it install                    # one-time, registers global hooks at ~/.claude/
% cd <git repo> && prove_it init      # per-repo config + script stubs + git hooks; comparable to `pre-commit install`
% prove_it doctor                     # comparable to `brew doctor`
```

I (finally!) tried it today and concluded that it's not for me.

That said, I really like the ideas that Justin developed there. I'll look into
adopting some of them into my global [CLAUDE.md]({{< ref "2026-05-20-personal-claude-md" >}}).

See the [`README.md`](https://github.com/searlsco/prove_it) for documentation.
