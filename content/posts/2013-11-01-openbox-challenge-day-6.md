---
title: "Openbox Challenge - Day 6 - Now with XFCE / goodbye"
date: 2013-11-01T12:00:00-03:00
tags:
  - dev
  - legacy
---

[Previously]({{< ref "2013-10-31-openbox-challenge-day-5" >}}).

Now I'm writing my posts in Markdown @ Emacs. I hope this makes me save some
time (it saved today). Wordpress is kinda distracting. Today we had big changes.
Maybe extra big ones. First, let's begin with the minor ones:

1. I've added some custom hotkeys to my rc.xml. These are openbox commands in
   essence. I intend to use another tool to launch programs.
2. I've runned **qtconfig-qt4** to make my QT applications look like GTK ones.
3. I've switched **pnmixer** for **volumeicon**. Now my laptop audio hotkeys
   work!
4. I've reinstalled batterymon.
5. I replaced my tint2 panel for **xfce4-panel**.

## Now I'll use XFCE

Install XFCE(4):

```bash
sudo pacman -S xfce4
```

Change `~/.xinitrc` to start XFCE:

```bash
#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)
if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# set the X cursor
xsetroot -cursor_name left_ptr

# set Brazilian keyboard layout
setxkbmap -layout br

# xinit window_manager
case $1 in
  gnome) exec gnome-session;;
  kde) exec startkde;;
  awesome) exec awesome;;
  fluxbox) exec startfluxbox;;
  openbox) exec openbox-session;;
  xfce|*) exec startxfce4;;
esac
```

To use XFCE with Openbox, run `openbox --replace` while in a xfce session. You
can continue from here, but I won't. I'll stick to XFCE for a while. This means
I'll try the Xfwm4 WM.

Notice I haven't said how much time this challenge would last. I preferred to
pick none (aka "30 days", for instance). So I'm stopping this here. I hope you
liked this mini journey.

---

## Final notes

Openbox was my first 'challenge'. Probably I'll continue this **challenges**
series with another thing. Maybe a programming language, maybe another WM, or
even a new IDE or distro. I'm not sure. But I think this is useful: for me, I
can fix more these concepts and have the opportunity to train my english and to
share some knowledge; for you, you can have a broad vision of a specific subject
(in this case, openbox) and maybe learn or become interested about something.

Now, my final review: I liked openbox more than fluxbox. I would say fluxbox is
easier to configure, but openbox kind of integrates better with any DE (or even
by itself) and... bah, it is nice!!

I would say there is at least four categories of DE/WM (I prefer the bold ones):

- The heavily ones: gnome, kde, **cinnamon**, unity
- The balanced ones: **xfce**
- The lightweight ones: fluxbox, **openbox**, blackbox
- The power user ones: **awesome**, **i3**, xmonad, dwm (actually, never tried
  any of these)

If I ever need to run **X(org)** under a server (some people like it), I would
choose openbox as my primary WM. I would feel very comfortable using it. I won't
delete my openbox repo (although it's pretty small), but I won't update it
(anymore) either.

## Further resources

- https://wiki.archlinux.org/index.php/Openbox
- https://wiki.debian.org/Openbox
- https://en.wikipedia.org/wiki/Openbox
- https://help.ubuntu.com/community/Openbox
- http://openbox.org/wiki/Configuration
- http://urukrama.wordpress.com/openbox-guide/
- http://www.gentoo.org/doc/en/openbox.xml

Thank you for reading.
