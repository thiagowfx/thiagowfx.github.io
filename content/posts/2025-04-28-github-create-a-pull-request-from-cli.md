---
title: "GitHub: create a pull request from CLI"
date: 2025-04-28T14:12:57+02:00
tags:
  - dev
---

Using the [`gh`](https://cli.github.com/) tool (the official GitHub CLI tool):

```shell
% gh pr create [--draft]
```

It will prompt for more information. `--draft` creates the PR in the draft
state, delaying code review assignments.

To skip all prompts and simply use the commit message to fill in the PR Title
and the PR description, pass `--fill`:

```shell
% gh pr create --fill
```

```shell
% gh pr create --help | grep -- --fill
`--body` to skip this, or use `--fill` to autofill these values from git commits.
alongside `--fill`, the values specified by `--title` and/or `--body` will
  -f, --fill                 Use commit info for title and body
      --fill-first           Use first commit info for title and body
      --fill-verbose         Use commits msg+body for description
```
