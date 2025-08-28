---
title: "midnight commander: Fn keys"
date: 2025-08-28T09:45:54+02:00
tags:
  - dev
---

[Previously]({{< ref "2025-08-26-midnight-commander-use-default-editor" >}}).

It turns out it's quite inconvenient to use Fn keys (F1, F2, ...) in Macbooks
and in my [mechanical keyboard]({{< ref "2022-01-12-keychron-k2-review" >}}),
because I need to press a key combo to do so (Fn + the corresponding function
key).

This makes `mc` unusable from a practical standpoint.

We could
[remap](https://superuser.com/questions/461452/is-there-a-way-to-change-shortcuts-in-midnight-commander)
its keys (`~/.config/mc/mc.keymap`), but this is not portable. The whole point
of learning how to use an universal application like midnight commander is to
stick to defaults as much as possible.

There's a
[workaround](https://stackoverflow.com/questions/59334351/how-can-i-bind-f3-behavior-on-key-5-on-numeric-keypad-in-midnight-commander) though!

Instead of pressing F2 (which is effectively Fn + F2), press `Esc` followed by
`2`, emacs style. That's much more ergonomic, because the key presses need not
be simultaneous.

The most frequent combo I'll use from now on is `Esc + 0` (=F10) to quit `mc`.
