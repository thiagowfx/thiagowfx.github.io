---
title: "Toggle light / dark mode"
date: 2025-12-21T18:24:28-03:00
tags:
  - dev
  - meta
---

After dabbling about this for a while, I decided to add a non-intrusive icon to
the footer of this site, wherein you can manually toggle between the light and
dark theme. Your choice is persistent locally indefinitely, courtesy of
[`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)[^1].

[^1]: `localStorage.getItem('theme')`.

Previously, the theme used to be set automatically depending upon your system /
browser preferences
([`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)).
