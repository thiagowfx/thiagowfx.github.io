
**TIL**: A few keybindings from [Ghostty](https://ghostty.org/). Assuming macOS.
This list contains the keyboard shortcuts I tend to use weekly (or daily). No
point in including an exhaustive list.

- `Cmd + d`: split right
- `Cmd + Shift + d`: split down
- `Cmd + Shift + p`: command palette[^1]
- `Cmd + Shift + Enter`: toggle (split) zoom (comparable [to](https://superuser.com/questions/238702/maximizing-a-pane-in-tmux) `prefix + z` in `tmux` a.k.a. `resize-pane`)
- `Cmd + Enter`: toggle fullscreen (at the system window manager level)
- `Cmd + 1`, `Cmd + 2`, etc: switch terminal tabs
- `Cmd + Shift + {` / `Cmd + Shift + }`: cycle through tabs backwards / forward
- `Cmd + Shift + [` / `Cmd + Shift + ]`: cycle through splits backwards /
  forward
- `Cmd + .`: open Ghostty config
- `Cmd + t`: open new tab
- `Cmd + w`: close current tab
- `Cmd + n`: open new window

I found these defaults to be quite sensible.

The only added customization that I really occasionally use is this:

```
keybind = global:cmd+;=toggle_quick_terminal
keybind = global:cmd+shift+;=toggle_quick_terminal
```

...to toggle the quick terminal ([previously]({{< ref "2025-11-27-ghostty-quick-terminal" >}})).

[^1]: After 1y using Ghostty, only now have I figured it out it has a command
    palette!

