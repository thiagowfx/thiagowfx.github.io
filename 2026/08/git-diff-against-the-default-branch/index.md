---
title: "git: diff against the default branch"
url: https://perrotta.dev/2026/08/git-diff-against-the-default-branch/
last_updated: 2026-08-31
---


**Problem statement**: create a git alias / script to diff against the default
upstream branch, inspired by chromium [`depot_tools(7)`](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/git-upstream-diff.html)
`git-upstream-diff(1)`:

> git-upstream-diff — Print a diff of the current branch, compared to its
> upstream.

I used to have an alias for it in 2024, but I did not have a reliable way at the
time to find whether a repository used `main`, `master`, or something else:

```gitconfig
udiff = !git diff $(git show-branch --merge-base HEAD 2>/dev/null)~1
```

It lasted one month (repository archeology FTW):

```shell
% git log --all --format='%h %ad %s' --date=short --grep=udiff -i
da961f1 2026-08-31 git: restore udiff command
a4f13e9 2024-10-07 git: remove udiff
244ca3b 2024-09-02 git: add udiff alias
```

[Worktrunk](https://worktrunk.dev/) now gives me what I always wanted:

```shell
% wt config state default-branch
master
```

[Previously]({{< ref "2026-05-25-worktrunk" >}}).

As git finds executables named `git-<command>` on `PATH`, the replacement is
a small script at `git/.bin/git-udiff`:

```shell
#!/bin/sh
#
# git-udiff - Show changes since the current branch diverged from the default branch

set -e

if [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" != "true" ]; then
  echo "Error: Not in a git repository"
  exit 1
fi

default_branch=$(wt config state default-branch 2>/dev/null)
merge_base=$(git merge-base "$default_branch" HEAD)

exec git diff "$merge_base" "$@"
```

Why a script instead of an alias? Because it is no longer a readable one-liner.

`git merge-base` finds the divergence commit. Diffing from that commit without
an end revision includes committed, staged, and unstaged tracked changes.
Forwarding `"$@"` keeps regular diff options and path filters working:

```shell
% git udiff --stat
 claude/.claude/settings.json | 3 ++-
 pi/.pi/agent/settings.json   | 2 +-
 2 files changed, 3 insertions(+), 2 deletions(-)

% git udiff --name-only -- pi/.pi/agent/settings.json
pi/.pi/agent/settings.json
```

The command is back, now based on repository state instead of a branch-name
guess:

```shell
% git show --stat --oneline da961f1
da961f1 git: restore udiff command
 git/.bin/git-udiff | 15 +++++++++++++++
 1 file changed, 15 insertions(+)
```

