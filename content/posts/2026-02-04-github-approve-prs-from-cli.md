---
title: "GitHub: approve PRs from CLI"
date: 2026-02-04T11:10:58+01:00
tags:
  - dev
  - git
---

**Problem statement**: approve a given github pull request from the CLI.

Why?

Presumably you would do the PR review outside the GitHub web UI (it's slow,
eh?). How to do this is out of scope of this post.

Let's assume the review is done, and all that is left is to approve the PR.

Let's also assume you have a local checkout of the repository, and your CWD is
set to it.

First, check the PR out:

```shell
thiago.perrotta ~/Corp/terraform git:main
% gh co
? Select a pull request  [Use arrows to move, type to filter]
> 509   OPEN Change ai-resources repository visibility to internal [fix/ai-resources-visibility-internal]
[...]
```

Now approve it:

```shell
thiago.perrotta ~/Corp/terraform git:fix/ai-resources-visibility-internal? #509
% gh pr review --approve
✓ Approved pull request corp/terraform#509
```

It's possible to approve the PR without checking it out:

```shell
% gh pr review -h
Add a review to a pull request.

Without an argument, the pull request that belongs to the current branch is reviewed.


USAGE
  gh pr review [<number> | <url> | <branch>] [flags]
```

```shell
% gh pr review 509 --approve
```
