---
title: "Diffing two directories"
date: 2025-01-07T15:23:55-03:00
tags:
  - dev
---

**Problem statement**: Given an 'alpha' directory setup with a bunch of
configuration files (e.g. for CI/CD) that works for one cluster, and given
another 'bravo' directory for a distinct cluster, how can you compare the
differences between both directories e.g. perhaps to reconcile them, or to make
them consistent and uniform?

In this context, `cp -r` or `rsync` are out of scope. We do not want to clone
one directory into another: that would have been trivial.

# Diffoscope

Main tool: [Diffoscope](https://diffoscope.org/):

> In-depth comparison of files, archives, and directories.
>
> diffoscope tries to get to the bottom of what makes files or directories
> different. It will recursively unpack archives of many kinds and transform
> various binary formats into more human-readable form to compare them. It can
> compare two tarballs, ISO images, or PDF just as easily.

`diffoscope` gained a lot of popularity a few years ago, when linux
distributions started to care about [reproducible
builds](https://reproducible-builds.org/). In fact, it's highlighted in their
[tools](https://reproducible-builds.org/tools/) page.

**Usage**: Very similar to `diff`. Run `diffoscope {dir1} {dir2}`.

## Midnight Commander

The classic [`mc`](https://midnight-commander.org/):

> GNU Midnight Commander is a visual file manager, licensed under GNU General
> Public License and therefore qualifies as Free Software. It's a feature rich
> full-screen text mode application that allows you to copy, move and delete
> files and whole directory trees, search for files and run commands in the
> subshell. Internal viewer and editor are included.

It has two side-by-side panes. The idea is to navigate to a directory in each
pane (toggle pane focus with `Tab`), and then perform a visual inspection (use
arrow keys to navigate). The effect is comparable to having two side-by-side
`tmux` panes with [`ranger`](https://github.com/ranger/ranger) opened in each of
them.
