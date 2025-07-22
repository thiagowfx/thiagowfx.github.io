---
title: "Ghostty: migrating config to dotfiles"
date: 2025-07-21T14:56:27+02:00
tags:
  - dev
---

[This year]({{< ref "2024-12-28-ghostty" >}}) I migrated my terminal
application from [iTerm2](https://iterm2.com/) to
[Ghostty](https://ghostty.org/) on macOS.

Ghostty has great defaults; I find that there are only a handful of
customizations that I need to make to satisfy my needs.

One can configure ghostty by opening its config file with `Cmd + ,`, the typical
preferences shortcut on macOS.

In a vanilla system, that config file is initially `$HOME/Library/Application\
Support/com.mitchellh.ghostty/config`
([docs](https://ghostty.org/docs/config#macos-specific-path-(macos-only):)).

That location is not convenient / accessible though.

Upon digging the [ghostty config docs](https://ghostty.org/docs/config):

```
$XDG_CONFIG_HOME/ghostty/config.
if XDG_CONFIG_HOME is not defined, it defaults to $HOME/.config/ghostty/config.

macOS-specific Path (macOS only):
$HOME/Library/Application\ Support/com.mitchellh.ghostty/config
macOS also supports the XDG configuration path mentioned above.
```

I prefer the `~/.config/ghostty` location: it is cross-platform, compatible with
Linux as well, and I can easily add it to my
[dotfiles](https://github.com/thiagowfx/.dotfiles/blob/master/ghostty/config).

Moving the file to that location yields a no-frills migration:

```shell
% mv $HOME/Library/Application\ Support/com.mitchellh.ghostty/config $HOME/.config/ghostty/config
```

As of today, the config looks like this:

```
# https://ghostty.org/docs/config
# keep-sorted start
cursor-style-blink = false
keybind = shift+enter=text:\n
macos-icon = chalkboard
shell-integration-features = no-cursor
theme = catppuccin-macchiato
# keep-sorted end
```

The first line is a handy shortcut to the config documentation.

The [`keep-sorted`](https://github.com/google/keep-sorted) stanzas stem from my
tendency to keep the house tidy. They are not merely comments: the sorting is
actually enforced via a git [pre-commit](https://pre-commit.com/) hook.

`cursor-style-blink = false`: blinking cursor is unnecessarily distracting.

`keybind = shift+enter=text:\n`: [Claude Code](https://www.anthropic.com/claude-code) added this, it's [surprising](https://github.com/ghostty-org/ghostty/discussions/7780) it's not the default:

```
[...]
│ > /termi                                                     │
───────────────────────────────────────────────────────────────╯
  /terminal-setup   Install Shift+Enter key binding for newlines
```

`macos-icon = chalkboard`: bells and whistles.

`shell-integration-features = no-cursor`: some
[context](https://github.com/ghostty-org/ghostty/discussions/2812#discussioncomment-11686920).

`theme = catppuccin-macchiato`: more bells and whistles. You may like: `ghostty
+list-themes`.
