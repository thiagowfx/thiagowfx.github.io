---
title: "Here be dragons! Free BSD Overview (part I)"
date: 2014-07-20T12:00:00-03:00
tags:
  - bestof
  - dev
  - legacy
---

## Overview

I'm done with Linux distros, and you probably already know that; I have a list
of them for servers and desktop use cases, and they cover almost everything I'll
ever need. So I don't bother testing new distros anymore, especially when
possessing Arch Linux, Vagrant, Docker and VirtualBox. Oh, together they are all
nice swiss army knives. So, what about other components of the \*nix world?
There are the Apple World and the \*BSD World. I plan to explore both of them in
the future, beginning with FreeBSD.

I know there are a couple of BSDs out there, from the top of my head I can list
OpenBSD (security oriented thing I believe), DragonFly BSD, NetBSD and PC-BSD
(desktop use). I have no clue what is the difference between them, but I believe
testing only one of them is sufficient. Let's get it. Heading to
http://www.freebsd.org/where.html, I choose the amd64 row of the tenth release.
Next comes a FTP listing where I can choose a download file. There are: bootonly
(1), disc (2), dvd (3) and (4) memstick. (4) is for using with dd to write to a
USB stick. This is nice, I don't usually find this thing explicitly on Linux
Distros download pages (however IIRC, dd is the official method of writing Arch
to a USB stick, and dd'ing the openSUSE ISO image usually works flawlessly too).
(3) probably contains a lot of unnecessary stuff and (1) is probably excessively
lightweight. So I chose (2), the disc option.

After downloading it, I chose to test it with VirtualBox. Current release on my
Arch system is 4.3.14. I create a new virtual machine optimized for BSD from the
wizard page, then choose the ISO I just download and boot it. The installation
process proved to be relatively straightforward. It is ncurses-based, and the
options you are prompted to enter are exactly what you would expect from a
pretty traditional unix system. One remarkable option is that I could choose to
have a `ZFS` filesystem. Linux systems usually don't allow that easily due to
license reasons.

A confusing thing was about the keyboard/locale config. It isn't traditional. I
would expect to have options such as `pt_BR`, `en_US`, `en_CA`, `fr_FR`, and so on, but
there are not. In the testing area of the keyboard, I couldn't enter the 'á'
character, with any of the Brazilian/Portuguese keyboard options. Another
downside: the shell. Default options were `sh`, `csh` and `tcsh`. REALLY? Where are
the 'traditional' shells, such as `bash`, `zsh`, `dash` (debian), `fish`…(?) The shell
will be the first program I'm going to install.

After the installation, I wasn't able to identify the bootloader. It didn't look
like GRUB or syslinux, so I believe it is something specific to \*BSDs. I'm a
Linux guy, so the first things I tried after logging into the system (as root,
of course) was to inspect which commands were available. Most of what I'm used
to were. This is one advantage of using a Unix systems: there is much in common
between Linux and BSDs. Of course, I'm not being 100% precisely here, since
Linux is only the kernel (what I'm referring to as Linux is actually GNU/Linux).
I entered `vi`. Shame on me. I took a while to find the ':' key to quit from it.
I've just discovered my keyboard wasn't properly set up, despite of my Brazilian
choice at the installation. `loadkeys` wasn't available either. But I can live
with that, for now.

## Important links

- http://www.freebsd.org/projects/newbies.html
- http://svnweb.freebsd.org/ (source code, distributed in a subversion repository)
- http://forums.freebsd.org/ (BBS)
- http://www.freebsd.org/projects/index.html
- http://www.freebsd.org/docs.html (official documentation)
- https://wiki.freebsd.org/ (moinmoin based)
- https://wiki.freebsd.org/Pkg Primer
- http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/ports.html
- http://www.freebsd.org/ports/index.html (ports (software) web search)
- http://www.hypexr.org/freebsd_ports_help.php (best resource about learning how to manage packages in FreeBSD)

You see, once with the system up and running, it is necessary to do a lot of
reading to understand what is going on behind the scenes. Those links might help
you as they helped me. I'm stopping here for now. Part II should cover package
management and more criticism about this system (maybe I might find something
useful and/or good there too, I'm not that biased (for now)). There are several
questions which still need an answer.

Before leaving, I've done `pkg install bash` then `pkg info` to check if
everything went fine. Default bash binary was put into `/usr/local/bin`. I really
dislike to have several binary folders (`/bin`, `/sbin`, `/usr/bin`, `/usr/sbin`,
`/usr/local/bin`, `/usr/local/sbin`), this is so non-intuitive (do I have to say
that Arch unified almost all of those, and Gentoo deals with them in an elegant
way?). Also, did you believe that I had to mount something to `/dev/fd` in order
to use bash? And I had to add an entry in `/etc/fstab` to make it permanent too.
What the hell?! (You see…hell, BSD logo…can't believe I made this joke. OK, till
next time!) (There is also an album available on Flickr with some screenshots of
the installation process. It might be deleted or cluttered with other
screenshots later on.) Second part of this series is part II.
