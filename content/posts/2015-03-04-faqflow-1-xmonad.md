---
title: "[FAQFlow #1]: XMonad"
date: 2015-03-04T21:45:47-03:00
tags:
  - dev
  - legacy
---

**WTF is a FAQFlow?** See the footnotes at the end of this post.

**XMonad** is a window manager for Unix systems written in Haskell. This is an
introductory post on how to use it.

## Getting started

First, install XMonad. You can either install it manually or use your system's
package manager.

If you're using X11 with a display manager, proceed normally. If you don't use a
DM, put this at the end of your `~/.xinitrc`:

```shell
exec xmonad
```

Now run `startx`.

## Common questions

### 1. XMonad is lightweight but GHC (Haskell compiler) is way too big (>400MB+). Do I really need it?

Yes, if you really want to get the most out of xmonad. This is part of the game.
If you already use Haskell, this won't be a problem. Otherwise, read about GHC
in "The Architecture of Open Source Applications"—there's a good reason it's
that big.

### 2. I just started xmonad. But there is nothing on my screen—it's blank all over the place

This is normal. XMonad is lightweight! There's nothing fancy getting in your
way. If you think there should be lots of widgets and desktop icons, maybe you
should start with an easier tiling window manager first. i3 is a good choice.

### 3. How do I open a terminal?

`Mod+Shift+Enter`. Mod is usually Alt, but can be changed to the Windows key
later.

## Bootstrapping

Now you have a terminal. What's next?

### How to change workspaces?

Yes, xmonad has workspaces: `Mod-1`, `Mod-2`, etc.

### How to change layouts?

`Mod-Space`. It cycles through the three default available layouts.

### I don't like xterm! It's way too ugly! Can I change the default terminal emulator?

Yes! Create a config file at `~/.xmonad/xmonad.hs`:

```bash
mkdir ~/.xmonad
cd ~/.xmonad
vim xmonad.hs
```

Add this:

```haskell
import XMonad

main = xmonad default Config
  {
  -- set your terminal. Examples: konsole, gnome-terminal, urxvt
  terminal = "urxvt"
  }
```

Lines beginning with `--` are comments. Change "urxvt" to your favorite terminal
emulator and run:

```bash
xmonad --recompile
```

This makes GHC compile your xmonad.hs. Do `ls` now and you'll see the compiled
results (assuming compilation succeeded).

Now restart xmonad:

```bash
xmonad --restart
```

Close your current terminal and open a new one (`Mod-Shift-Enter`). Done—now you
have a pretty terminal!

This post will have a continuation.

## Footnotes

- **FAQFlow**: A new way to document and teach introductory skills or tutorials.
  The word is a portmanteau of "FAQ" (frequently asked questions) and
  "workflow".
- Customizing xterm: You can customize `~/.Xresources` to get a nice-looking
  xterm, but most people either don't know what a Xresources file is or don't
  bother creating one.
