---
title: "pre-commit: periodic garbage collection"
date: 2026-04-07T10:56:21+02:00
tags:
  - dev
  - git
  - pre-commit
---

How funny, I do not remember setting this up. It is useful nonetheless:

```
thiago.perrotta ~
❯ crontab -l
30 12 1-7 * 5 [ "$(( ($(date +\%-d)-1)/7+1 ))" -eq 1 ] && /opt/homebrew/bin/pre-commit gc >> /Users/thiago.perrotta/.cronlogs/pre-commit-gc.log 2>&1

thiago.perrotta ~
❯ cat /Users/thiago.perrotta/.cronlogs/pre-commit-gc.log
2 repo(s) removed.
0 repo(s) removed.
3 repo(s) removed.
20 repo(s) removed.
10 repo(s) removed.
18 repo(s) removed.
2 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
4 repo(s) removed.
61 repo(s) removed.
5 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
1 repo(s) removed.
26 repo(s) removed.
17 repo(s) removed.
9 repo(s) removed.
11 repo(s) removed.
1 repo(s) removed.
3 repo(s) removed.
10 repo(s) removed.
1 repo(s) removed.
6 repo(s) removed.
1 repo(s) removed.
6 repo(s) removed.
4 repo(s) removed.
0 repo(s) removed.
15 repo(s) removed.
0 repo(s) removed.
2 repo(s) removed.
4 repo(s) removed.
1 repo(s) removed.
16 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
0 repo(s) removed.
```

What does `gc` do? As per the [docs](https://pre-commit.com/#pre-commit-gc):

> Clean unused cached repos.
>
> `pre-commit` keeps a cache of installed hook repositories which grows over
> time. This command can be run periodically to clean out unused repos from the
> cache directory.

This is on macOS. If I were on Linux, I'd prefer [systemd
timers](https://wiki.archlinux.org/title/Systemd/Timers) instead.
