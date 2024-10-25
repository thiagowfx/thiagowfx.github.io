---
title: "Conventional commits"
date: 2024-10-25T14:43:55+02:00
tags:
  - dev
  - devops
---

Conventional commits: https://www.conventionalcommits.org/:

> A specification for adding human and machine readable meaning to commit
> messages
>
> [...] a lightweight convention on top of commit messages. It provides an easy
> set of rules for creating an explicit commit history; which makes it easier to
> write automated tools on top of. This convention dovetails with SemVer, by
> describing the features, fixes, and breaking changes made in commit messages.

<!--more-->

It looks like the following:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

In practice, it looks like the following:

```
feat(sessions): add integration with github sso

So that developers no longer need to log in with the shared admin account.

Follow-up-of: #4242
Tested: `make test`
```

One way to enforce it in a `git` project is with its [pre-commit.com](https://pre-commit.com/) integration:

```yaml
repos:
  - repo: https://github.com/compilerla/conventional-pre-commit
    rev: v3.4.0
    hooks:
      # https://conventionalcommits.org
      - id: conventional-pre-commit
        stages: [commit-msg]
        args:
          # keep-sorted start
          - base
          - build
          - chore
          - ci
          - docs
          - feat
          - fix
          - meta
          - refactor
          - test
          # keep-sorted end
```

The above hook only runs in the `commit-msg` stage, which is not installed by
default via `pre-commit install`. You'll need to pass `-t commit-msg` to it.

I have mixed experiences and opinions with conventional commits in a team
setting.

In a [previous team](https://github.com/GoogleChromeLabs/chromium-bidi), it was
successfully
[adopted](https://github.com/GoogleChromeLabs/chromium-bidi/pull/900). It was
very easy to generate changelogs this way.

In other teams, only a handful of members adopted it. In this setting there
isn't much value in enforcing a half-adopted convention, it must be all or
nothing.

In repositories that I own, I tend to adopt something in-between, writing a
prefix in the commit message title.
