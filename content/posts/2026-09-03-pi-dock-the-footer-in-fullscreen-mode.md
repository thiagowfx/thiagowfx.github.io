---
title: "pi: enable fullscreen TUI mode"
date: 2026-09-03T13:48:57+02:00
tags:
  - dev
  - pi
---

**Today I learned**: [pi](https://pi.dev/) can keep its editor and footer at the
bottom of the terminal with fullscreen TUI mode, similarly to Claude Code.

The regular mode leaves terminal scrollback in charge. The `--tui-mode` option
switches to a viewport managed by Pi:

```shell
% pi --help | rg -- '--tui-mode|TUI mode'
  --tui-mode <mode>              TUI mode: regular (default) or fullscreen
```

For an one-off session:

```shell
% pi --tui-mode fullscreen
```

For a persistent default, add `tuiMode` to `~/.pi/agent/settings.json`:

```diff
diff --git pi/.pi/agent/settings.json pi/.pi/agent/settings.json
index 7d2fee8b..57fd5094 100644
--- pi/.pi/agent/settings.json
+++ pi/.pi/agent/settings.json
@@ -41,6 +41,7 @@
   "showCacheMissNotices": true,
   "theme": "catppuccin-mocha",
   "treeFilterMode": "user-only",
+  "tuiMode": "fullscreen",
   "warnings": {
     "anthropicExtraUsage": false
   }
```

The transcript scrolls inside Pi. The editor, queued messages, widgets, and
footer stay docked at the bottom.

The same setting is available under `/settings` as **TUI mode**. Pi 0.84.4
supports `regular` and `fullscreen`.
