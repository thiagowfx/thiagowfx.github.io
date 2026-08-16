---
title: "Wrapping up -- FreeBSD Overview (Part V / last one)"
date: 2013-10-27T02:15:28-03:00
tags:
  - dev
  - legacy
---

[Previous post]({{< ref "2014-07-25-all-over-again-freebsd-overview-part-iv" >}}).

**This is the final post of this series.**

**TL;DR:** In this post, random maintenance and cleaning, better defaults, etc;
and, in the end, a small review and opinion about FreeBSD.

## Keyboard map

I've finally discovered how to change my console keyboard map. Run `kbdmap`,
then choose your keymap in the curses screen. Another option is to directly load
a keymap file: `kbdcontrol -l /usr/share/syscons/keymaps/br275.iso.kbd`.

## Default shell

To change my default shell to `bash`: `chsh -s /usr/local/bin/bash root`. You
might recall I've already installed `bash` before, but I haven't changed it to
be the default one, until now.

## Creating new ports

The Porters Handbook is a fantastic manual on how to create your own ports.
However, given its complexity, I've realized I probably won't create any new
ports for FreeBSD. I come from the `PKGBUILD` world, where creating a package is
really simple. It is so simple that I can explain it to you in just one
paragraph:

> Just take an existing `PKGBUILD` file, modify it to your needs (it's just Bash
> scripting), then use `makepkg` to create a `.tar.xz` package. You can install
> it with `makepkg -i`.

OK, I'm not comparing Arch to FreeBSD, and I don't want to begin a flame war.
But here is the problem from my point of view: a FreeBSD port uses many
predefined variables, and the process of testing and creating a port is divided
in several steps (it should be just a few). You can confirm what I'm saying by
skimming the handbook. Anyways, I'm willing to try to create a port in the
future.

Also, I can't say that modifying an existing port is difficult: it is probably
not. For example, if I want to change an `nginx` compile flag, it should be
easy. I believe it is. This is good, because most people will just modify an
existing port, instead of creating a new one. There is a list of requested
ports, where you can contribute to the project if you want to.

## Poudriere

In the last post I've said I would install `poudriere` for a friend. It turns
out this is not necessary anymore, because he already installed it. This is not
an excuse, as it doesn't need to be (i.e., I don't care, really); I just believe
it is wasted effort to install it for no purposes. However, I've skimmed over a
couple of pages and tutorials, and it looks like a good and standard solution
for the FreeBSD world.

If you want to maintain your own collection of ports and your own package
repository, you just install **Poudriere** then tell it which ports you would
like to be available. It will then build everything in a jail and later serve
these packages. Well, actually it just makes the packages available; the
responsible to serve is probably `nginx` or other common web server. As a
comparison, in the Ubuntu world you would probably create a PPA for that. In the
Arch world, you would maintain a collection of `PKGBUILD`s then create your own
repo from those packages.

Now, if you only want one or two ports, you don't need Poudriere just for that.
You better store your patches or your built `.txz` binaries somewhere.

## Services

I've already looked into services in previous posts. There is a good read about
them in the official FreeBSD Handbook (specially section 12.4, "Managing
Services in FreeBSD"). Style is like sysvinit/OpenRC; every service is either in
`/etc/init.d` or in `/usr/local/etc/init.d` for user services. Usual tasks
include: `start`, `stop` and `status`. There is one remarkable feature: if you
want to execute a service only in the current session, you should prefix the
command with `one`: `onestatus`, `onestart`, `onestop`.

To make the services restart on boot, it is just a matter of adding a line such
as:

```
SERVICENAME_ENABLE="YES"
```

in `/etc/rc.conf` or `/usr/local/etc/rc.conf`. It is also possible to use the
`service` command, although I usually avoid it.

## Overall

I believe there is not much more I can add. This was intended to be both an
overview and a documentation with my experience and exploration about the
FreeBSD system. I can keep exploring more, however this would get out of scope.
Now, two things:

### Feedback

What did you think about this mini series? Did you like it? Did you hate it?
Have you learned anything new? Any suggestions or corrections? I am open to
critics and would really like to hear you; if I ever write a new overview about
other subject, this would be useful to me. Well, if you have something to say,
just leave a comment! And, of course, if you are reading this, thanks for your
attention! I'm boring, I know :), and yet you have managed to come here, so I
appreciate it.

### What is my final opinion about FreeBSD?

I can't express everything I feel in just a subsection, but let's try to
summarize it: I liked it. I won't say I loved it, neither that I super enjoyed
it, because this would not be true, however the system is really nice. Many
packages and ports are available, there is a reasonable active community out
there, many blog posts and documentation scattered across the web, and a very
good flexibility about customizing your system by editing ports and compiling
packages: this is not easy to achieve in some Linux distros!

Use cases? **Servers, period**. This is not a system I would use for a desktop.
Neither for my own, neither to recommend to other people. There is a
distribution called PC-BSD which **may be** a good choice for desktops, but I
never tried it myself. Why not a desktop? Maintenance, mainly. And setup time /
configuration. One might argue that Gentoo and Arch are in the same category in
this aspect, but I have to disagree. OK, true reason? Compatibility. I am more
comfortable in running desktop software in Linux rather than in *BSDs, because
support and documentation for Linux is much more available. For servers, this
doesn't matter much, because use cases are usually specific.

And now, how would I rank it, compared to other Linux distros? Hmmmm, that's
tricky. Well, for servers, FreeBSD is the best distribution regarding
customization, because of its ports system. It is not super easy to customize a
`.deb` or a `.rpm` package; so, FreeBSD covers specific use cases for servers
(don't forget about Poudriere here). If customization is not much necessary, it
competes well with Debian.

Problem with Debian is that it kinda enforces you to use specific stacks of
software – for example, Apache with PHP. You can use PHP with `nginx`, but it is
a little boring to see warning messages about Apache in this case. And CentOS
packages are old, really old. FreeBSD wins in this aspect, because its packages
and ports are usually more bleeding edge / up-to-date. I guess that's it! See
ya.
