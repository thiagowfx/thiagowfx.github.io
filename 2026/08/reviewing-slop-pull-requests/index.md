---
title: "Reviewing slop pull requests"
url: https://perrotta.dev/2026/08/reviewing-slop-pull-requests/
last_updated: 2026-08-18
---


**Problem statement**: review an AI-written ~~slop~~ pull request from a
teammate.

We'll use a [clanker](https://lucumr.pocoo.org/2026/5/26/clankers/) to review slop
PRs.

**First**, I invoke the
[`/meat`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/meat/SKILL.md)
skill, turning the diff into a reading guide, inspired by [David Crawshaw](https://meat.dev/):

```text
/meat <PR-URL>
```

It does not look for defects. It captures the diff once, follows control and
data flow, treats tests as specifications, and returns this shape:

```markdown
One sentence with intent and observable result.

## Read in this order
- path:line — why this contract matters

## Flow
1. input
2. transformation
3. effect

## Contracts
## Tests as specs
## Omitted
```

That gives me the author's system model (the "meat" of their PR) without the PR
body's narrative.

**Second**, [`/dual-review`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/dual-review/SKILL.md)[^2]
tries to break that model:

[^2]: Inspired by an internal skill created by our CISO.

```text
/dual-review <PR-URL> [--post]
```

It runs _two_ review passes with different lenses / perspectives, then validates
every candidate against source and focused probes. Reviewer agreement changes
investigation priority.

To recap:

- `/meat` says what the change means and where to read it.
- `/dual-review` checks whether contracts survive hostile input.

My default sequence for a long, plausible PR is now:

```text
/meat <PR-URL>
/dual-review <PR-URL> --post
```

One tool removes narrative noise.
The other removes findings without evidence.

