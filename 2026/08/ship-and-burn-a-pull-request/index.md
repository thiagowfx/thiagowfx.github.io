---
title: "/ship-and-burn a pull request"
url: https://perrotta.dev/2026/08/ship-and-burn-a-pull-request/
last_updated: 2026-08-19
---


**Problem statement**: ship a simple change (or commit, or pull request: you
name it), then wait for green CI, then remove its local branch and worktree
(=clean up).

It's 2026, so we'll codify this workflow in the form of an [agent
skill](https://skills.md/).

I created
[`/ship-and-burn`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/ship-and-burn/SKILL.md)
for that.

```text
/ship-and-burn [reviewer]
```

It's very important that you picture [this
movie](https://www.imdb.com/title/tt0887883/) whenever you invoke this skill.

The structure is the following, composing various of my other [skills](https://github.com/thiagowfx/skills):

```text
/ship ──> pull request ──> /pr-pass ──> green ──> delete local state
                                  └──> blocked ──> keep local state
```

The _implementation_ is a single `SKILL.md` Markdown file (naturally!):

```shell
% git show --stat --oneline 8e0eed7
8e0eed7 feat: add ship-and-burn skill

 README.md                                       |  1 +
 package.json                                    |  2 +-
 plugins/thiagowfx/.claude-plugin/plugin.json    |  2 +-
 plugins/thiagowfx/skills/ship-and-burn/SKILL.md | 67 +++++++++++++++++++++++++
 4 files changed, 70 insertions(+), 2 deletions(-)
```

The skill stops before cleanup whenever CI remains failed or pending 🔴.

Once checks pass 🟢, it verifies that the worktree/checkout is clean and that
every local commit exists on the remote:

```bash
test -z "$(git status --porcelain)"
git merge-base --is-ancestor HEAD "origin/$branch"
```

For a secondary (=non-base) worktree, [`wt`](https://github.com/adamtabrams/wt)
removes both the worktree and its local branch:

```bash
cd "$primary"
wt del -- --foreground "$branch"
```

The pull request and remote branch remain intact.

Should review comments arrive later, my `gh co` (or `wt co` for a separate
worktree) alias restores the branch and worktree before I address them:

```text
% gh co <pull-request>
% /address-pr-comments
```

This surely feels like living in the future!

And, when using a light harness like [pi](https://pi.dev), it's super fast!

