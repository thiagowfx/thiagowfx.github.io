---
title: "keychron k2: bluetooth always-on"
date: 2026-06-20T23:51:02+02:00
tags:
  - macos
---

**Problem statement**: the Keychron K2 (C3, stock firmware) disconnects from
macOS after ~10 minutes idle — and there's no way to prevent it.

I spent some time looking for a fix. The usual suggestions:

- Disable Bluetooth auto-sleep in macOS? macOS doesn't do that — the keyboard
  decides to sleep, not the host.
- Install a keep-alive app? The keyboard's firmware powers down its own radio.
  By the time the app could send a ping, there's nothing on the other end
  listening.
- Key combo to disable sleep on the keyboard? Only on newer Keychron boards
  (QMK/VIA). The C3 runs stock firmware with no configurable sleep timer.
- Flash QMK and set an infinite sleep timeout? The C3 isn't a QMK board. Can't.

The C3 stays *paired* — macOS reconnects on the first keypress, with ~1s lag.
That's the firmware's design. The radio sleeps to save battery. Nothing running
on the Mac can reach through a sleeping radio and wake the other end.

The only real fix: flip the side switch to **Cable**, plug in USB-C. No
Bluetooth, no sleep, no drops.

Time to shop for a new Keychron, with QMK?

- - -

🤖 *Drafted with `/bloggify`.*
