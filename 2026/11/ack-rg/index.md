---
title: "ack → rg"
url: https://perrotta.dev/2026/11/ack-rg/
last_updated: 2026-11-07
---


I am trying hard to migrate from `ack` to `rg`, but my muscle memory is
struggling to do so:

```
tperrotta ~/Workspace/perrotta.dev git:master✘?
❯ ack
zsh: correct 'ack' to 'ac' [nyae]? n
The program 'ack' is currently not installed. You can install it by typing:
  brew install ack

127 tperrotta ~/Workspace/perrotta.dev git:master✘?
x ack foo
zsh: correct 'ack' to 'ac' [nyae]? n
zsh: command not found: ack foo
```

And I don't feel like `alias ack=rg`, as they are not fully compatible with each
other.

`rg` is faster and more modern (citation needed).

