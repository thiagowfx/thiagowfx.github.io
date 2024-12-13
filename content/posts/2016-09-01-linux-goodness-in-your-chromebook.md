---
title: Linux goodness in your Chromebook
date: 2016-09-01T16:29:07-02:00
tags:
  - linux
---

[Chromebooks](https://www.google.com.br/chromebook/) are excellent for testing
and playing with Linux userland[1] stuff. And, even better, (almost) every
change you make to it can be reset back to its factory state — even in the worst
case of completely wiping ChromeOS from your computer. As long as you don't mess
up with its [firmware](https://en.wikipedia.org/wiki/Firmware), you can do
whatever you want and still be safe. Most models are cheap, battery life is
amazing for a cheap Linux laptop (8+ hours, depending on the device and on
usage)[2], Linux support is great (well, it ships with a Linux OS, right?) —
even for most touchscreen models [citation needed] — and it is simple (as in
KISS).

<!--more-->

Now, the previous paragraph sounded a little repetitive, but I'd like to focus
on two of my previous points here:

1.  **You can do whatever you want and still remain safe.** Yes. Indeed, you can
    reset your chromebook to its factory state with just a few clicks — this is
    still hard to do with Windows and OS X, as far as I know. I think Windows 10
    is introducing a feature to ease this process, however I am not sure about
    it yet. This is super important (and convenient!) for people playing with a
    ChromeOS device — like me. My usual way to reset the system back to "factory
    state" was, usually, to install a Linux distro with the btrfs filesystem so
    I could create a snapshot upon the installation was finished, and then
    revert back to it at anytime I wanted. However, this solution is a little
    cumbersome. The second usual solution would be to simply use a virtual
    machine, but I don't need to reiterate that this is slow and limited in many
    ways.
1.  **Simple**. This is really important if you don't want to have headaches in
    the long run. For starters, simplicity is always a trade-off that involves
    performance: it is hard to be simple with a core i7 CPU, so if you choose
    the KISS path, you are deliberately sacrificing some of your performance.
    Once you accept that, we can move forward: Chromebooks are very simple
    devices. They're almost directly comparable to a tablet with a keyboard.
    Sometimes they feel like a full-featured arduino.

These were some small highlights about my decision to get one. Now here's the
good stuff:

## There be dragons

**Disclaimer/Warning**: these will potentially void the warranty of your device,
and they are only recommended if you know what you're doing. Be a good user and
research before messing up with your system. I will provide upstream links with
documentation as much as possible.

* [Enable developer
  mode](https://www.chromium.org/chromium-os/poking-around-your-chrome-os-device)
  — it's a must; however, it weakens the security of your device. Beware and
  research! This can be totally reverted with a single keystroke (SPACE) at the
  login screen that will appear in every subsequent boot of your system.
* [dev_install](https://www.chromium.org/chromium-os/how-tos-and-troubleshooting/install-software-on-base-images)
  — to get fdisk, python, tmux, nano, emerge (for binaries), and so on. These
  are just a few developer tools, they won't scale and you won't get whatever
  package you want in your vanilla ChromeOS, however these might help a lot with
  simple tasks. For example, you can format a SD card or an USB Flash Drive
  directly from ChromeOS upon running this tool — otherwise, you'd usually have
  to use another computer, with another OS to do it. It uses just a little space
  (~100M+ or so), and it can be totally reverted with `devinstall --uninstall`
* Switch to the [beta
  channel](https://support.google.com/chromebook/answer/1086915?hl=en) if you
  want to be slightly more into the bleeding edge — but not too much as in the
  dev channel. In fact, at the time of this post, select devices in beta channel
  have support for Android apps in ChromeOS.
* Open a new shell (crosh) with Ctrl + Alt + T. The default username is
  'chronos', without any password.
* User-writable locations are: /usr/local (in particular, /usr/local/bin is in
  your PATH env variable out-of-the-box (echo $PATH)), /tmp and
  /home/chronos/user/Downloads. There might be more, but these are enough.
* You can also insert removable media (USB flash drives, SD cards), which would
  show up on /media. ChromeOS can read/write filesystems formatted as ext{2,3,4}
  and FAT{,32} at least.

These are the basics. However, you will soon find out that you cannot do too
much with ChromeOS, even with these modifications. In this case, there are three
options, and all of them involve getting a Linux distribution in some way:

1.  **(RECOMMENDED)** Install a Linux distro on either a SD card or an USB Flash
    Drive and dual-boot from it. It is really easy to dual-boot, you just press
    C-d to boot from the internal eMMC / SSD, or C-u to boot from external
    storage. There's no need to play with grub, EFI, or any (other) fancy
    bootloader. If you change your mind later on, just format your SD card:
    there is no need to change anything on ChromeOS.
1.  **(NOT RECOMMENDED BY ME)** Completely wipe ChromeOS by installing another
    Linux distribution on its place. Although it's easy to revert this process
    through [recovery
    media](https://support.google.com/chromebook/answer/1080595), it completely
    defeats the purpose of getting a Chromebook in the first place, especially
    now that Android apps are starting to become available on them (for
    touchscreen devices, of course).
1.  **(PROBABLY WOULDN'T RECOMMEND, BUT YOU MAY LIKE IT)** Install a chroot
    alongside your ChromeOS, such as
    [crouton](https://github.com/dnschneid/crouton). I tried it however I hated
    it. It is very buggy and opinionated, somewhat similar to oh-my-zsh: both of
    them promise to deliver a good framework and they're kinda large open source
    projects, however they do lots of automatic things for you, and you end up
    not knowing what is happening to your system. It opposes the Arch Linux
    philosophy, being user-friendly rather than user-centered. Some people like
    it, I won't argue this, it can work for them; but not for me. An alternative
    would be to install a chroot manually, without the help of crouton.

I've chosen the first option, installing Arch Linux ARM on my Chromebook. So
far, so good: it's working very well. Storage is easily shared between the two
OSes (by using the SD card). There's more to get out of my system, and I intend
to share new findings in this blog. **In particular, the most important one: to
find an easy way (not crouton!) of running whatever Linux-compatible application
I want from within Chrome OS, without dual-booting.** I have a few ideas (well,
it's just a matter of creating a KISS chroot), I just want to polish them a
little more before trying them out.

## See also

* [Generic Chrome OS Troubleshooter Chart v0.3](https://imgur.com/BrVVyNi)

## Footnotes

1.  I wouldn't say the same for kernel stuff though. It is not trivial to
    install a bootloader (such as grub) or to boot a custom kernel in a
    Chromebook. It's possible indeed, it's just not as nice or as easy as an
    average PC or Mac laptop from today, especially if you have the intention of
    keeping the upstream OS (Chrome OS) in the device.
1.  People probably would cite a Macbook, a Surface Pro, or something else
    similar here. For starters, did you see how much they cost, in comparison to
    an average Chromebook? Such a comparison wouldn't be fair.
