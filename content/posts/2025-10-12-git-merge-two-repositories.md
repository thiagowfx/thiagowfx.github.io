---
title: "git: merge two repositories"
date: 2025-10-12T15:52:06+02:00
tags:
  - dev
  - git
---

Daniel Roy Greenfeld, [TIL: Merging two git projects](https://daniel.feldroy.com/posts/til-2025-09-merging-two-git-projects):

> Of course this task can be done with copy/paste. The challenge there is the
> loss of git history. All the history of struggles and tribulations are gone.
> More important is the attribution - unless any and all contributors are made
> co-authors. But then the volume of attribution isn't accurate, some one who
> made one tiny change gets as much credit as the leading contributor.

Adapted to my own words: we will merge "atreides" into "harkonnen".

- `cd` to `harkonnen`
- `git remote add atreides {atreides git repo URL}`
- `git fetch atreides` (or `git fetch --all`)
- `git merge atreides/master --allow-unrelated-histories`  # or main, if applicable

Fin.
