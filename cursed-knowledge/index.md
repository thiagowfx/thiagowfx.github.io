---
title: "Cursed Knowledge"
url: https://perrotta.dev/cursed-knowledge/
last_updated: 2026-07-29
---


Cursed knowledge learned while building software, that I wish I never knew.

Inspired by [immich's Cursed Knowledge](https://immich.app/cursed-knowledge).

---

## pi session cwd

*2026-07-29*

[pi](https://pi.dev)'s session working directory is cursed because it's frozen at session creation with
no supported way to change it mid-run — extensions that need to redirect into a
worktree resort to hacks like killing the process and replaying keystrokes via tmux.
Multiple feature requests ([#3921](https://github.com/earendil-works/pi/issues/3921),
[#2992](https://github.com/earendil-works/pi/issues/2992),
[#4423](https://github.com/earendil-works/pi/issues/4423)) were all closed
not-planned/unsupported.

