---
title: "MIUI debloater"
date: 2025-12-21T19:28:50-03:00
tags:
  - dev
  - privacy
---

[Previously]({{< ref "2025-11-29-coreldraw-disable-ads-on-windows" >}}).

From 'Technical Support' tales of the trenches.

**Problem statement**: My parents have a Xiaomi Android phone. The amount of
bloat in it is horrifying, incredibly disgusting.

It is not possible to _uninstall_ system apps – including Xiaomi's and Google's
– by normal means. Once upon a time it used to be possible to, at the very
least, _disable_ them. But now there are many apps that can't even be disabled!

One example: YouTube Music. It's such a shame that vendors, even supposedly
reputable ones, need to employ such consumer-hostile dark patterns in order to
artificially inflate their engagement metrics.
Shove it in our face, but we're not using YouTube Music, full stop.

The goal is to remove as many of these apps as possible, using whichever means
to be necessary.

I found [MIUI debloater](https://github.com/kirthandev/MIUI-Debloater-official)
to work well. Instructions, executed preferably from a Windows machine:

- install a modern Java SDK (e.g. 21 or 25)
- install ADB
- open the `.jar` provided by the project

From the ~~ill patient~~ affected phone:

- enable USB debugging via system settings – multiple confirmation prompts are
  needed to do so
- connect the device with a USB cable to the computer

From this point on it is quite straightforward to remove undesired / unwanted
apps.

The project is a GUI Java app with options to install and uninstall
applications, among other functionalities (e.g. download and install custom
ROMs).

Just be careful not to remove important Android system apps – triple-check that
you're only removing non-essentials.
