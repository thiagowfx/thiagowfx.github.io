---
title: "atuin: limit scope to current directory"
date: 2025-12-23T12:08:44-03:00
tags:
  - dev
  - fosdem
---

[Previously]({{< ref "2025-12-01-atuin-delete-history-entries" >}}),
[previously]({{< ref "2025-11-30-atuin" >}}).

Pressing `C-r` opens the global history search by default.

To limit the history lookup to the current directory only, keep pressing `C-r`.

The scope will cycle through:

Global > Host > Session > Workspace > Directory

This makes it easier to find commands previously executed in a given directory.
