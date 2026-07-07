---
title: "cmux"
url: https://perrotta.dev/2026/07/cmux/
last_updated: 2026-07-07
---


[cmux](https://cmux.com/) is the best implementation I've
seen for agent orchestrators apps like [Conductor](https://www.conductor.build/),
[T3 Code](https://github.com/pingdotgg/t3code),
[Dux](https://github.com/patrickdappollonio/dux), and friends:

> Open source Ghostty-based macOS terminal with vertical tabs and notifications
> for AI coding agents. Built for multitasking, organization, and
> programmability.

It's built on top of [Ghostty](https://ghostty.org/)[^1] and it's absolutely
amazing. It's effectively better than what I attempted to build once during an
on-site hackathon wiring Claude Code sessions to
[Obsidian](https://obsidian.md/).

The invariant I care about the most:

- restart your computer
- reopen `$APP`
- automatically restore every claude code session: layout & history preserved,
  scrollback intact

...is accomplished with fine elegance by `cmux`.

There's no need to manually fiddle with `tmux` / `zellij` resurrection or alike.

Pair it with [worktrunk]({{< ref "2026-05-25-worktrunk" >}}) (the `wt` CLI) for
bonus points. Its
[integration](https://worktrunk.dev/tips-patterns/#cmux-workspace-per-worktree)
is well-supported, achieving one cmux workspace per git worktree. For the time
being I'm still invoking `wt` manually though, because that gives me more
control.

It is very [customizable](https://cmux.com/docs/configuration).

[^1]: Desirable side effect: existing `ghostty` settings are automatically
    inherited. They aren't duplicated — they are effectively reused, which is
    superb.

