---
title: "Living on Ubuntu - Instance #1"
date: 2014-09-15T23:24:45-03:00
tags:
  - dev
  - legacy
---

As stated in my last post, I'm now using Ubuntu as my main linux distro. This is temporary and might even hurt a little, however I'm willing to keep going with this goal for a while.

In this post I'm going to document some cleanups and tips/tricks/whatever that I find interesting and, sometimes, important too.

**Disclaimer**: I am a heavily biased Arch Linux user. Anything related to it in this post is probably not a coincidence. This disclaimer won't be repeated through other posts of this series. So, you have been warned. This is important to understand some of the motivations behind the changes I'll list here.

Now, just one thing: one of the reasons I'm using Ubuntu right now is so I won't spend much time customizing it. So, I am deliberately cutting this list in more than a half. There are other things that I would usually do _but_ I simply won't.

1. Enable the **root** account – by default, the root account is disabled on
   Ubuntu. This is great so newbies won't harm the system; however, powerusers
   don't like that, this is simply annoying for them. You might do that as
   follows:

```shell
$ sudo passwd root
```

Then just enter a password for it. Now you might become a superuser by invoking
`su`.

 2. Install `aptitude`. And **never**, I mean **ever****ever** touch `apt-get`.
    `apt-get` is evil and **will** break your system sooner or later. Top used
    `aptitude` commands are probably `aptitude install`, `aptitude upgrade`,
    `aptitude remove` and `aptitude search`. The `-y` flag is useful sometimes,
    too. So,

```shell
$ sudo apt-get install aptitude -y
```

Then **forget apt-get**!

 3. Install `unity-tweak-tool` then change some annoying Unity defaults. What is
    annoying depends on each user taste.
 4. I like to create a `Ramdisk`. How? Arch Wiki Ramdisk. This also works for
    Ubuntu.
 5. Install the `classicmenu-indicator` package.
 6. I like using a clipboard manager. `clipit` is a good choice and is well
    integrated with the Unity panel.
 7. Add/activate workspaces. 4 of them is (usually) okay. Use `Ctrl + Alt +
    directional keys` to cycle through them.
 8. `Super + D` shows the desktop. (Super is usually the key with the windows
    logo).
 9. `Ctrl + Alt + L` locks the screen.
10. Install the `nautilus-open-terminal` package.
11. Improve your `.bashrc`. How? See here. You'll also find my `.bashrc` there
    (search for _thiagowfx_).
