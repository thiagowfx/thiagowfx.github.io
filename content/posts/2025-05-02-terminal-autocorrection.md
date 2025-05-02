---
title: "Terminal autocorrection"
date: 2025-05-02T16:43:42+02:00
tags:
  - dev
  - serenity
---

Appreciate this:

```shell
% gitp ushm
zsh: correct 'gitp' to 'git' [nyae]? y
WARNING: You called a Git command named 'ushm', which does not exist.
Continuing in 1.0 seconds, assuming that you meant 'pushm'.
branch 'master' set up to track 'origin/master' by rebasing.
Everything up-to-date
```

- [`zsh` autocorrection](https://hunden.linuxkompis.se/2018/08/04/spell-check-and-auto-correction-of-commands-in-zsh.html)
- [`git` autocorrection](https://andycarter.dev/blog/auto-correct-git-commands)
