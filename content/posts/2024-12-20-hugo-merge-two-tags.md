---
title: "hugo: merge two tags"
date: 2024-12-20T00:46:50-03:00
tags:
  - dev
  - meta
---

So far I've been using the `dev` and `devops` tags pretty much interchangeably
(and inconsistently) in this blog. There's no real difference: Dev and Ops work
overlap quite a lot. It's time to do some house cleaning and merge them. I
choose `dev` as it is more generic / agnostic.


First step, use `sed` to rename all `devops` tags to `dev`:

```shell
% ack -l -- "^  - devops"  | xargs -n 1 gsed -i -e 's/^  - devops/  - dev/g'
```

I use `gsed`, the GNU flavour of `sed`, in macOS via homebrew. This is necessary
because vanilla `/usr/bin/sed` from macOS keeps littering my system with `.-e`
files, the original files before inplace modification (`-i`), whereas `gsed`
doesn't. It saves me from having to do `rm **/*.-e` as an extra step.

Then delete one of two `- dev` occurrences in a row:

```shell
% ack -l -- "^  - dev"  | xargs -n 1 gsed -i -e '/^  - dev/{N;s/\n  - dev//;}'
```

I know how to write this `sed` expression by hand, but ChatGPT helped me craft
it nonetheless. The whole _cult_ of memorizing `sed`[^1] commands by heart has
been obsoleted by GenAI, for better or worse.

During iteration between the two commands above I snapshotted the first one with
a `git commit`, so that it was easy to `git reset --hard` my initial failed
attempt of the second command.

[^1]: And also `\LaTeX{}`...
