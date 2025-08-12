---
title: "git: --no-pager"
date: 2025-08-12T12:21:22+02:00
tags:
  - bestof
  - dev
---

Let's say you use color highlighting to visually inspect diffs with `git`, such
as [`delta`](https://github.com/dandavison/delta) or
[`diff-highlight`](https://github.com/git/git/blob/master/contrib/diff-highlight/README)
or [`diffr`](https://github.com/mookid/diffr).

**Implication**: whenever you run `git diff`, `git show`, or any other `git`
command that produces a diff, it will emit colors (typically red and green).

Colors are great for local visual inspection, but they are terrible for sharing.
They won't be carried over with copy-and-paste.

If you intend to share diff output (e.g. to a Q&A site, with teammates), it's
better to emit `-` and `+`, as vanilla `diff` does.

The easiest way to do so is to pass `--no-pager` to `git`:

```shell
git --no-pager diff a83bc395
git --no-pager show HEAD
```

For example, a recent commit in my
[dotfiles](https://github.com/thiagowfx/.dotfiles):

```shell
% git --no-pager show HEAD~1
commit 52b1e91b0f1d93176ec768aa6158974fc401f335
Author: Thiago Perrotta <{redacted}>
Date:   Thu Aug 7 12:00:47 2025 +0200

    fix mr

diff --git bin/.bin/sd-world bin/.bin/sd-world
index c46be0e..44c0b47 100755
--- bin/.bin/sd-world
+++ bin/.bin/sd-world
@@ -58,7 +58,7 @@ esac
 run_if_exists "claude" claude update

 # myrepos
-run_if_exists "mr" mr -d ~ update
+(cd ~ && run_if_exists "mr" mr update)

 # source corp updates if any
 run_if_exists "sd-world-corp"
```

Note that `--no-pager` is a `git`-level option: it should be specified before
the git subcommand. The following does not work:

```shell
% git show HEAD~1 --no-pager
fatal: unrecognized argument: --no-pager
```
