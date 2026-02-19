
Salt is what you want when you have to manage several servers. It looks like a
good option for open-source servers (Unix systems), so I'm giving it a try. A
common alternative is the community version of Puppet.

## Motivation

Historically, I've always used Arch on my notebook because it's the machine I
use, customize, and play with the most. Arch is perfect for it—I'm always with
the latest software and always tinkering.

But my desktop? I rarely use it compared to my notebook. I've tried installing
Arch on it, but always wiped it days later because I tend to over-customize Arch
boxes and didn't want to duplicate work across machines.

What distro is good for "non-mainstream" personal use but that you won't use
much? Each has problems:

- **Funtoo/Gentoo**: Too many compilation times. You don't want that for a
  machine you don't use often.
- **Ubuntu/openSUSE**: Okay, but Ubuntu is often out-of-date; openSUSE's zypper
  packages are bloated.
- **Fedora**: Changes releases too often. You don't want to reinstall.
- **Alpine/grml**: Great for other purposes, not "my-quiet-desktop".

Maybe the problem is me. I got too strict about my personal environments. Then I thought: the problem is lack of automation. If you don't want to touch machines you don't use often, automate them. Upgrades, maintenance, etc. **SaltStack** to the rescue!

## SaltStack Hello World

We begin with hello world. For network environments? A ping, of course.

I'm installing Salt on my Arch notebook (master) and my Arch desktop (minion).
Salt uses a master-minions hierarchy. My notebook is the master; my desktop is
the minion.

Salt is cross-platform, so you can use different distros. You need to care about
your init program; systemd eases everything for me:

```shell
$ systemctl enable salt-master # (in master)
$ systemctl enable salt-minion # (in minion)
```

Salt is now set up. After installing, you have to connect your machines. This is
well documented (RTFM). I connected them on the same LAN network and they
continue to recognize each other across reboots.

Now the best part. From my master (notebook):

```
# root@arch /home/thiago # salt '*' test.ping
<$MYHOSTNAME>:
  True
```

Everything is properly set up. Now what? I don't know—I'll discover!

But I tried automating a system upgrade:

```
root@arch /home/thiago # salt '*' pkg.install refresh=True sysupgrade=True feh
<$MYHOSTNAME>:
  ----------
  feh:
    ----------
    new:
      2.12-1
    old:

  giflib:
    ----------
    new:
      5.1.1-1
    old:

  imlib2:
    ----------
    new:
      1.4.6-3
    old:

  libexif:
    ----------
    new:
      0.6.21-2
    old:

  libid3tag:
    ----------
    new:
      0.15.1b-8
    old:
```

Really nice! I can install or remove any package. This is all about automation.
I'll see in the next days if I keep using Salt.

## Footnotes

- Why Salt? I just picked it first. I could use other technologies. I don't
  recommend it right now—just testing it. The choice was pure serendipity.

