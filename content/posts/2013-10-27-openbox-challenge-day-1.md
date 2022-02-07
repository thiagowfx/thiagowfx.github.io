---
title: "Openbox Challenge – Day #1"
url: 'openbox-challenge-day-1'
date: 2013-10-28T02:12:15+00:00
tags:
  - classics
  - challenge
  - linux
---

**Note:** I am sorry but the openbox repository I created for this challenge doesn't exist anymore. But you can still read the challenge, there is some relevant information out there.

I chose to start this new 'challenges' series with the [openbox](http://openbox.org/) window manager. I'm not sure if I will continue this project, but I'll try to. Also, you'll notice I'm writing all of my posts in English, from now on.

So, this will be a both a big review and a opportunity to describe how pleasant &#8212; or painful &#8212; a life with this WM can be.

<!--more-->

For starters,

```shell
# install openbox from Arch repos
$ sudo pacman -S openbox

$ emacs -nw ~/.xinitrc  
# add the following line to my session chooser:
openbox) exec openbox-session;;

# start X  
xinit openbox  
```

Then I notice I got a completely blank screen. Hum...I'm likely in the right way. A quick right click in the darkness shows the classic openbox menu. It is very similar to the fluxbox one which I'm used to.

The first thing I did was to install the **tint2** panel. It is really simple and fits well with the openbox philosophy and look & feel.

The first thing I did later was to open the **tint2conf** program, then added the battery indicator to the tint panel.

My startup programs I'm used to simply don't start automagically anymore. I'll have to figure out how to add them to the openbox startup file (this is pretty easy, I guess, but I'll do it tomorrow).

I've launched a **Konsole** window from the menu (because this was the only terminal emulator in the list that I had installed). Usually I launch **lxterminal**, but it wasn't there (not yet).

From there, I've used **fbrun** (from Fluxbox) to launch some utilities, like `firefox`, `netbeans` and other stuff I'm using now.

I've got myself comfortable in this process. I have so much to work (and figure) out there, but I think I'll like openbox.

Tomorrow plans:

  * customize my startup file
  * customize the wallpaper (because a completely black one sucks)
  * apply my GTK themes to openbox (or find a new one)

~~As a bonus, here is a screenshot (got with **scrot**):~~

~~(OK, the background is not _really_ black: compare the 'blackness' of Konsole to it. But it is dark =p)~~