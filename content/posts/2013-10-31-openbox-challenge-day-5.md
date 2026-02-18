---
title: Openbox Challenge - Day 5
date: 2013-10-31T12:00:00-03:00
tags:
  - dev
  - legacy
---

[Previously]({{< ref "2013-10-30-openbox-challenge-day-4" >}}).

Today I removed obmenu-generator and installed archlinux-xdg-menu instead. This
one is so much better! Less bloated and more relevant. Its Arch Wiki page says
better than me. Quick command:

```bash
xdg_menu --format openbox3 --root-menu /etc/xdg/menus/arch-applications.menu >xdg-menu.xml
```

You can either choose to add it to the entire openbox menu (= replace the
current openbox menu) or add it as a menu entry to openbox. I chose the last
one, so I added

```xml
<menu id="xdg-menu" label="XDG Menu" execute="cat /var/cache/xdg-menu/openbox/menu.xml"/>
```

to my custom_menu.xml and put it in my menu.xml too. It supports icons,
out-of-the-box, and looks like the xfce menu (for example). Now, if I ever need
to update this menu again, I'll have to run my mmaker template and then add
custom_menu.xml to menu.xml. Now I'm done with menus. I'll only have to add my
favorite applications to custom_menu.xml. But this is not much essential because
I usually launch them with synapse. I think the purpose of the menu is to give a
quick overview of which applications are installed under the system; but not to
launch them. It takes time; and time costs. (Actually, maybe I'll find some
interesting pipe menus later. But I'll not cover them here, probably.)

## Windows 7 Snap feature

I've also enabled the Windows 7 Snap feature. Read the Arch Wiki. It is *much*
cool. You'll have to edit rc.xml to do this. I've also tried opensnap, but I
couldn't get it working (I'm trying these programs in a hurry, I can't try to
debug or bug report them right now. Probably I'll try them again later. When I
can't make things work at the first try, usually I manage to do it a few days
later.).

---

## Note about post length

I usually write larger posts. Explained as much as possible. But I think I won't
apply this principle to the *challenges* section anymore, because it should act
more like a diary than a tutorial (and because I can't spend much time here).
Yeah, as you can see, my first 3 posts (days) are kind of a tutorial. But I
won't do this tutorial thing anymore. This is good news for more advanced users
(I suppose), but maybe won't be much good for learners/newbies. But hey, I'm a
newbie (too) in this openbox thing now, so we'll learn together. Just try to
google my terms, I always try to be precise and name the applications as much
detailed as possible. Thank you for reading.
