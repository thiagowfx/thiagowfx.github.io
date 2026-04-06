---
title: "Quick and dirty random password generator"
url: https://perrotta.dev/2025/01/quick-and-dirty-random-password-generator/
last_updated: 2026-01-01
---


On Linux / macOS, use `/dev/urandom`, with a `tr` pass-through filter:

```shell
% tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 20 && echo
BLH1gVgdukdmTcvopOuC
```

In the example above only alphanumeric characters are allowed.

There are other popular ways to do so:

- Dice ([Douglas Muth](https://diceware.dmuth.org/),
  [EFF](https://www.eff.org/dice)).
- [`pwgen`](https://pwgen.sourceforge.net/) (via `brew home pwgen`)

