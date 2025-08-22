---
title: "/security-review"
date: 2025-08-22T15:31:01+02:00
tags:
  - dev
---

Anthropic, [Automated Security Reviews in Claude Code
](https://support.anthropic.com/en/articles/11932705-automated-security-reviews-in-claude-code):

> Claude Code now includes automated security review features to help you
> identify and fix vulnerabilities in your code. This guide explains how to use
> the `/security-review` command and GitHub Actions to improve your code security.

Of course, there are also
[docs](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command).

It is merely a [glorified system
prompt](https://github.com/anthropics/claude-code-security-review/blob/main/.claude/commands/security-review.md?plain=1),
which is exactly what I expected:

> Complete a security review of the pending changes on the current branch
>
> You are a senior security engineer conducting a focused security review of the changes on this branch.
>
> [...]

The prompt employs the well-established pattern of outlining countless examples
and instructing the model to follow a certain output format.

In 2025, the Gen AI arms race is mostly about (i) cost-benefit and (ii) user /
developer experience. Anthropic surely has a good taste in user experience; to
me, they often resemble Apple.
