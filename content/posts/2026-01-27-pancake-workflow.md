---
title: "pancake workflow (OR: how to solve problems only once)"
date: 2026-01-27T11:52:10+01:00
tags:
  - ai
  - bestof
  - dev
draft: true
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

I have a problem. An issue. A task. Let's exemplify with today's issue:

**Problem statement**: given a local git repository with various branches,
create a worktree for each of them.
