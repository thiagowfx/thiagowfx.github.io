---
title: "pre-commit: make a hook opt-in"
date: 2025-03-27T13:22:44+01:00
tags:
  - dev
---

Recently we added the following hook to our [pre-commit](https://pre-commit.com)
setup:

```yaml
repos:
  - repo: https://github.com/sbrunner/hooks
    rev: ee105bd276e163fce85744b39104ca563f923c47 # frozen: 1.4.0
    hooks:
      - id: helm-lock
```

It can be triggered with `pre-commit run --all-files helm-lock`.

It turned out to be an issue because not every developer has read-only access
to our helm repositories.

The workaround was to make this hook opt-in.

We can do so by adding it to the [manual stage](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages):

```yaml
repos:
  - repo: https://github.com/sbrunner/hooks
    rev: ee105bd276e163fce85744b39104ca563f923c47 # frozen: 1.4.0
    hooks:
      - id: helm-lock
        stages:
          - manual
```

It can be then invoked like this: `pre-commit run --all-files helm-lock
--hook-stage manual`.

An alternative could have been to instruct people to set
[`SKIP=helm-lock`](https://pre-commit.com/#temporarily-disabling-hooks), however
[defaults](https://world.hey.com/jason/software-defaults-15955a8e) are powerful.
