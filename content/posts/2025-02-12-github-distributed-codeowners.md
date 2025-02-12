---
title: "GitHub Distributed CODEOWNERS"
date: 2025-02-12T13:57:29+01:00
tags:
  - bestof
  - dev
---

We recently adopted Andrew Ring's "Distributed CODEOWNERS"
([github](https://github.com/andrewring/github-distributed-owners)) in some
parts of our codebase.

You know the concept of
[`OWNERS`](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/code_reviews.md)
if you've worked at Google, or in the Chromium codebase. As far as I know, they
  were the pioneers of this concept.

Outside Google, GitHub has popularized it with
[CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
It's pretty much the same concept, it's just implemented differently.

## Google

You have distributed `OWNERS` files throughout the whole repository. For
example:

```
java/
  OWNERS (a)
  project1/
    OWNERS (b)
  project2/
    OWNERS (c)
```

`OWNERS` in (b) have CL (ChangeList) / PR (Pull Request) approval permissions
for `java/project1`, but not for `java/project2`.

`OWNERS` in (a) have approval permissions for both projects.

## GitHub

There's a single `.github/CODEOWNERS` file that controls the whole repository:

```
* a
/java/project1 b
/java/project2 c
```

## Distributed CODEOWNERS

What if we wanted to adopt the Google approach in GitHub? Use Andrew's tool!

What does it do? It collects all scattered `OWNERS` in the repository and
consolidates them in a single `.github/CODEOWNERS` file, expected by GitHub.
Win-win!

I like to adopt it with a [pre-commit](https://pre-commit.com) hook:

```yaml
repos:
  - repo: https://github.com/andrewring/github-distributed-owners
    rev: v0.1.9
    hooks:
      - id: github-distributed-owners
        files: .*/OWNERS$|^\.github/CODEOWNERS$
```

Then it gets automatically managed via CI and/or local commits. It can also be
triggered manually with:

```shell
pre-commit run -a github-distributed-codeowners
```
