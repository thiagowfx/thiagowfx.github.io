---
title: "claude: ccusage"
date: 2025-09-04T14:55:15+02:00
tags:
  - ai
  - dev
---

[`ccusage`](https://github.com/ryoppippi/ccusage) via [Simon
Willison](https://simonwillison.net/2025/Jul/14/ccusage/):

> Claude Code logs detailed usage information to the `~/.claude/` directory.
> `ccusage` is a neat little Node.js tool which reads that information and shows
> you a readable summary of your usage patterns, including the estimated cost in
> USD per day.

> A CLI tool for analyzing Claude Code usage from local JSONL files.

**Usage**:

```
% npx ccusage@latest
Need to install the following packages:
ccusage@16.2.3
Ok to proceed? (y)

 WARN  Fetching latest model pricing from LiteLLM...

ℹ Loaded pricing for 1544 models

 ╭──────────────────────────────────────────╮
 │                                          │
 │  Claude Code Token Usage Report - Daily  │
 │                                          │
 ╰──────────────────────────────────────────╯

┌────────────┬───────────────┬───────────┬───────────┬───────────────┬─────────────┬───────────────┬─────────────┐
│ Date       │ Models        │     Input │    Output │  Cache Create │  Cache Read │  Total Tokens │  Cost (USD) │
├────────────┼───────────────┼───────────┼───────────┼───────────────┼─────────────┼───────────────┼─────────────┤
│ 2025-08-05 │ - sonnet-4    │       896 │    30,430 │       303,782 │   7,232,685 │     7,567,793 │       $3.77 │
├────────────┼───────────────┼───────────┼───────────┼───────────────┼─────────────┼───────────────┼─────────────┤
│ 2025-08-11 │ - sonnet-4    │        58 │     5,870 │        83,682 │   1,024,297 │     1,113,907 │       $0.71 │
├────────────┼───────────────┼───────────┼───────────┼───────────────┼─────────────┼───────────────┼─────────────┤
│ 2025-08-12 │ - sonnet-4    │        42 │     6,758 │       116,661 │     777,241 │       900,702 │       $0.77 │
[...]
```

Neat!
