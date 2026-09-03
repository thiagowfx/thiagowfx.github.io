---
title: "claude code: /goal"
date: 2026-08-26T17:45:34+02:00
tags:
  - ai
  - argocd
  - bloggify
  - claude
  - dev
  - kubernetes
---

**Problem statement**: a coding agent stops when it thinks it is done, not when
the thing is actually done.

[`/goal`](https://code.claude.com/docs/en/goal.md) sets a condition that
outlives the turn. The docs call it a wrapper around a session-scoped,
prompt-based Stop hook: every time the agent tries to end its turn, an evaluator
checks the condition and pushes back if it does not hold.

```text
/goal argocd, prometheus and external secrets should all be healthy and synced in cluster #26
```

I set that mid-session while debugging a cluster where three Argo CD apps were
stuck. What followed was the useful part. The agent wrapped up with a tidy
summary and two pull requests, and got this back:

```text
Stop hook feedback:
[argocd, prometheus and external secrets should all be healthy and synced in cluster #26]:
PRs #3064 and #3062 have been opened but not yet merged. The latest status check
in the transcript confirms external-secrets = 'OutOfSync', argocd = 'OutOfSync',
prometheus = 'Unknown' — none are both 'healthy and synced'.
```

Opening a PR is not the same as the apps being green, and the evaluator reads
the transcript rather than the closing paragraph. It fired three times. Each
time the summary was plausible and each time the condition was still false.

`/goal` with no arguments shows the condition, elapsed time, turn count, token
spend, and the evaluator's last reason. `/goal clear` ends it.

The failure mode it fixes is specific: an agent that declares victory one step
early. It does not make the agent smarter — mine still burned several turns on
wrong theories, and I had to redirect it more than once. It only refuses to let
"I opened a PR" stand in for "the apps are green".
