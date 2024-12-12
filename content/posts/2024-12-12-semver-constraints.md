---
title: "Semantic versioning constraints"
date: 2024-12-12T12:34:39-03:00
tags:
  - dev
  - devops
---

When working with semantic versioning a.k.a. [semver](https://semver.org/), it's
often useful to use range constraints[^1] to express the versions you're
interested in.

The most useful ones are the tilde (`~`) and the circumflex / hat / caret
(`^`)[^2]:

- `~4.2.1`: picks up `4.2.x` for `x >= 1`
- `^5.0.2`: picks up `5.x.y` for `x >= 0` and `y >= 2`

Popular software tooling that uses them include:

- nodejs / npm packages
- terraform
- ruby gems (here `~>` is used instead of simply `~`)

<!--more-->

Sometimes I use https://jubianchi.github.io/semver-check to double-check[^3], or
to teach teammates how the range constraints work.


[^1]: Or constraint ranges? 🤔
[^2]: In Portuguese we say "acento circunflexo" (circumflex accent). In English,
    AFAIK, "caret" is the most precise term however people typically refer to it
    as "hat".
[^3]: [Example](https://jubianchi.github.io/semver-check/#/~0.1.1/0.1.3).
