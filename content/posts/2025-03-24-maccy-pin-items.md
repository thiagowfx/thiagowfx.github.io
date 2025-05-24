---
title: "maccy: pin items"
date: 2025-03-24T13:21:46+01:00
tags:
  - dev
---

[Previously]({{< ref "2023-12-02-maccy-macos-clipboard-manager" >}}).

Sometimes it's useful to have certain code snippets be easily accessible from
the clipboard manager.

As I use [Maccy](https://github.com/p0deje/Maccy), I figured I should leverage
its built-in pinning feature to do so.

It's not intuitive [how to do
it](https://github.com/p0deje/Maccy?tab=readme-ov-file#usage):

- first, focus an existing clipboard entry
- then press `OPTION (⌥) + P` ("p" for "pinning")

> The item will be moved to the top with a random but permanent keyboard
> shortcut. To unpin it, press `OPTION (⌥) + P` again.

**Pros**:

- no need to keep a text editor (or notes app) opened with temporary clipboard
  contents to keep copying from (=less overhead)
- no need to keep digging the clipboard manager history to find the same entry
  over and over again

This workflow is decent for temporary entries.
For semi-permanent ones, I should
look into [Espanso](https://espanso.org/) at some point. For now, [Raycast
Snippets]({{< ref "2025-01-29-raycast-snippets" >}}) fills in this role.
