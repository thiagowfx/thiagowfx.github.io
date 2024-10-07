---
title: "bash built-in date"
date: 2024-10-07T15:12:20+02:00
tags:
  - dev
  - devops
---

To format dates [GNU
date](https://www.gnu.org/software/coreutils/manual/html_node/Examples-of-date.html)
is often used:

```shell
$ date '+%Y-%m-%d'
2024-10-07
```

It turns out bash (>=4.2) has this feature built-in as part of `printf`:

<!--more-->

```shell
$ printf '%(%Y-%m-%d)T\n'
2024-10-07
```

It does not work on `zsh` though:

```shell
% printf '%(%Y-%m-%d)T\n'

printf: %(: invalid directive
```

**Source**: https://blog.marco.ninja/notes/technology/linux/working-with-dates-in-bash-and-other-shells/
