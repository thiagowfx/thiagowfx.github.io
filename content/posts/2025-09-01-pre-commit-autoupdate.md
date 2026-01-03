---
title: "pre-commit: autoupdate"
date: 2025-09-01T12:05:52+02:00
tags:
  - dev
  - pre-commit
---

When using [`pre-commit`](https://pre-commit.com/), you can take advantage of
its built-in `pre-commit autoupdate` command to keep your hook dependencies
up-to-date.

There's one major drawback of adopting it ubiquitously: it is virtually
[impossible](https://stackoverflow.com/questions/74232399/is-it-possible-that-pre-commit-autoupdate-skips-a-single-linter)
to instruct it to skip certain repositories.

It wouldn't be hard to update it to ignore hook dependencies with skip byline
comments, but its author [isn't
keen](https://stackoverflow.com/a/74240674/1745064) on implementing support for
it.

So far I've been working around it by manually reverting undesired updates, but
that is super tedious and inefficient.

Today I discovered a small utility,
[`pre-commit-update`](https://pypi.org/project/pre-commit-update/), which
explicitly supports that and was created precisely because of the limitation of
the original subcommand:

> pre-commit-update was created because there is no easy way to update your
> hooks by using pre-commit autoupdate as it is not versatile enough.

The tool (which is thankfully also written in Python, for uniformity) supports a
config file to skip certain hooks from `autoupdate`.
