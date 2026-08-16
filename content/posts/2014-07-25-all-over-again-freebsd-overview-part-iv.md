---
title: "All over again - FreeBSD Overview (Part IV)"
date: 2014-07-25T12:00:00-03:00
tags:
  - dev
  - legacy
---

[Previous post]({{< ref "2014-07-23-hello-world-freebsd-overview-part-iii" >}}).

**TL;DR:** Reinstalling the system, in QEMU/KVM + Xorg stuff. Okay people, so
after a (probable) virtual disk corruption, I've decided to start a new and
fresh installation. I'm using the same ISO as before (Release 10, amd64),
however I'm now with QEMU/KVM. Fortunately, my beloved Linux distro has a very
well documented wiki page on how to setup it. I've chosen `gnome-boxes` as GUI,
after a non-successful trial with `qtemu`, and it was pretty straightforward to
use it to re-install the system.

Too straightforward that I don't need this anymore. This time the network
interface didn't configure itself automagically, out-of-the-box (at least not
completely). I later confirmed that: after logging in as root, there was no
internet connection. At this point I suspected I would be in trouble. It is a
nightmare to manually set up networks from the command line – I know it from
Arch Linux. However, after further inspecting with `ifconfig` and then realizing
that there wasn't any `/etc/resolv.conf` file, hmmmmm, I got it: DNS!

What, then? I tried (literally, several tries) to play with `dhclient`; things
such as `service dhclient status`, `service dhclient onestart`, etc; finally, I
managed to do a `dhclient re0` (`re0` is the name of the network interface
here). This worked! `ping google.com` (the most standard way to test connection,
huh?) returned successfully. So, let's reinstall our ol' good tools:

```shell
pkg install bash dmenu dwm htop i3 rxvt-unicode uemacs xorg
echo "urxvt &\nexec dwm\n" >> $HOME/.xinitrc
```

A quick `startx` wouldn't work. However, this time I didn't shutdown the VM;
instead I've found that I could use `Alt+F1` to switch to a tty (**note**: it is
not `Ctrl+Alt+F1`, this would instead switch to a tty in my host machine. In
other words, drop the Ctrl key here.) In part III, I got stuck here, remember?
Not anymore.

```shell
service dbus onestart
service hald onestart
```

Additionally, add the following to `/etc/rc.conf` so this will persist across
reboots:

```shell
dbus_enable="YES"
hald_enable="YES"
```

Now a `startx` works, and I have a terminal emulator (`urxvt`) running. Both
keyboard and mouse work. Nice! This is getting better. To properly configure my
X keyboard is simple: `setxkbmap br`. Yet I still have to discover how to
configure it in a tty. I've chosen a lightweight GUI application to test Xorg:
`pcmanfm` (a simple file manager). It runs okay, except that I don't see any
folders there. This is probably related to some missing component, or something
about the FreeBSD filesystem that I don't know yet.

Since X seemed to work okay, I've installed `i3`. I just tested with `dwm`
because it is even more lightweight than `i3`, but I don't know how to operate
it beyond its basics; however, I'm very familiar with `i3`. My updated
`.xinitrc` file:

```shell
setxkbmap br &
urxvt &
exec i3
```

Xorg doesn't end here, of course. However, my goal – and I've already said this
before – is to get a feeling of how FreeBSD works, not to exhaustively configure
each of its components.

## Next

At this point, here is my org file (from now on I'm gonna delete old 'DONE'
entries, there is no need to keep displaying them):

```org
DONE X Window System (X11)
TODO create a new port (poudriere?)
  This will probably take a while. I'm accepting suggestions of software to port (should be something not much complex).
TODO jails, chroot, etc
  I've heard they are common in the FreeBSD world. Let's find out…
TODO services (rc.conf, /etc/rc)
  Explored this a little, but let's see if there is more.
TODO Linux compatibility?
  systemd, gnome3, binaries in general. Is any Linux software automagically portable to FreeBSD?
TODO what about user contributions?
  Is there something like Arch's AUR? Maybe freshports?
```

~~If you want to suggest more items to this list, please let me know. There is
no fixed quantity of posts, I'll keep updating my experience as long as there is
something relatively relevant to write about.~~

~~**Edit (2014-07-30):** There is a friend of mine who needs Poudriere on his
server. I'll probably help him then write about it in my next post, by the end
of the week. Thank you for your patience.
