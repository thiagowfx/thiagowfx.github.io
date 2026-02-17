---
title: The Eudyptula Challenge
date: 2015-01-07T12:54:40-03:00
tags:
  - dev
  - legacy
---

**Update: I stopped at task 06 on February. Little seems to have stopped responding e-mails. Which is sad, because I was liking those tasks =/**

I am participating in the [Eudyptula Challenge](http://eudyptula-challenge.org/), which is not something exactly new, but it is as able to get you out of your comfort zone as if it were[^1].

It puts you into the mind of a Linux Kernel developer, where you are required to write and submit patches and to complete some tasks.

Subscribing to the challenge is a mini challenge itself[^2]: you must write to _little_ (the superuser behind the thing) an e-mail in plain text. This means: NO HTML. This looks like a silly requirement, but it&#8217;s the way how the (real) Linux developers work, and it is actually slightly fancier than you probably imagine. _Little_ himself recommends that the participants don't use either the Gmail web interface or Outlook.

I intend to document here my own experiences with Eudyptula[^3].

## Setting up

The first thing I went after was a decent and updated Linux distro; doing the challenge within a Linux rather than anything else offers a better experience. Zero effort here, as I&#8217;ve already had Arch Linux[^4] installed.

Next: a good text editor. Wait…why not two? I am using vim to compose e-mails, and emacs to write code.

What&#8217;s next? Oh yes…a decent `sendmail` program. It is not mandatory to have one of those, but it eases a lot the process of writing e-mail in plain text. I grabbed `msmtp` plus its MTA. Writing a config file for it is pretty straightforward.

And now I was ready: I subscribed to the challenge.

## The task #01

Hours later, _little_[^5] acknowledged my e-mail and sent me the instructions for the first task.

> I should write my first module for the Linux Kernel.

A good start. _I didn&#8217;t even know how to begin, oh no!_

The task was to write a module that would write &#8216;Hello World&#8217; to the debug level log of the running kernel when loaded.

First, I had to install some dependencies to be able to compile a couple of C programs. Actually, the `base-devel` group from Arch already contained most of the things I would need. `linux-headers` and `bc` were also relevant.

My first module, written in C[^6], looked like this in the end:

```c
#include <linux/init.h>;
#include <linux/kernel.h>;
#include <linux/module.h>;

MODULE_AUTHOR("Thiago Perrotta");
MODULE_DESCRIPTION("A gentle Hello World module");
MODULE_LICENSE("GPL");

static int __init hello_init(void)
{
  printk(KERN_DEBUG "Hello world!\n");
  return 0;
}

static void __exit hello_cleanup(void)
{
  printk(KERN_DEBUG "Goodbye World!\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
```

I didn&#8217;t get it right in my first trial, of course. In particular, I wrote &#8216;Hello World&#8217; to the INFO log level, using `KERN_INFO`, instead of `KERN_DEBUG`.

And I also needed a `Makefile` to be able to compile it:

```make
obj-m += hello.o
KERNEL ?= /lib/modules/$(shell uname -r)/build

all:
    make -C $(KERNEL) M=$(PWD) modules

clean:
    make -C $(KERNEL) M=$(PWD) clean
```

The `Makefile` wasn't right in my first trial, either. Another requirement of this task was that this file should provide an environment variable, as an alternative location for the build directory of the kernel, opposed to being a hard coded value. I provided one from the beginning, but the way I wrote it was slightly wrong.

Now, this code didn't just pop out of my head out of nothing. Although I know how to program in C, I never did kernel programming before. I had to look up for some documentation about how to write a module. It wasn't super straightforward, because I found many documentation sources about writing modules for the Linux 2.6.x version, which is outdated now[^7], and the modern version of writing modules is a bit different from it.

Also, I was careful not to accidentally find a solution for this task directly. Of course, some people have already done it, and they could have written something about their experiences, as I am doing right now.

Anyways, after writing those two files and testing that they really worked as expected, I loaded my freshly built module. And yay, a simple `dmesg` would reveal my hello message out there. It was really cool to see it worked:

```text
thiago@archpad ~//01 % sudo modinfo hello.ko
filename:       /home/thiago//01/hello.ko
license:        GPL
description:    A gentle Hello World module
author:         Thiago Perrotta
depends:
vermagic:       3.17.6-1-ARCH SMP preempt mod_unload modversions
```

After that, I&#8217;ve sent everything I should to _little_, and today I got its reply, about the second task. So, let&#8217;s go…

## What have I learned with this task?

- how to write a Makefile to compile a kernel module
- how to execute shell commands within a Makefile
- how to use an environment variable within a Makefile
- how to write e-mails in plain text and send them with msmtp
- how to send attachments **without** base64 encoding[^8]
- how to load, unload and get information about modules
- modules are so dynamic and easy to load, huh? Like USB devices. I would never imagine that.

[^1]: It is also a excuse for me to write something here :-)

[^2]: Pun intended.
[^3]: I can&#8217;t write this in one shot. Really. Eudi←yptull←a. **EUDYPTULA**.
[^4]: The distro that will conquer the [moon](https://wiki.archlinux.org/index.php?title=DeveloperWiki&oldid=293327#Organization).
[^5]: Which turned out to be a bot.
[^6]: Damn, everything will be written in C from now on. That&#8217;s what we get with kernel programming, I guess.
[^7]: Only lazy or paranoid Linux sysadmins will tell you otherwise 😉
[^8]: This turned out to be the hardest thing of this task, yet it wasn&#8217;t even part of it.
