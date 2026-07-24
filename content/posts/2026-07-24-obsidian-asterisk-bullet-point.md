---
title: "obsidian: type * for a bullet point, not ** bold"
date: 2026-07-24T10:04:46+02:00
tags:
  - dev
  - pkm
---

**Problem statement**: in [Obsidian](https://obsidian.md), out-of-the-box,
typing `*` at the start of a new line emits `*|*` (an empty bold pair, cursor in
the middle) instead of starting a bullet point.

The culprit is **Settings → Editor → Auto pair Markdown syntax**. With it on,
every `*` auto-inserts its closing `*`, so a `*` followed by a space never gets
the chance to become a list marker. In fact, we get a bullet point followed by
a plain `*`, which we then have to delete.

To turn this setting off: set **Settings → Editor → Auto pair Markdown syntax**
to off.

**Now**: `*` followed by a space at the start of a line converts it to a bullet,
exactly like `-` does.
