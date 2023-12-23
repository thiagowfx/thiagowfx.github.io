---
title: "Doas: bridging the sudo gap"
date: 2022-02-07T14:49:03-05:00
tags:
  - linux
---

[`doas`][doas] is a lightweight and safer replacement for `sudo`. In most occasions you invoke it exactly like `sudo`:

```shell
$ sudo apt install <foo>
$ doas apt install <foo>
```

`doas` has gained popularity recently. Besides being the default in OpenBSD, Alpine Linux 3.15 (released last year) has also [switched to it](https://wiki.alpinelinux.org/wiki/Release_Notes_for_Alpine_3.15.0#Move_from_sudo_to_doas):

> `doas` is the default temporary privilege escalation tool. You are advised to migrate from `sudo` to `doas` as 3.15 will be the last release to support `sudo` throughout its full lifecycle, in 3.16 `sudo` will be moved from main to community.

It's not very difficult to get used to it, however you may still find yourself writing `sudo` occasionally. This post highlights a few ways to bridge that gap.

<!--more-->

## Use a shell alias

In your `~/.bashrc` or `~/.zshrc` or in your favorite shell, do:

```shell
alias sudo=doas
```

Caveat: Besides being an user-dependent workaround[^1], `doas` isn't really a full drop-in replacement to `sudo`. This workaround will work in most day-to-day situations but it will obviously not support most `sudo` specific flags.

## Use a shim/wrapper (recommended)

Alpine Linux provides a [`doas-sudo-shim`](https://pkgs.alpinelinux.org/package/edge/community/x86_64/doas-sudo-shim) package:

```shell
$ doas apk add doas-sudo-shim
```

> This is a shim for the `sudo` command that utilizes `doas`. It supports only a subset of the `sudo` options (both short and long variants) that have an equivalent in `doas`, plus option `-i` (`--login`).

This is a slightly better solution, as this thin wrapper is aware of some `sudo` flags, translating them to the equivalent `doas` ones; furthermore, it works out-of-the-box and it's system-wide. As an added bonus, it's implemented entirely in shell script, being as much portable as possible.

## Final remarks

Last but not least, you could choose to install `sudo` and configure it, keeping both `doas` and `sudo`, but what's the point? If your system favours `doas`, stick to `doas`. There's no need to unnecessarily increase complexity by keeping around two programs that serve exactly the same purpose.

If you don't like or want `doas` for some reason, you could look into the other way around: find a `doas` shim that bridges to `sudo`, or define an alias: `$ alias doas=sudo`.

The best long-term solution though would be to just use `doas` without any alias or shim, but our muscle memory may have trouble adapting to that, especially when `sudo` is still the _de facto standard_ in most Linux distributions out there these days.


[doas]: https://man.openbsd.org/doas

[^1]: To make it system-wide, change the relevant file in `/etc`: for example, `/etc/bashrc` for `bash`. I would advise against it though.