---
title: "Finding linters"
date: 2024-12-08T23:40:26+01:00
tags:
  - dev
---

A no-brainer and effective way to increase code quality in an organization is by
the means of incorporating linters into your CI/CD pipeline.

But where can you find them?

<!--more-->

Some sources of inspiration include curated "super-mega-hyper" linter packages,
such as:

- https://megalinter.io
- https://github.com/super-linter/super-linter

I am not generally a fan of employing these collections directly because it's
not possible to exert tight control over them, and there's no security or
reproducibility guarantee of their pipeline.

Instead, I cherry-pick interesting / useful linters from their packs,
effectively using them as serendipity sources for linters.

Bonus points whenever there's out-of-the-box integration with the pre-commit.com
framework i.e. whenever there's a `.pre-commit-config.yaml` file present at the
root of the git repo.
