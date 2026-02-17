---
title: "Using proxy servers on Linux"
date: 2014-12-09T02:48:45-03:00
tags:
  - dev
  - legacy
  - security
---

There are some times when you need to connect your PC to an access point which
requires you to route your connections through a web proxy. No panic! It is
really simple to config your linux desktop (or server, for that matter) to do
it. You just have to modify your `http_proxy` and `https_proxy` environment
variables.

For example:

```shell
export http_proxy=http://1.2.3.4:3128
export https_proxy=http://1.2.3.4:3128
export HTTP_PROXY=http://1.2.3.4:3128
export HTTPS_PROXY=http://1.2.3.4:3128
```

After that, just execute your favorite web browser then test your new settings.
Beware! You have to execute your web browser through the command-line, in the
same shell that you have exported those environment variables. For example:

```shell
$ export HTTP_PROXY=http://1.2.3.4:3128 && chromium &
```

Starting the `.desktop` application of your web browser, for example, wouldn't
work, unless you store those environment variables in a system wide directory
(good recommendations include `/etc/profile` and `/etc/profile.d/_`).

However, from my experience, this is limited in the sense that it would be the
default proxy of your system, which isn't what you probably want -- the common
use case is: connect to some AP, switch to its proxy, and after a while
disconnect from it *and* throw away its proxy.

Simple, isn't it? If you want to automate this task a little more, please refer
to the [Arch Wiki](https://wiki.archlinux.org/index.php/Proxy) -- from
where this post was originally inspired.

Also, I needed to apply this setup in a real world situation and I can confirm
it works really well.
