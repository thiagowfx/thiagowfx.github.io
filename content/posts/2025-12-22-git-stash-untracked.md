---
title: "git: stash untracked files"
date: 2025-12-22T02:30:06-03:00
tags:
  - bestof
  - dev
  - git
---

As I write this very post, this is what my git repository status looks like:

```shell
% git st
## master...origin/master
?? content/posts/2025-12-22-git-stash-untracked.md
```

What if I wanted to stash it?

```shell
% git stash
No local changes to save
% git st
## master...origin/master
?? content/posts/2025-12-22-git-stash-untracked.md
```

Nothing happens, because this post is a new file, not yet tracked by git.

The classic way to address this is to switch to another branch, commit
everything (e.g. with [`git-freeze`]({{< ref "2025-03-19-git-freeze-git-thaw" >}})), and then switch back. But this is slow.

Today I learned about `git stash -u`:

```
-u, --include-untracked, --no-include-untracked
    When used with the push and save commands, all untracked files are               also stashed and then cleaned up with git clean.

    When used with the show command, show the untracked files in the
    stash entry as part of the diff.
```

Let's try it:

```shell
% git stash -u
Saved working directory and index state WIP on master: 58cde6e88 hide codeblock header in RSS feeds
% git st
## master...origin/master
```

The new post gets stashed indeed!

I don't know how I missed this feature – I've wanted this functionality for
`stash` since forever!
