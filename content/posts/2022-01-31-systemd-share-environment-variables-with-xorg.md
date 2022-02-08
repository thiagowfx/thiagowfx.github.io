---
title: "Systemd: share environment variables with xorg"
date: 2022-01-31T21:38:54-05:00
tags:
  - linux
---

In this post we will learn how to share environment variables (e.g.
`$GDK_SCALE`) between a system user session and X11/Xorg.

<!--more-->

The typical [`~/.xinitrc`][xinitrc] and/or [`~/.xprofile`][xprofile] setup in
2020s involves some environment variable exports such as the following:

```shell
# fix java application decorations, for tiling window managers
export _JAVA_AWT_WM_NONREPARENTING=1

# make Chrome pick up proxy settings stored in gconf
export DESKTOP_SESSION=gnome

# HiDPI settings for GTK3+
export GDK_DPI_SCALE=0.5
export GDK_SCALE=2

# HiDPI settings for QT
export QT_FONT_DPI=192
```

This particular set of customizations stems from my [dotfiles][dotfiles] but
there isn't anything special about it. I'll include an explanation anyway for
completeness:

- The java setting is meant for launching certain java-based applications from
  within a tiling window manager.

- All the other settings are meant for 4K HiDPI displays. The baseline DPI is
  96, which is too small for 4K monitors, the fonts and icons all look tiny. In
  order to make them scale it's necessary to use a higher DPI. Typical setups
  use either 144 (x1.5) or 192 (x2.0), the bigger the DPI the bigger fonts and
  icons will appear in the screen.

Those exports work well for graphical applications launched from your favorite
window manager after it has already started, however if you decide to launch an
application from `systemd`, those settings will not be picked up by it.

For example, if you decide to manage [`redshift`][redshift][^1] (more
specifically, `redshift-gtk` which has a system tray app) from a systemd user
session[^2], its fonts will look small.

There are several ways to address this issue.

One of them is to edit the service file directly:

```shell
$ systemctl --user edit redshift-gtk
```

And then add:

```
[Unit]
Environment=GDK_SCALE=2 GDK_DPI_SCALE=0.5
```

Which results in:

```shell
$ cat ~/.config/systemd/user/redshift-gtk.service.d/override.conf
[Unit]
Environment=GDK_SCALE=2 GDK_DPI_SCALE=0.5
```

Which you can make effective by:

```shell
$ systemctl --user daemon-reload
$ systemctl --user restart redshift-gtk
```

I am not a fan of this approach though, because this step would need to be repeated
to all service files you want to manage this way. There's a better, [DRY][dry] way to
do so.

`systemd` supports [environment
files](https://www.freedesktop.org/software/systemd/man/environment.d.html)
(`environment.d(5)`). User-defined ones live in
`~/.config/environment.d/*.conf` by default.

This means we could produce the following file:

```shell
$ cat ~/.config/environment.d/user.conf
# systemd environment.d(5) EnvironmentFile
# https://www.freedesktop.org/software/systemd/man/environment.d.html
#
# Do not use export here.
#
# Alternatively
#   systemctl --user import-environment [var1] [var2] [...]
#
# Troubleshooting
#   systemctl --user show-environment

# fix java application decorations, for tiling window managers
_JAVA_AWT_WM_NONREPARENTING=1

# make Chrome pick up proxy settings stored in gconf
DESKTOP_SESSION=gnome

# HiDPI settings for GTK3+
GDK_DPI_SCALE=0.5
GDK_SCALE=2

# HiDPI settings for QT
QT_FONT_DPI=192
```

Which is applied to all systemd user service files automatically, no need to
set `Environment=` manually everywhere.

However, now we need to maintain two different files: the systemd `.conf` one
and the xorg `~/.xinitrc` one.

One elegant way to reduce maintenance burden is, in my opinion, the follownig:

```shell
$ cat ~/.xinitrc
...
# Parse user session environment variables.
# This file is shared with the systemd user instance.
# Export all variables: https://stackoverflow.com/a/30969768/1745064
set -a
[ -r ~/.config/environment.d/user.conf ] && . ~/.config/environment.d/user.conf
set +a
```

It does what you expect: the underlying shell sources the `*.conf` file as if
you were `export`ing each variable therein.

One caveat of this setup is that you cannot define the variables
dynamically; for example, with subshells, with external programs, or with
simple mathematical operations derived from other variables[^3].

Ultimately though you end up with only one file to manage, which is the systemd one.
[KISS][kiss]™.

{{< figure align="center" src="https://imgs.xkcd.com/comics/x11.png" link="https://xkcd.com/963/" alt="Thomas Jefferson thought that every law and every constitution should be torn down and rewritten from scratch every nineteen years--which means X is overdue." attr="XKCD Courtesy of Randall Munroe" >}}


[dotfiles]: https://github.com/thiagowfx/.dotfiles
[dry]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
[kiss]: https://en.wikipedia.org/wiki/KISS_principle
[redshift]: http://jonls.dk/redshift/
[xinitrc]: https://wiki.archlinux.org/title/Xinit
[xprofile]: https://wiki.archlinux.org/title/Xprofile

[^1]: Redshift adjusts the color temperature of your screen according to your
  surroundings. This may help your eyes hurt less if you are working in front
  of the screen at night. Redshift is similar to [f.lux](https://justgetflux.com/).
[^2]: `systemctl --user start redshift`.
[^3]: For example, `QT_FONT_DPI=$(($GDK_SCALE * 96))` or similar.
