---
title: "pre-commit: hazmat n1"
date: 2026-02-06T18:28:16+01:00
tags:
  - dev
  - pre-commit
---

**Problem statement**: some CLI tools accept only a single file as an argument.
Create a [pre-commit](https://pre-commit.com/) local hook for them.

A common workaround is to wrap it in a bash for-loop (`.pre-commit-config.yaml`):

```yaml
repos:
  - repo: local
    hooks:
      - id: my-formatter
        name: my-formatter
        language: system
        entry: bash -c 'for file in "$@"; do my-formatter fmt "$file"; done' --
        files: ^path/to/files/
```

This works, but it's noisy and easy to get wrong. Plus it's not elegant at all.

It turns out pre-commit has a built-in mechanism for this: [`hazmat
n1`](https://pre-commit.com/#codepre-commit-hazmat-n1code). It runs the hook
once per file, one at a time:

> some hooks only take one filename argument. this runs them one at a time
> (which is super slow!)

```yaml
repos:
  - repo: local
    hooks:
      - id: my-formatter
        name: my-formatter
        language: system
        entry: pre-commit hazmat n1 my-formatter fmt --
        files: ^path/to/files/
```

Note the trailing `--` at the end of `entry`.

This is a super recent feature, added in [pre-commit 4.5.0, in Nov
2025](https://github.com/pre-commit/pre-commit/commit/1af6c8fa9502336c6977c2ff3e79185bd97a6e57).

The name "hazmat" is supposedly intended to discourage people from using it.
Yet, here we are.

> "hazardous materials"
>
> pre-commit provides a few entry prefix "helpers" for unusual situations.
>
> in case it's not clear, using these is usually a bad idea.

It is a bad idea, but sometimes the underlying hook / script simply does not
support multiple arguments.
