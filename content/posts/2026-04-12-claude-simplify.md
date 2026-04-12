---
title: "claude: /simplify"
date: 2026-04-12T10:18:17+02:00
tags:
  - ai
  - dev
---

My all-time favorite bundled skill _for code reviewing_ in Claude Code:
`/simplify`.

As per the official docs:

```
/simplify   Review changed code for reuse, quality, and efficiency, then fix any issues found. (bundled)
```

A sample run:

```
  Running 3 agents… (ctrl+o to expand)
   ├─ Code reuse review · 38 tool uses · 42.1k tokens
   │  ⎿  Read: modules/remote-access-ips/main.tf
   ├─ Code quality review · 17 tool uses · 29.8k tokens
   │  ⎿  Searching for 7 patterns, reading 10 files…
   └─ Efficiency review · 0 tool uses
      ⎿  Done
     (ctrl+b to run in background)
```

It is effective, not very opinionated (which is good in this context!), and
non-intrusive.

And it surely burns a good share of tokens.

I'm interested in exploring ways to automate this skill invocation as part of
every PR.
