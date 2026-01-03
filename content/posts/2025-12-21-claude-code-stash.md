---
title: "Claude Code: stash"
date: 2025-12-21T16:48:26-03:00
tags:
  - ai
  - dev
---

**Problem statement**: You're midway in a long, multi-line prompt in Claude
Code.

```
> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum
dolor sit amet.
```

Now you would like to "stash" it away temporarily to run a more important,
one-off prompt, before resuming.

If this were an one-line prompt, you could hit `C-u`, run your one-off, and then
hit `C-y`. This is pure `readline` / `emacs` wizardry, supported natively in the
TUI that Claude Code employs.

For the multi-line situation, hit `C-s`.

Claude will then show:

```
› Stashed (auto-restores after submit)
```

From here, run your one-off. Your initial prompt will be automatically
restored upon completion.

Alternatively, press `C-s` again to restore the initial prompt.

This is a simple quality-of-life improvement, but it's specific to Claude Code.
`C-u` + `C-y` works almost everywhere though.
