---
title: "caveman: talk like caveman, save tokens"
date: 2026-06-25T01:30:43+02:00
tags:
  - ai
  - bestof
  - dev
---

Long Claude Code sessions eat a lot of context, fast. Each response injects
tokens into the context window: prose-heavy replies **burn** through it faster
than terse ones ($$).

[caveman](https://github.com/JuliusBrussee/caveman) is a Claude Code plugin that
switches the model into a **compressed** communication style: drops articles,
filler words, and pleasantries while keeping full technical accuracy. Claims
~75% token reduction per response.

Installation:

```shell
% /plugin marketplace add JuliusBrussee/caveman
Successfully added marketplace: caveman
% /plugin install caveman@caveman
✓ Installed caveman. Run /reload-plugins to apply.
```

After `/reload-plugins`, manually activate with `/caveman`. Manually deactivate
it by saying "normal mode" or "caveman off".

A session-start hook fires automatically on the next session, effectively
auto-enabling it (`M-x caveman-mode` emacs vibes).

It ships three modes (`lite`, `full`, `ultra`) and three subagent presets
(`cavecrew-investigator`, `cavecrew-builder`, `cavecrew-reviewer`). I don't
care. This is unnecessary bloat. An irony, for a plug-in intended to mitigate
bloat.

The out-of-the-box installation is enough; tweaks are not necessary. The
defaults are sensible.

In practice: responses are punchy. The model still reasons correctly; it just
stops narrating. No "Sure, I'd be happy to help with that." Just the answer.

~~You're absolutely right.~~ no more!?

- - -

🤖 *Drafted with `/bloggify`.*
