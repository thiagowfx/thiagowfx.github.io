
[Previously]({{< ref "2013-10-27-openbox-challenge-day-1" >}}).

Today, the first thing I did was to create my openbox config folder. Next, I
modified the autostart file. Basically all I had to do was to copy some of the
contents of my startup file from Fluxbox (`~/.fluxbox/startup`) to this one. I
only removed **batterymon** from it, since tint2 already has its own battery
indicator.

## Wallpaper

So, let's modify the default wallpaper. I usually go to http://wallbase.cc/ to
choose a new one. The keyword "abstract" (or "abstraction") is a good one. I
searched for "keep it simple" and liked [this one](http://wallbase.cc/). To set
the wallpaper, `fbsetbg /path/to/wallpaper.jpg` is sufficient. I've put this
line in the autostart file. Another option would be to use **feh**.

## Theming

To set a GTK theme, **lxappearance** is a good start. It is a GUI config tool,
so it should be pretty straightforward. I like the elementary OS one (for the
iconset and the widget style). For the (mouse) cursor, xcursor-aero from the AUR
is nice. For the fonts, I like Droid Sans (from Android). But I had to install
**gtk-chtheme** to change it (lxappearance doesn't seem to have this option). It
is a GUI too. We could edit `~/.gtkrc-2.0` by hand too, but I find this
unnecessary here.

Next thing was to search a theme for openbox itself. Box-look contains several
ones. But hey, I'm using Arch, so let's do it in the arch way. The package
**openbox-themes** from the official repos is a good start. Also, I've found the
**obtheme** utility from Xyne repo (it is in the AUR too). It is a
python-written GUI, so it should be pretty intuitive too. Hit Control-P (or
activate Theme > Preview Mode) then double click in each theme to have a taste
of them. I liked a dark one called "Carbon". I had some trouble with this
program, not sure why. But use **xkill** if you ever need to kill it.

To effectively apply the theme, use **obconf** (available in the official
repos). This is an amazing (GUI) tool. Actually, I found it better than
**obtheme**. There are several options to tweak there. I like to enable the
'focus window with the mouse' behavior. It saves a lot of clicks sometimes.
Another good tweak is to enable a margin of 1px size (for example, on the left).

Next I installed **plank** (the simplest dock you'll ever find out there) from
the AUR and moved tint2 panel to the top. You can do the latter with
**tint2conf**. It looks a good rule to let its width be 99%, so there will be a
tiny space on top left (or top right) corner, where you can right click to
access the openbox menu (this could be achieved with a margin too, like I said
before). You could enable the 'autohide' option from here too (I dislike it).
I've also changed the clock format.

## Menu editing

Just to finish this day, let's edit the menu. The first tool I've found for that
was **menumaker** (in the official repos), but it didn't look so intuitive.
First, there is no such a "menumaker" command. The right command is **mmaker**.
Also, there is no man page for it; but fortunately the Arch Wiki contains a
little description about it (later I've found `mmaker --help`).

This looks sufficient for today.

## Tomorrow plans

- Add all of my openbox (and tint) configs to my **Github**. _Maybe_ set a cron
  job to automatically update (push) them. I'm not sure if I will create a new
  repo or use my existing one, "dotfiles". Also, I'm not sure how to link the
  openbox files to this repo. The easiest way I know to do that is to manually
  link (`ln -s`) all the files I want, but this is not much elegant.
- Create some custom menu entries (maybe with **obmenu**?)
- Read the Arch Wiki a little more.

I followed mainly the Arch Wiki and some recommendations on reddit and in the comments of my previous post to create this guide for day 2. Here is a screenshot of today:

![Openbox desktop screenshot day
2](http://farm6.staticflickr.com/5477/10541670586_d486dc4ea5_o.png)

