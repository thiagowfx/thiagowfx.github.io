---
title: "when Gen AI cites docs that don't exist"
date: 2026-07-16T12:34:22+02:00
tags:
  - ai
  - dev
  - kubernetes
---

**Today in AGI**: two Claude agents, same annotation, opposite answers.

I had a PR touching an ArgoCD `PostSync` hook. Ordering hooks within a phase
needs an annotation, so I asked; Claude Code (Opus 4.8) and Claude in GitHub
disagreed:

- Claude Code: `argocd.argoproj.io/hook-weight` does **not** exist.
- Claude in GitHub: it **does** exist.

Both stated it flatly. So I pushed the GitHub agent, and it doubled down —
citing documentation(!):

> This claim is incorrect. `argocd.argoproj.io/hook-weight` is a documented
> ArgoCD annotation for controlling hook execution order within a phase. From
> the ArgoCD resource hooks documentation:

Citing non-existent docs is the clanker equivalent of pulling rank.

Confident. Sourced. Wrong. The actual annotation for ordering is
[`argocd.argoproj.io/sync-wave`](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/):

> They are defined by the `argocd.argoproj.io/sync-wave` annotation. The value
> is an integer that defines the ordering.

```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "5"
```

There is no `hook-weight`. The "documentation" it quoted from doesn't say what
it says it says.

Eventually it folded:

> You are correct, and I apologize for the confident but incorrect claim in
> round 3.

Round 3. It took three rounds and a fabricated citation before the model
conceded. The failure mode isn't the hallucination — it's the escalation to
`"""docs"""` as authority to defend it.

Same model family, same question, one right and one wrong. Verify against the
upstream source, not against the more confident agent.

Human-in-the-loop is still very much needed, folks.

- - -

🤖 *Drafted with `/bloggify`.*
