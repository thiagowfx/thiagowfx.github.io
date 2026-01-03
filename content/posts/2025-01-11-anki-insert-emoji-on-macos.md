---
title: "Anki: insert emoji on macOS"
date: 2025-01-11T00:28:48-03:00
tags:
  - dev
  - macos
---

There's a longstanding bug in [Anki](https://apps.ankiweb.net/) on macOS: it's
not possible to insert an emoji in the editor view via the system emoji picker.

Whenever you click an emoji, the emoji picker closes whilst nothing is inserted.

This has always annoyed me.

Today I found a
[workaround](https://forums.ankiweb.net/t/macos-emoji-picker-not-working-in-editor-view/4061) (thanks Luc!):

> For anyone who comes across this. I figured out a quick workaround. You have
> to open the Emoji-Picker-Keyboard on your Mac and then select the Emoji and
> pull it into the editor window with your mouse.

It works indeed!

My previous alternative was to use the emoji picker to insert an emoji in
another application (e.g. the Notes.app), and then manually cut and paste it.
