---
title: "git: empty stash"
date: 2026-04-09T12:48:57+02:00
tags:
  - dev
  - git
---

There are too many entries in my `git` stash:

```shell
% git stash list | wc -l
69
```

I would like to completely empty it, nothing there matters, it's all draft junk
accumulated over months.

```shell
% git stash clear
```

Verification:

```shell
% git stash list | wc -l
0
```

That's all! It's the first time I ran this command.

Normally I do this instead:

```shell
% git stash drop
```

> _drop_
>
> Remove a single stash entry from the list of stash entries.

In `zsh` land, if I hadn't learned about `stash clear`, I could have done
the following instead:

```shell
% repeat 100 git stash drop
```

...popping each entry one by one.
