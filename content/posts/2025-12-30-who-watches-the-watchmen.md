---
title: "Who watches the watchmen?"
date: 2025-12-30T11:02:51-03:00
tags:
  - bestof
  - dev
---

[Previously]({{< ref "2022-01-30-watch-files-and-react-to-changes-during-development" >}}).

I've been in love with [`watchexec`](https://github.com/watchexec/watchexec):

> Recursively monitors the current directory for changes, executing the command
> when a filesystem change is detected (among other event sources). By default,
> watchexec uses efficient kernel-level mechanisms to watch for changes.

It's a modern version of [`entr`](https://jvns.ca/blog/2020/06/28/entr/).

Its usage is very simple and easy to remember:

```shell
watchexec [--clear] [--] python main.py
```

...will re-run `python main.py` whenever it changes on disk.

`--clear` will `clear` the screen between successive runs.

Other useful invocations:

```shell
watchexec make
watchexec just
watchexec -e html,css,js make  # watch the given extensions for changes
watchexec -w src make          # watch the given directory
```

There are various other useful command-line switches, its [man
page](https://man.archlinux.org/man/watchexec.1) is very descriptive.

Here is a practical example when iterating on [`stack.py`]({{< ref
"2025-12-30-stack" >}}):

```shell
% watchexec --clear -- python stack.py
[Running: python stack.py]
[Command was successful]
```

```shell
% watchexec --clear -- ty check
[Running: ty check]
[Command was successful]
```
