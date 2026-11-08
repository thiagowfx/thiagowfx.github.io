---
title: "maccy: pinned items instead of private espanso snippets"
date: 2026-11-08T13:54:05+00:00
tags:
  - bloggify
  - dev
  - macos
---

[Previously]({{< ref "2025-03-24-maccy-pin-items" >}}).

**Problem statement**: keep frequently accessed private snippets handy
_without_ maintaining a separate [Espanso]({{< ref
"2025-05-16-espanso-hello-world" >}}) config.

Use [Maccy](https://maccy.app/) pinned items instead. I already use it as my
clipboard manager. For fixed text I need to paste often, a pinned entry is
enough.

The [workflow](https://github.com/p0deje/Maccy#usage):

1. Copy the snippet.
2. Open Maccy and highlight its clipboard entry.
3. Press `⌥P` to pin it.

The entry stays at the top of the list and gets a permanent keyboard shortcut.
Press `⌥P` again to unpin it. Clearing unpinned history leaves pinned entries
in place.

In the previous post, I treated pins as temporary and text expansion as the next
step for semi-permanent snippets. It turns out that distinction isn't absolutely
necessary. Frequently pasted text doesn't always need a trigger or a YAML file.

Espanso still makes sense for typed triggers and dynamic replacements. For a few
static snippets meant to be private (e.g. phone number), Maccy is enough. One
fewer private config to maintain.
