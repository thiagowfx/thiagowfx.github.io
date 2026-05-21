---
title: "wt: exec shell vs shell integration"
date: 2026-05-21T17:02:29+02:00
tags:
  - dev
  - git
---

[Previously]({{< ref "2026-05-21-homebrew-conflicts" >}}).

**Problem statement**: my [`wt`](https://github.com/thiagowfx/pancake/tree/master/wt) tool's `cd` subcommand does not survive a terminal split — the new pane opens at the original directory, not the worktree. [`worktrunk`](https://worktrunk.dev/)'s `wt` does(!)

A subprocess cannot change its parent's working directory (PWD). `wt.sh` works around it by replacing the script process with a fresh shell:

```bash
cd "$target_path" || exit 1
exec "$SHELL"
```

The `exec "$SHELL"` is the culprit. The interactive shell process is gone, replaced by a new one rooted in the worktree. The terminal emulator's record of "what shell is (currently) running in this pane" still points to the original PID's cwd at split time — not the new shell's. Shell history, env vars, `pushd`/`popd` stack, prompt state: all lost too (not that I particularly care about all these).

`worktrunk` ships a [shell integration](https://worktrunk.dev/config/#shell-integration) step:

```shell
% wt config shell install
```

That installs a function in `~/.bashrc` / `~/.zshrc` (or equivalent for other shells) which `eval`s the binary's output in the *current* shell. The `cd` happens in the shell we are actually using. No `exec`, no replacement, no lost state. Splits inherit the real, updated cwd.

The README of my `wt` already documents the escape hatch:

```shell
% cd "$(wt goto feature-x)"
```

…which is the same trick, just manual. The `goto` subcommand prints the path; `cd` runs in the shell.

The proper fix is to ship a `wt shell init` that emits an eval-able function, and route `cd`/`bd`/`add` through it. I do not plan to do so though, `wt` is not supposed to become a complex project. In fact, perhaps it will even be deprecated, should I end up switching to `worktrunk`.
