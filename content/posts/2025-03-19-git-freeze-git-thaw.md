---
title: "git freeze, git thaw"
date: 2025-03-19T13:27:43+01:00
tags:
  - bestof
  - dev
---

Now I am becoming one of the snobs™ with the first sentence in the following
paragraph. Here we go.

I had [Claude
Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)[^1]
write me a pair of `git` utilities: `git freeze` and `git thaw`.

First of all: "to thaw" means "to defrost":

> To change from a frozen solid to a liquid by gradual warming.

Perhaps `git unfreeze` would have been more intuitive, let's leave the
bikeshedding to another day though.

What should these utilities do? They are inspired by the ones with the same name
in Chromium
[depot_tools](https://www.chromium.org/developers/how-tos/install-depot-tools/).
[Direct
link](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up):

> [`git-freeze(1)`](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/git-freeze.html)
> allows you to put the current branch in 'suspended animation' by committing
> your changes to a specially-named commit on the top of your current branch.
> When you come back to your branch later, you can just run
> [`git-thaw(1)`](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/git-thaw.html)
> to get your work-in-progress changes back to what they were.

Installing
[`depot_tools(7)`](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools.html)
just to get these two utilities is too bloated though. The security software at
work flagged it as malware[^2]. And they didn't even bother to package it for
Linux distributions in the first place.

## [`git-freeze`](https://github.com/thiagowfx/.dotfiles/blob/master/git/.bin/git-freeze)

```shell
#!/bin/sh
#
# git-freeze - Stage all files and create a git-freeze commit

set -e

# Check if we're inside a git repository
if [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" != "true" ]; then
  echo "Error: Not in a git repository"
  exit 1
fi

# Stage all changes (tracked and untracked)
git add -A

# Create a commit with the freeze message
git commit -m "git-freeze" -n

echo "Git freeze created successfully"
```

## [`git-thaw`](https://github.com/thiagowfx/.dotfiles/blob/master/git/.bin/git-thaw)

```shell
#!/bin/sh
#
# git-thaw - Undo a git-freeze operation

set -e

# Check if we're inside a git repository
if [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" != "true" ]; then
  echo "Error: Not in a git repository"
  exit 1
fi

# Check if there's at least one commit
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "Error: No commits yet"
  exit 1
fi

# Check if the last commit is a git-freeze commit
if ! git log -n 1 --pretty=%B | grep -q "^git-freeze$"; then
  echo "Error: Last commit is not a git-freeze commit"
  exit 1
fi

# Undo the git-freeze commit
if git rev-parse --verify HEAD^ >/dev/null 2>&1; then
  # If there's a parent commit, reset to it
  git reset "HEAD^"
else
  # If it's the initial commit, delete the reference and unstage everything
  git update-ref -d HEAD
  git restore --staged .
fi

echo "Git freeze thawed successfully"
```

## Post-AI cleanup

The only change I had to make was to add `-n` to `git commit` in `git-freeze` so
that pre-commit hooks would be skipped upon freeze.

## Usage

* Within an existing `git` repository, do some work in a custom branch.

* Decide that something else more important and/or urgent needs your attention.
Let go of [git worktrees](https://git-scm.com/docs/git-worktree) in this
instance.

* `git freeze`

* Switch to a new branch. Do whatever. Done.

* `git checkout <your previous branch>`

* `git thaw`

* Resume your previous work. Profit.

**Edit(2025-03-20)**: A friend asked that is the difference between `git freeze`
and `git stash`. The main difference is that `git stash` does not handle files
not yet tracked by `git`, whereas `git freeze` does. I think of `freeze` as the
equivalent of completely clearing up my physical desk of all objects so that I
can focus on something else.


[^1]: _An agentic coding tool made by Anthropic. Currently in beta as a research
    preview._

[^2]: In hindsight that's not even surprising.
