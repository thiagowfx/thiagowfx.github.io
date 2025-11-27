---
title: "Chrome DevTools: toggle prefers-color-scheme"
date: 2025-11-27T18:46:08-03:00
tags:
  - dev
---

**Problem statement**: My blog automatically selects a light or dark color theme
depending on the user's browser or system preferences. Assume it currently
defaults to light. How to force dark mode temporarily?

This is needed for local testing and theme development purposes.

[Stack
Overflow](https://stackoverflow.com/questions/57606960/how-can-i-emulate-prefers-color-scheme-media-query-in-chrome):

- Open Chromium (or Google Chrome)
- Open DevTools
- Open the Command Control (Palette): `Cmd + Shift+ P`
- Type "Show rendering"
- Set the Emulate CSS media feature `prefers-color-scheme` to the desired value
