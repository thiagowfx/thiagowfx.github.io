---
title: "JIRA: backfill tickets from merged pull requests"
date: 2026-09-29T11:21:17+02:00
tags:
  - bloggify
  - dev
  - git
---

**Problem statement**: how can I catch up JIRA when pull requests have already
(been) merged without tickets?

I wrote a local `/backfill-jira` skill for my AI harnesses. It compares recent
merged PRs with existing issues before it creates anything. This is its
structure; internal projects, repositories, queries, and field IDs are omitted:

```shell
% rg -n '^### Phase' ~/.claude/skills/backfill-jira/SKILL.md
31:### Phase A — gather + reconcile (read-only)
72:### Phase B — create the backfill tickets
125:### Phase C — confirm
```

The unit of work is a *theme*, not a PR. Several PRs can implement one change;
one PR can also be routine enough to need no ticket. The skill checks PR
references and matching issue summaries before declaring a gap. Existing
backlog issues count as coverage.

The report rule in the skill is explicit:

```text
4. **Report.** Print a table of every PR → (existing ticket | NEW theme-N | skipped-routine) and a
   separate list of the gap themes to create. The counts must reconcile: covered + new + skipped =
   total PRs. Don't let "get every PR to a theme" pressure you into merging unrelated skipped PRs
   into a theme just to shrink the skipped list.
```

Phase B creates one ticket for each uncovered theme, marks work as complete,
and reads the status back. It also checks the sprint assignment after writing
it. Neither a successful create response nor an attempted status change is
proof that the final fields stuck.

The skill deliberately leaves routine work alone:

```text
- Don't create per-PR tickets by default — one ticket per theme keeps signal high. **Never create a
  "grab bag" / "catch-all" / "hygiene" ticket that lumps together unrelated PRs** just to get to
  zero gaps — each ticket must describe one coherent, describable piece of work. If a PR is
  genuinely routine and not worth tracking on its own (a version bump, a dependency bump, a typo
  fix) and doesn't fit an existing theme, leave it **uncovered**: list it in the report as *skipped
  (routine, no ticket)* rather than inventing a ticket to absorb it.
```

A second pass over the same window checks whether the new tickets now cover
the gaps. Zero new gaps matters more than zero skipped PRs.
