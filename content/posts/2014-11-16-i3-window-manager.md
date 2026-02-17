---
title: "i3 window manager"
date: 2014-11-17T02:35:49-03:00
tags:
  - bestof
  - dev
  - legacy
---

I'm a huge fan of the [i3](<http://i3wm.org>)tiling window manager. It was the
first 'simple' window manager I tried, and it is still my favorite one. It eases
the management of your windows, is optimized for keyboard control, and maximizes
all the space you have available, thus being a nice option for laptop users. i3
is packaged for most Linux and BSD distributions. You just have to install it
through your package manager, then enjoy simplicity and agility. In this post
I'll share a couple of configurations and tweaks I use for my day-to-day
computing and programming tasks on i3. First thing: the **statusbar**. My
preferred one is [i3blocks](<https://github.com/vivien/i3blocks>). A statusbar
should be easy to config and tweak, and should not be bloated. Only the
information you really care about should be displayed on it. Colors are also
welcome, as they are a good design practice. Essential blocks include the
battery of your laptop, the system load, the current date and time, and whether
you are connected to the web or not. I also like to have a block which displays
my current network speed (download/upload) and another one for system memory and
swap. Optional things include volume and the currently playing song. Second
thing: the background of your desktop. You'll rarely see it, but it is nice to
have something other than a black background fill color. **feh** is the best
wallpaper setter for i3. A simple

    feh --bg-scale '/home/thiago/Pictures/wallpaper.jpg'

sets your background image, and creates a `$HOME/.fehbg` shell script, which you
can run to reload your wallpaper later on. Third thing: a i3lock which blurs the
current view of your desktop is very nice. I like `i3lock-wrapper` from
i3-extras repository by ashinkarov, available on
[GitHub](<https://github.com/ashinkarov/i3-extras>). There are other interesting
things there. `j4-make-config` is great for managing i3-themes, in the case you
dislike the default one. It is available on http://www.j4tools.org/. Workspace
management should be simple, so I don't use names for them. Just numbers. When
you use names, it becomes annoying when a given window is not in the proper
workspace. While you can force them to go its proper place in your i3 config
file, this process is more automatic than I need and it keeps getting in my way,
so I decided it is better not to give names to my workspaces. If you use dual
monitors, `xrandr` is your best friend. I like to have the following aliases in
my shell rc file:

    alias xrandr-t-hdmi-connect="xrandr --output LVDS1 --primary --output HDMI1 --auto --left-of LVDS1"
    alias xrandr-t-hdmi-disconnect="xrandr --output HDMI1 --off"
    alias xrandr-t-hdmi-mirror="xrandr --output LVDS1 --primary --auto --output HDMI1 --auto --same-as LVDS1"

`arandr` also helps when you need something a bit more advanced. Those set of
configs makes me happy on i3. There are several more i3 customizations you can
do, and I'll leave a couple of references here. Other ones were already
    mentioned through the post.

* https://wiki.archlinux.org/index.php/I3
* https://i3wm.org/docs/

Having a good window manager, the next step is to achieve a good shell
environment (urxvt + tmux + zsh). More on that later.
