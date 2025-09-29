---
title: "git blame: prior commits"
date: 2025-09-29T10:41:15+02:00
tags:
  - dev
---

Let's say you want to inspect the history of a given file tracked in a git
repository. Straightforward with [`git-blame(1)`](https://man.archlinux.org/man/extra/git/git-blame.1.en):

```shell
% git --no-pager blame templates/secret-aws-info.yaml
5d478f6cb83b (Kubernetes Astronaut 2025-08-05 10:49:07 -0400  1) {{- if or (eq .Values.config.cloud.provider "aws") (not (.Values.config.externalDNS).enabled) }}
1aeb7c4d7b9b (Thiago Perrotta 2025-04-06 13:11:45 +0200  2) apiVersion: v1
1aeb7c4d7b9b (Thiago Perrotta 2025-04-06 13:11:45 +0200  3) kind: Secret
```

I am not interested in `5d478f6cb83b` though: it was just a refactoring change.
How can I look deeper in history? More specifically, I'd like to run `git blame`
on a point in time *before* commit `5d478f6cb83b`:

```shell
% git --no-pager blame 5d478f6cb83b^ templates/secret-aws-info.yaml
1aeb7c4d7b9b (Thiago Perrotta 2025-04-06 13:11:45 +0200  1) {{- if or (eq .Values.config.cloudProvider "aws") (not (.Values.config.externalDNS).enabled) }}
1aeb7c4d7b9b (Thiago Perrotta 2025-04-06 13:11:45 +0200  2) apiVersion: v1
1aeb7c4d7b9b (Thiago Perrotta 2025-04-06 13:11:45 +0200  3) kind: Secret
```

And I could keep going on:

```shell
% git --no-pager blame 1aeb7c4d7b9b^  templates/secret-aws-info.yaml
[...]
```

The Chromium project has a
[`git-hyper-blame(1)`](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/git-hyper-blame.html) script:

> Like git blame, but with the ability to ignore or bypass certain commits.

...that enables tracking refactoring/cleanup commits on a permanent basis for
skipping blame.
