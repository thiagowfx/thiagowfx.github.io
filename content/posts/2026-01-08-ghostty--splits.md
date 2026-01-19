---
title: "ghostty: splits"
date: 2026-01-08T12:28:27-03:00
tags:
  - dev
  - ghostty
  - macos
---

[Previously]({{< ref "2025-07-21-ghostty-migrating-config-to-dotfiles" >}}).

The best quality-of-life improvement for Ghostty I added in 2025[^1]: add the
following keybindings to your Ghostty config:

```
# native: Cmd + Shift + d
keybind = cmd+shift+-=new_split:down
# native: Cmd + d
keybind = cmd+shift+|=new_split:right
```

Now you can split your terminal to the right and to the bottom with keyboard
shortcuts.

Previously I was using the mouse to do so (right click + split).

[^1]: Unless you count [eye-candy]({{< ref "2025-11-30-ghostty-shaders" >}}) as
    a QoL improvement :)
