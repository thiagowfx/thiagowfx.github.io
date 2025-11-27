---
title: "ghostty: quick terminal"
date: 2025-11-27T01:43:35-03:00
tags:
  - dev
---

[Ghostty](https://ghostty.org/) has a
[Quake](https://en.wikipedia.org/wiki/Quake_(video_game))-like[^1] mode to pop
up a terminal (console) from the top of the screen, no matter where you are.

Enable it with this setting in your Ghostty config:

```
keybind = global:cmd+;=toggle_quick_terminal
```

`global:` is what does the "no matter where you are" magic. Even if your focus
is in another application / window, the shortcut will still work. I did not test
it with conflicting shortcuts, it's better to pick an uncommon one (don't pick
`Cmd + T`!).

`Cmd + ;` seems reasonable. I am also dabbling with `Cmd + Shift + Enter`.

The terminal session persists. Say you open `vim` and then close the terminal.
Upon opening it again, `vim` will still be there. This blog post was written
from the quick terminal.

[^1]: See also: [Guake Terminal](https://guake.github.io/).
