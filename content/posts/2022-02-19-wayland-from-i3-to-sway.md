---
title: "★ Wayland: from i3 to sway"
date: 2022-02-19T19:18:25-05:00
tags:
  - linux
  - bestof
---

I've been giving Wayland a try. My window manager of choice in X11/Xorg is [`i3`](https://i3wm.org/), so the natural choice in Wayland is [`sway`](https://swaywm.org/).

<!--more-->

## Intro

`sway` works well with the `i3` config out-of-the-box. A few adjustments were necessary for full compatibility. To maximize code reuse, I went with the following structure:

```shell
$ tree ~/.config/{i3,sway}
/home/typhoon/.config/i3
├── conf.d
│   └── i3.conf
└── config
/home/typhoon/.config/sway
├── conf.d
│   └── sway.conf
└── config -> ../../../i3/.config/i3/config
```

- The master config is
  [`~/.config/i3/config`](https://github.com/thiagowfx/.dotfiles/blob/master/i3/.config/i3/config).
  It is pretty standard, generated by
  [`i3-config-wizard`](https://build.i3wm.org/docs/i3-config-wizard.html) with
  a few tweaks on top for my own workflow. It works for both `i3` and `sway`.
  The config contains this snippet:

```
# Load user configs if existing. Order is important.
include conf.d/*.conf
```

The snippet allows drop-in customizations to live in `conf.d`. The `include` directive is a relatively [new](https://github.com/i3/i3/pull/4420) addition to the i3config syntax and it's the main reason this setup is elegant and minimalist.

- i3-only config options live in [`~/.config/i3/conf.d/i3.conf`](https://github.com/thiagowfx/.dotfiles/blob/master/i3/.config/i3/conf.d/i3.conf). To give you an idea of what it looks like and which options aren't compatible with `sway`, here's a snapshot of my config in early 2022:

```conf
# i3(1) only config file
# Commands herein are not compatible or interoperable with sway(1)
# Reference: https://i3wm.org/docs/userguide.html

# Autostart XDG applications (.desktop files).
# https://wiki.archlinux.org/title/XDG_Autostart
#
# Troubleshooting:
#   dex -ade i3
exec dex --autostart --environment i3

# lock screen, Ctrl+Alt+l (systemd)
exec --no-startup-id xss-lock -l -- i3lock -c 222222
bindsym Ctrl+Mod1+l exec loginctl lock-session

# XF86AudioPlayPause is not recognized by sway, add it only to i3
# https://github.com/swaywm/sway/issues/4783
bindsym XF86AudioPlayPause exec playerctl play-pause

# show window title icon
for_window [all] title_window_icon on

set $bgcolor #526532
set_from_resource $black i3.color0
set_from_resource $red i3.color1
set_from_resource $green i3.color2
set_from_resource $white i3.color7
set_from_resource $gray i3.color8

# Theme colors
client.focused $bgcolor $bgcolor $white $green
client.focused_inactive $gray $gray $black $gray
client.unfocused $black $black $gray $black
client.urgent $red $red $white $red

# Start i3bar to display a workspace and status bar
bar {
    status_command i3status
    position top
    workspace_min_width 25

    colors {
        background $black
        statusline $white

        focused_workspace $bgcolor $bgcolor $white $black
        active_workspace $gray $gray $black $gray
        inactive_workspace $black $black $gray $gray
        urgent_workspace $red $red $white $green
    }
}

# restart i3 inplace (preserves layout/session, can be used to upgrade i3)
bindsym $mod+Shift+r restart

# vim: ft=i3config
```

It's possible some of these configs will become compatible with `sway` over time, but at the time of this writing they are not.

- sway-only config options live in [`~/.config/sway/conf.d/sway.conf`](https://github.com/thiagowfx/.dotfiles/blob/master/sway/.config/sway/conf.d/sway.conf). To give you an idea of what it looks like and which options aren't compatible with i3, here's a snapshot of my config in early 2022:

```conf
# sway(1) only config file
# Commands herein are not compatible or interoperable with i3(1)
# References:
#   sway(5)
#   https://github.com/swaywm/sway/wiki
#   https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway

# HiDPI
output "*" scale 1.5

# Wallpaper
output "*" bg ~/.wallpaper fill

# Gaps a la i3-gaps
gaps inner 10

# XF86AudioPlayPause is not recognized by sway: xmodmap -pke | grep XF86AudioPlay
# https://github.com/swaywm/sway/issues/4783
bindcode 172 exec playerctl play-pause

# Start i3bar to display a workspace and status bar
bar {
    status_command i3status
    position top
    workspace_min_width 25
}

# restart i3 inplace (preserves layout/session, can be used to upgrade i3)
bindsym $mod+Shift+r exec sway reload

# vim: ft=i3config
```

Most of those are wayland-specific options.

## Quirks

`gaps` is available in `i3` as well but only if you use
[`i3-gaps`](https://github.com/Airblader/i3), which generally I refuse to in
order to stay closer to vanilla/upstream `i3`.

The `play-pause` multimedia key is
a [bug](https://github.com/swaywm/sway/issues/4783) I found on `sway`. It's quite
annoying, the workaround as you can see above is to use `bindcode` instead of
`bindsym`. For more details see the bug.

In general `sway` works very well out-of-the-box so long as you install
[XWayland](https://wayland.freedesktop.org/xserver.html) (`xorg-xwayland` on
Arch Linux). XWayland **transparently** proxies X11 apps to a X11 server that
runs inside wayland.

It's possible to detect those apps by running
[`xprop`](https://www.x.org/releases/X11R7.5/doc/man/man1/xprop.1.html) and
trying to click a window: If you cannot do it, then the window is not a X11
app. Alternatively
[`xeyes`](https://unix.stackexchange.com/questions/162769/what-is-the-purpose-of-xeyes)
is another way to detect them.

To achieve a 100% Xorg/X11-free experience with pure wayland, just add
`xwayland disable` to the `sway` config. I wouldn't recommend that though, most
Linux GUI apps aren't Wayland ready and will probably never be. To put it
another way, X11/Xorg will take a long time (if ever) to disappear the same way
that IPv4 will take a long time (if ever) to let IPv6 completely replace it.
That's life.

X11 apps look a bit blurry in a 4K monitor with scaled DPI (>96) when they run
inside Wayland with XWayland. I am not particularly bothered by that, but it's
noticeable.

There's no need to replace all of your small `i3` Xorg utilities with wayland
ones. For example, [`rofi`](https://github.com/davatorium/rofi) (application
launcher) works just fine (no need for `wofi`). The stock `i3` bar (`sway` bar?)
works just fine, there's no need for `polybar` or `waybar`.

Some utilities need to be replaced though. For example, `dunst` (notification
daemon) does not seem to work with `sway` out-of-the-box, `mako` seems to be a
recommended replacement. `i3lock` (lock screen) also does not work, `sway`
comes with its own screen lock directives. Screenshotters (e.g. `scrot`) will
also need to be replaced.

The system tray does not seem to work fine out-of-the-box. I haven't
investigated much to figure out what's wrong with it.

I was looking for a display manager that works well with both X11 and Xorg and
ended up trying [`greetd`](https://git.sr.ht/~kennylevinsen/greetd),
[`emptty`](https://github.com/tvrzna/emptty/) and
[`ly`](https://github.com/fairyglade/ly), in that order. `ly` is in my opinion
the best one in terms of balancing simplicity and usefulness.

`sway` / `XWayland` doesn't source `~/.Xresources`. This is an issue if you
rely on customizations therein. It does source `~/.Xdefaults` though!
Leveraging this, I did the following changes:

- (i) `~/.Xresources` sources `~/.Xdefaults`:

```shell
$ cat ~/.Xresources
! These settings apply to X11 only.
! Use ~/.Xdefaults for settings that apply to both X11 and Wayland (xorg-xwayland).
#include ".Xdefaults"

! Source:
!   xrdb -merge ~/.Xresources
!
! Dump all properties:
!   xrdb -q
!
! Check if DPI is set:
!   xrdb -q | grep -i dpi

! HiDPI
! Common values:
!   96  (x1.0, baseline)
!   144 (x1.5)
!   192 (x2.0, HiDPI)
*.dpi: 144
```

- (ii) `~/.Xdefaults` holds my customizations that originally lived in `~/.Xresources`:

```shell
$ cat ~/.Xdefaults
! These settings apply to both X11 and Wayland (xorg-xwayland).
! Use ~/.Xresources for X11-only settings.

Xft.antialias: true
Xft.hinting: true
...
```

In principle I could just have symlinked them:

```shell
$ ln -s ~/.Xresources ~/.Xdefaults
```

The reason why I didn't do it is to avoid double scaling (DPI). You see, my
`sway` config already sets DPI / scaling to 1.5x. If we do that in
`~/.Xdefaults` as well then Xorg applications would have been scaled twice.

## Closing remarks

In general Wayland / `sway` works reasonably well out-of-the-box in 2022, but
tiny adjustments are still necessary, and it isn't as polished as it could have
been. Furthermore, my workflow is very simple. Try sharing your screen in a
video call in Wayland and you'll run into other quirks. I have mixed feelings
and wouldn't necessarily recommend it. I wouldn't give an anti recommendation
either. It's complicated...even though Wayland is supposed to overcome some X11
/ Xorg limitations, as a client and without knowing its internals I fail to see
its advantages.