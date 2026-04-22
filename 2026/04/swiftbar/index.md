---
title: "swiftbar"
url: https://perrotta.dev/2026/04/swiftbar/
last_updated: 2026-04-22
---


[SwiftBar](https://github.com/swiftbar/SwiftBar):

> Powerful macOS menu bar customization tool

It is comparable to [i3bar](https://i3wm.org/i3bar/) and
[i3status](https://i3wm.org/docs/i3status.html), but on macOS.

My current setup:

![macOS status bar](statusbar.webp)

This screenshot is from a few months ago (January).

From left to right, skipping the default macOS Control Center icons on the
right side:

- **On-call tribunal · in 7m**: next calendar event of the day, with a countdown — via a [Raycast extension](https://www.raycast.com/changelog/1-32-0)
- 🟢 **VPN**: VPN status — green when connected (SwiftBar)
- 🔒 **TP [6h]**: time left on my [Teleport](https://goteleport.com/) session (SwiftBar)
- ☁️ **AWS [2h]**: time left on my AWS credentials (SwiftBar)
- 👤 **Decisive Battle · 目黒将士**: currently playing track on Spotify[^1] — via a [Raycast extension](https://www.raycast.com/mattisssa/spotify-player)

Each SwiftBar item is its own script, refreshed on its own cadence. The shorter
the refresh interval, the more system resources it takes, naturally.

Scripts live in `~/.config/swiftbar`.

Here's a typical one: `~/.config/swiftbar/corp-status.30s.sh`.

`30s` in the filename means that the script is refreshed every 30 seconds.

[^1]: Final Fantasy OST!

