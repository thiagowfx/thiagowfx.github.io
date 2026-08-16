---
title: "git: repair unreachable object corruption"
date: 2026-07-29T22:16:46+02:00
tags:
  - bloggify
  - coding
  - dev
  - git
---

**Problem statement**: `git fsck` failed in a linked worktree, even though every
branch and reflog remained intact.

The initial diagnosis was noisy: missing blobs, hundreds of dangling objects, and
an invalid commit graph:

```text
missing blob 97f9a2ed29f84e47848244c2d2626b2536a33c55
error: Could not read 003fb43a3aa361b52f2ab3f27bdabcb9b5137103
failed to parse commit 003fb43a3aa361b52f2ab3f27bdabcb9b5137103 from object database for commit-graph
```

Worktrees have their own administrative directory but share an object database:

```shell
% git rev-parse --git-dir
.git/worktrees/thiagowfx-prm-revenue-tagging
% git rev-parse --git-common-dir
.git
```

I checked every missing blob against objects reachable from refs and reflogs. None
were reachable. Before removing them, I backed up objects, commit graphs, and index:

```shell
% common=$(git rev-parse --git-common-dir)
% backup="$common/repair-backup-20260729221124"
% mkdir -p "$backup"
% cp "$(git rev-parse --git-path index)" "$backup/worktree-index"
% ditto "$common/objects" "$backup/objects-before-gc"
% mv "$common/objects/info/commit-graphs" "$backup/commit-graphs"
```

The index also had an invalid cache-tree entry. Rebuilding it from `HEAD` preserves
working-tree files; comparing its old entries found no staged changes:

```shell
% git read-tree HEAD
% GIT_INDEX_FILE="$backup/worktree-index" git ls-files --stage > /tmp/index-before-repair
% join -t $'\t' -v 1 \
    <(awk '{print $4 "\t" $1}' /tmp/index-before-repair | sort) \
    <(git ls-files --stage | awk '{print $4 "\t" $1}' | sort)
% # no output
```

Then Git could discard unreachable corrupt objects and rebuild its graph:

```shell
% git gc --prune=now
% git fsck --full --strict
% echo $?
0
% git fsck --full --no-reflogs --strict >/tmp/fsck
% echo $?
0
```

The backup remains under `.git/repair-backup-20260729221124`. `fsck` is clean;
recovery material remains available.

It's very weird to experience this kind of error. We're not used to it.

The one trick to remember from this post is `git fsck`.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
