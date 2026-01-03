---
title: "Optimize images"
date: 2024-12-28T16:14:19-03:00
tags:
  - dev
  - pre-commit
---

I like to use [oxipng](https://github.com/shssoichiro/oxipng) to optimize PNG (and other) images.

There's a [pre-commit hook](https://github.com/shssoichiro/oxipng/blob/master/.pre-commit-hooks.yaml) available, therefore enforcing it is a breeze:

```yaml
- repo: https://github.com/shssoichiro/oxipng
  rev: v9.1.3
  hooks:
    - id: oxipng
```

Surely you could run it in github actions as well, if you don't use pre-commit.com.

If I need to use it as an one-off, I can either run the `oxipng` binary directly,
or use a web version such as [Squoosh](https://squoosh.app/) ([via Simon Willison](https://github.com/simonw/til/blob/main/github-actions/oxipng.md)).
