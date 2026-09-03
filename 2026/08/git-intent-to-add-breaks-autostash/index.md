---
title: "git: intent-to-add breaks autostash"
url: https://perrotta.dev/2026/08/git-intent-to-add-breaks-autostash/
last_updated: 2026-09-03
---


**Problem statement**: `git pull` could not autostash files added with
`git add -N`.

I had local work and was nine commits behind `origin/master`:

```shell
% git pull --force
Updating 266a5af537..07e4551075
error: Entry 'ci/goodreads_to_reading.py' not uptodate. Cannot merge.
Cannot save the current worktree state
fatal: Cannot autostash
```

`--force` does not replace local worktree files. My global Git configuration
makes `git pull` run `rebase.autostash`, which found an intent-to-add entry:

```shell
% git status --porcelain=v2
1 .M N... 100755 100755 100755 fcc319233ddf8e000ad2f735dbc2b0d760f467e5 fcc319233ddf8e000ad2f735dbc2b0d760f467e5 Justfile
1 .A N... 000000 000000 100755 0000000000000000000000000000000000000000 0000000000000000000000000000000000000000 ci/goodreads_to_reading.py
1 .M N... 100644 100644 100644 2787100c3968766ea3a84e7c28e28b5046d1da32 2787100c3968766ea3a84e7c28e28b5046d1da32 config/_default/config.yml
1 .A N... 000000 000000 100644 0000000000000000000000000000000000000000 0000000000000000000000000000000000000000 content/reading.md
1 .A N... 000000 000000 100644 0000000000000000000000000000000000000000 0000000000000000000000000000000000000000 data/reading.yaml
```

The `.A` records have an empty index object (`0000000`), so Git has tracked
path metadata without file content to stash.

`git reset` removes intent-to-add entries and leaves worktree files alone:

```shell
% git reset
% git pull
```

