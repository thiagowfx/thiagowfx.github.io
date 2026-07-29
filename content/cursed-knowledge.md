---
title: "Cursed Knowledge"
email: false
tocOpen: true
---

Cursed knowledge learned while building software, that I wish I never knew.

---

## pi session cwd is cursed

*2026-07-29*

pi's session working directory is cursed because it's frozen at session creation with
no supported way to change it mid-run — extensions that need to redirect into a
worktree resort to hacks like killing the process and replaying keystrokes via tmux.
Multiple feature requests ([#3921](https://github.com/earendil-works/pi/issues/3921),
[#2992](https://github.com/earendil-works/pi/issues/2992),
[#4423](https://github.com/earendil-works/pi/issues/4423)) were all closed
not-planned/unsupported.
