---
title: "pancake workflow (OR: how to solve problems only once)"
date: 2026-04-06T11:52:10+01:00
tags:
  - ai
  - bestof
  - dev
---

[Previously]({{< ref "2025-09-25-pancake-potpourri-scripts" >}}).

Software Engineers / Programmers and the like have had curated
[dotfiles](https://dotfiles.github.io/) for ages.

These days (2025s), we're evolving to times where it makes sense to curate
collections of other utilities as well:

- [prompts for LLMs](https://github.com/danielmiessler/Fabric)
- [commands / skills for LLMs](https://github.com/anthropics/skills)
- [miscellaneous utilities / tools](http://tools.simonwillison.net/)

[pancake](https://github.com/thiagowfx/pancake) is my own little repo for all
sorts of CLI utilities. Its [first
commit](https://github.com/thiagowfx/pancake/commit/454fa890999a149a580dbb899c768abfc11a0763)
was on Sep 25th, 2025, and now it's a core part of my workflow, which is what
this post will dive into.

First of all, obligatory xkcd:

{{< figure align="center"
src="https://imgs.xkcd.com/comics/is_it_worth_the_time.png"
link="https://xkcd.com/1205/"
alt="Don't forget the time you spend finding the chart to look up what you save. And the time spent reading this reminder about the time spent. And the time trying to figure out if either of those actually make sense. Remember, every second counts toward your life total, including these right now."
attr="XKCD Courtesy of Randall Munroe" >}}

It became _really_, _really_ cheap (in terms of time) to automate all sorts of
tasks with the advent of better coding agents last year. And this totally
changes the game.

## Workflow

I have a problem. An issue. A task. Let's exemplify with today's[^1] issue:

**Problem statement**: given a local git repository with various branches,
create a worktree for each of them.

Step 1: go to the pancake repo.

```shell
% z pancake
```

Step 2: prompt the LLM.

```
❯ create a new script called "wt" (short for worktree).
  Given a local git repo, it should create a worktree for each
  remote branch. Use the same conventions as the other scripts
  in this repo (help2man compatible, -h/--help, etc).
```

Claude Code reads the existing scripts, matches the conventions, and writes the
new one. I review it, maybe nudging it once or twice.

Step 3: commit, push, release.

```shell
% git add wt/
% git commit -a -m "new script: wt"
% git push
% just release
```

`just release` creates a CalVer tag (e.g. `2026.01.27.0`), pushes it, and
GitHub Actions updates the Homebrew formula automatically.

Step 4: install it.

```shell
% just update
```

This is a wrapper around `brew upgrade thiagowfx/pancake/pancake`.

Step 5: use it.

```shell
% cd ~/Workspace/some-repo
% wt
```

That's it. Problem solved, script in the toolbox, reusable forever.

The whole cycle — from "I wish I had a tool for this" to "it's installed and
working" — takes O(minutes). The LLM does virtually everything: writes the
script, follows the repo conventions, generates help text. I just steer and
review.

Before coding agents, I'd weigh whether it was worth the O(hours) to write a
proper script with argument parsing, help text, cross-platform support. Most of
the time the answer was "no", and I'd settle for a brittle alias or just
remember the command. Now the answer is almost always "yes".

The [xkcd chart](https://xkcd.com/1205/) above needs to be recalibrated. The
"time to automate" column collapsed by an order of magnitude, so long as you're
willing to burn LLM tokens.

As of this writing, pancake has 30+ scripts.

Some highlights:

- `retry` — retry a command until it succeeds, with timeouts and output diffing
  (inspired by `zsh`)
- `murder` — graceful process killing with signal escalation (TERM → INT → HUP →
  KILL) (one step above `pkill`)
- `notify` — cross-platform desktop notifications (inspired by `notify-send`)
- `timer` — countdown timer with notification when done
- `wt` — the worktree script from today

Each one started the same way: a problem, a prompt, a review, a release.

The repo name is silly but the idea is practical: **solve problems once**. Every
time I catch myself running a multi-step command more than twice or thrice, it
becomes a pancake script. The cost of doing so used to be high enough that I'd
only bother for frequent tasks. Now it's so low that even a task I'll run twice
a year gets a script, so long as it's reusable and comprensive enough.

In 2026, the compounding effect from curating your own toolbox does pay off.

[^1]: This post has been originally drafted in January 2026, but it was only
    finished in April 2026.
