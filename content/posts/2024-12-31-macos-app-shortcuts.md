---
title: "macOS app shortcuts"
date: 2024-12-31T22:26:00-03:00
tags:
  - dev
---

Let's say you want to assign a keyboard shortcut within a given app to invoke a
menu item.

To illustrate: Assume that you want to map `Cmd + Shift + X` within `Logseq.app`
to "paste and match style".

[Apple Docs](https://support.apple.com/en-ca/guide/mac-help/mchlp2271/mac):

> On your Mac, choose Apple menu > System Settings, click Keyboard in the
> sidebar (you may need to scroll down), then click Keyboard Shortcuts.
>
> Select App Shortcuts on the left, click the Add button, click the Application
> pop-up menu, then choose a specific app or All Applications.

Choose `Logseq.App`.

> In the "Menu title" field, type the menu command for which you want to create
> a shortcut, exactly as the command appears in the app, including the >
> character (type ->), ellipses (type three periods without spaces), or other
> punctuation.
>
> For example, to set a shortcut for the default ligature command in TextEdit
> (Format > Font > Ligatures > Use Default), type Format->Font->Ligatures->Use
> Default in the "Menu title" field. To set a shortcut for the Export as PDF
> command (File > Export as PDF…), type File->Export as PDF… in the field.

Type in `Edit->Paste and Match Style`, case sensitive, no spaces around the ` ->
`.

> Click in the "Keyboard shortcut" field, press the key combination that you
> want to use as the keyboard shortcut, then click Done.

**Note**: This method doesn't work if the keyboard shortcut is already mapped within the
app.

Credits to [David Winterbottom](https://til.codeinthehole.com/posts/how-to-bind-custom-keyboard-shortcuts-to-nested-macos-menu-options/) for the idea.
