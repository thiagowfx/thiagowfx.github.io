---
title: "pre-commit: no-commit-to-branch hook"
date: 2025-03-21T16:33:04+01:00
tags:
  - dev
---

**Problem statement**: prevent developers from committing directly to master (or
main) in git.

You can do so server-side e.g. on GitHub via [branch protection
rules](https://stackoverflow.com/questions/46146491/prevent-pushing-to-master-on-github).

How to address it client-side though?

Countless times have I accidentally committed to master locally without creating
a branch first, only to have `git push` fail.

I wanted `git commit` to fail early – this is better than having `git push` fail
later.

[pre-commit.com](https://pre-commit.com/) provides an out-of-the-box hook called
[`no-commit-to-branch`](https://github.com/pre-commit/pre-commit-hooks), which
addresses exactly this use case.

I adopted it in our `.pre-commit-config.yaml`. It worked as intended locally.

There was a problem though: the pre-commit CI pipeline / workflow in main /
master would fail, because...errrr, there's a commit there. When you think of
it, it's working as intended, even though it comes across as unexpected.

The [solution](https://github.com/antonbabenko/pre-commit-terraform/pull/748/):
skip the hook in CI. Which is also the [official
recommendation](https://github.com/pre-commit/pre-commit-hooks/issues/954#issuecomment-1893632616):

```shell
SKIP=no-commit-to-branch pre-commit run
```

I wish this would be done out-of-the-box.
