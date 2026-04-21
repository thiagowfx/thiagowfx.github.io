---
title: "swiftbar: my macOS status bar"
date: 2026-04-20T23:45:00+02:00
tags:
  - dev
  - macos
---

[SwiftBar](https://github.com/swiftbar/SwiftBar):

> SwiftBar lets you put the output from any script or program right in your
> macOS menu bar.

My current setup:

![macOS status bar](statusbar.webp)

From left to right, skipping the default macOS Control Center icons on the
right:

- **On-call tribunal · in 7m**: next calendar event of the day, with a countdown
- 🟢 **VPN /**: VPN status — green when connected
- 🔒 **TP [6h] /**: time left on my [Teleport](https://goteleport.com/) session
- ☁️ **AWS [2h]**: time left on my AWS credentials
- 👤 **Decisive Battle · 目黒将士**: currently playing track

Each item is its own script, refreshed on its own cadence. The shorter the
refresh interval, the more system resources it takes, so tune accordingly.
