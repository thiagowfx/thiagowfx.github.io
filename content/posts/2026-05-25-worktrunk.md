---
title: "Worktrunk"
date: 2026-05-25T10:57:00+02:00
tags:
  - ai
  - bestof
  - dev
  - git
  - pkm
  - pre-commit
---

[Worktrunk](https://worktrunk.dev/):

> Git worktree management for parallel AI agent workflows

I stumbled upon `worktrunk` (`wt`) due to a fortunate coincidence, serendipity
at its best. I was pitching my own [pancake
`wt`](https://github.com/thiagowfx/pancake/tree/master/wt) to someone, and this
person asked if I hadn't heard of `worktrunk`.

If you look at its [git star
history](https://www.star-history.com/?type=date&repos=max-sixty%2Fworktrunk)[^1],
you'll notice that it became popular _only_ at the beginning of 2026, whereas I
wrote my `wt` back in [November
2025](https://github.com/thiagowfx/pancake/commit/a4de064cdcd0b0c0f19177e58cda41c14f55c88a).
I did proper diligence at the time but couldn't find anything resembling my
vision. Normally I prefer to reuse rather than writing from scratch.

"AI agent workflows" is a tagline that does not convince me. If anything, it
actually worsens my appeal to try out the software. Seriously. Riding the wave
is not helpful.

What really sold me was its [usage
examples](https://worktrunk.dev/#context-git-worktrees). I was able to
immediately tell that it had very similar goals to my own `wt` (sans _AI_).

## Setup

First, [install](https://repology.org/project/worktrunk/versions) `worktrunk`:

```shell
brew install worktrunk
```

It is as simple (and rusty!) as it could be:

```shell
% brew ls worktrunk
/opt/homebrew/Cellar/worktrunk/0.53.0/.crates.toml
/opt/homebrew/Cellar/worktrunk/0.53.0/.crates2.json
/opt/homebrew/Cellar/worktrunk/0.53.0/bin/wt
/opt/homebrew/Cellar/worktrunk/0.53.0/etc/bash_completion.d/wt
/opt/homebrew/Cellar/worktrunk/0.53.0/sbom.spdx.json
/opt/homebrew/Cellar/worktrunk/0.53.0/share/fish/vendor_completions.d/wt.fish
/opt/homebrew/Cellar/worktrunk/0.53.0/share/zsh/site-functions/_wt
```

Shell completion is a bonus that you'll definitely want, as noted in a
[previous]({{< ref "2026-05-21-wt-exec-shell-vs-shell-integration" >}}) post:

```shell {filename="~/.zshrc.d/plugins.zsh"}
# worktrunk: https://worktrunk.dev/
(( $+commands[wt] )) && eval "$(wt config shell init zsh)"
```

The snippet above integrates well with my [own
dotfiles](https://github.com/thiagowfx/.dotfiles); a vanilla setup that most
people should follow is, instead, `wt config shell install`, which will populate
your `.bashrc` / `.zshrc` accordingly with `wt config shell init`.

The shell integration alone makes it compelling enough to switch to `wt`, but
we're not done yet.

## Workflow

It is possible to [customize
`wt`](https://worktrunk.dev/config/#user-configuration). I value muscle memory
and the ability to easily recall commands, therefore I crafted [this basic
configuration](https://github.com/thiagowfx/.dotfiles/blob/5c665572443c3fd22a35c15ad2f15abf90edd711/wt/.config/worktrunk/config.toml)
to facilitate the migration from my own `wt`:

```toml {filename="~/.config/worktrunk/config.toml"}
worktree-path = "{{ repo_path }}/.worktrees/{{ branch | sanitize }}"

[aliases]
add = "wt switch --create {{ args }}"
bd = "wt remove -D {{ args }}"
cd = "wt switch {{ args }}"
checkout = "wt switch {{ args }}"
cleanup = "wt step prune {{ args }}"
co = "wt switch {{ args }}"
commit = "wt step commit {{ args }}"
create = "wt switch --create {{ args }}"
del = "wt remove {{ args }}"
delete = "wt remove {{ args }}"
goto = "wt switch --no-cd {{ args }}"
ls = "wt list {{ args }}"
new = "wt switch --create {{ args }}"
prune = "wt step prune {{ args }}"
rm = "wt remove {{ args }}"
tui = "wt switch {{ args }}"
world = "wt step prune {{ args }}"
xl = "wt list {{ args }}"

[pre-start]
prek = "test -f .pre-commit-config.yaml && prek install --install-hooks || true"

[pre-merge]
prek = "test -f .pre-commit-config.yaml && prek run --from-ref \"$(git symbolic-ref --short refs/remotes/origin/HEAD)\" --to-ref HEAD || true"
```

You can start by running `wt config create` and then iterating upon the newly
generated config file, which is very well documented. What a great developer
experience!

Let's break it down.

We start with `wt add <feature>` (upstream: `wt switch --create`). This will
create a worktree:

```shell
tperrotta ~/Workspace/perrotta.dev git:master!?
% wt add myfeature
◎ Running pre-start user:prek
  test -f .pre-commit-config.yaml && prek install --install-hooks || true
prek installed at `/Users/tperrotta/Workspace/perrotta.dev/.git/hooks/pre-commit`
✓ Created branch myfeature from master and worktree @ ~/Workspace/perrotta.dev/.worktrees/myfeature
  39.06s user 6.26s system 251% cpu 17.984 total

tperrotta ~/Workspace/perrotta.dev/.worktrees/myfeature git:myfeature ⎇ myfeature
% git st
## myfeature...master
```

At any time, we can check the current status with `wt xl` (upstream: `wt list`):

```shell
tperrotta ~/Workspace/perrotta.dev/.worktrees/myfeature git:myfeature ⎇ myfeature
% wt xl
  Branch     Status        HEAD±    main↕  Remote⇅  Path                    Commit    Age   Message
@ myfeature      _                                  ./.worktrees/myfeature  23df7c41  50m   name author explicitly
^ master      !? ^|      +5   -6              |     .                       23df7c41  50m   name author explicitly

○ Showing 2 worktrees, 1 with changes
```

When opening a new shell, we can easily switch to the newly created worktree
from the repo root with `wt cd` (upstream: `wt switch`):

```shell
tperrotta ~/Workspace/perrotta.dev git:master!?
% wt cd myfeature
○ Switched to worktree for myfeature @ ~/Workspace/perrotta.dev/.worktrees/myfeature

tperrotta ~/Workspace/perrotta.dev/.worktrees/myfeature git:myfeature ⎇ myfeature
%
```

Once we are done (e.g. created/merged a pull request), we can delete the
worktree with `wt bd` or `wt del` (upstream: `wt remove -D`).

That's all! The core workflow steps are quite easy to assimilate.

You'll notice that my worktrees are created in a `.worktrees` directory within
the git repository root. This is due to my setting `worktree-path` in the config
file. The default behavior of `worktrunk` is to use sibling directories (e.g.
`../myrepo.myfeature` from the git root).

As you can see from my config file, I have also integrated [`prek`]({{< ref
"2026-04-20-migrating-from-pre-commit-to-prek" >}}) (`pre-commit`) to it:

- the creation of a worktree yields `prek install`
- the merge of a worktree (not covered in this post) yields `prek run` on the
  affected commits

`wt` has many other features; this is just the tip of the iceberg.

[^1]: GitHub stars are a vanity metric but they are occasionally useful.
