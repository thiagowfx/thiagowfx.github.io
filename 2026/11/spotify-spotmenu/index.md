---
title: "spotify: spotmenu"
url: https://perrotta.dev/2026/11/spotify-spotmenu/
last_updated: 2026-11-07
---


[Previously]({{< ref "2025-09-10-raycast-spotify-macos-menu-bar" >}}).

Spotmenu:

> SpotMenu brings Spotify and Apple Music to your macOS menu bar. See what's
> playing, control playback, and enjoy beautiful album art — all without leaving
> your workflow.

It is free and [open source](https://github.com/kmikiy/SpotMenu), and requires
macOS 13 Ventura or later. It includes playback controls, global keyboard
shortcuts, and an optional two-line menu bar view.

Install with [Homebrew](https://brew.sh/):

```shell
% brew install spotmenu
```

Then open SpotMenu and grant it permission to access `Spotify.app` when prompted.

I prefer SpotMenu over Raycast's Spotify extension for showing the current song
in the macOS menu bar. It turns out Raycast became too bloated lately,
especially with the addition of Gen AI features. Now I no longer need it:

```shell
% brew uninstall raycast
```

