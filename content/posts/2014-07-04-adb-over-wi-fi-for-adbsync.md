---
title: "adb over Wi-Fi for adbsync"
date: 2014-07-04T19:33:12-03:00
tags:
  - dev
  - legacy
---

Serendipity is good. I've just discovered one can use `adb` over Wi-Fi. What
does it mean? We (well, I) don't need anymore Android apps just to transfer
files between your computer and your device.

This has a common drawback, though: it is not very fast. So, if you want to
transfer 1 GB of files to your device, you better arrange an USB cable. I won't
detail here how to do that, because a simple search with your favorite search
engine will teach you that. However, here is a nice application I've found so
far: to transfer (sync) files between a folder in your device and a folder in
your PC.

The workflow is very simple: first you set up a target directory in your device
(mine is '/storage/sdcard1/adbwifi'). Now, you'll issue a command such as
`adbsync /home/thiago/tvseries/loremipsum/`. This will copy everything from your
'loremipsum' directory to `/storage/sdcard1/adbwifi/loremipsum`. Sounds nice?

You only have to issue this command, after enabling `adb` in your device and
connecting it to your PC. That's it. No need for cables, GUI, webapps, etc.

You'll notice this `adbsync` command doesn't exist natively. There is an `adb
sync`, but this won't do what you are expecting. So I created an 'adbsync'
(bash) function/script and set it up as an alias. Here it is: (gist no longer
available).
