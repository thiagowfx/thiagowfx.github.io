---
title: "'New' series: Raspberry Pi fun with DevOps, redux"
date: 2026-01-17T23:14:21-03:00
tags:
  - alpine-linux
  - dev
---

Once upon a time, [a few mistakes
ago](https://www.youtube.com/watch?v=vNoKguSdy4Y), I wanted to start a blog
series about doing projects with my two Raspberry Pi units at home.

The [initial post]({{< ref "2024-10-13-new-series-raspberry-pi-fun-with-devops"
>}}) described my vision, but it was never followed upon. There was a mix of
reasons for that:

- lack of time and proper prioritization
- being overwhelmed by choice
- a desire to stay digitally disconnected[^1]
- lack of structure in this blog[^2]

Needless to say, my motivation is still well alive, and I have an itch to move
forward with this project this year. Let's see how it will flow.

I want to start by commenting on my ideas from 15 months ago. New Thiago reviews
old Thiago.

> For a long time I've been wanting to do something useful with them, while
> increasing my DevOps toolkit knowledge.

And trying out new tools and workflows that I am not able to try at work –
either because they don't make sense there, or due to lack of prioritization.

> The roadblock to do so was the most classic excuse: lack of non-interrupted
> time.
>
> There's plenty of motivation, and ideas. These will likely _never_ run out,
> any time soon.

Still true! Hah!

> There's no guarantee I will follow up on all of these ideas but,

I can foresee the future! 🔮

> Guiding principles
>
> _a.k.a. rules of engagement_

My revised goals:

1. It must run unix → **unchanged**.
2. It must be vanilla / upstream → **unchanged**.
3. Every software installation _must_ come from a package → packages are still
   OK, but I am opening up the possibility for container images as well (e.g.
   via docker or podman). Ad-hoc installations are still explicitly ruled out,
   UNLESS they are scripted in an idempotent manner e.g. via Ansible or pyinfra,
   but only as a last resort.
4. It must have no X11 nor Wayland nor a graphical system → **unchanged**. Web
   server management interfaces are acceptable though.
5. Software updates must happen with a single command → **unchanged**. These
   days I have
   [sd_world](https://github.com/thiagowfx/pancake/tree/master/sd_world). A
   custom [Justfile](https://just.systems/) recipe would also be acceptable:
   `just update` or `just upgrade` or `just world`.
6. It should be reasonably popular and well-supported → **unchanged**. No
   abandonware.
7. It should support Raspberry Pi (the ARM architecture, for that matter) as a first-class citizen → **unchanged**.

Revised distributions / operating systems:

- Debian
  — RaspberryPi OS
- Fedora
- Alpine Linux
- Arch Linux (Arch Linux ARM)
- Gentoo Linux
- NixOS
- FreeBSD
- OpenBSD
- ~~openSUSE~~: I decided that, if I invest in the `.rpm` world, Fedora is the
  way to go.
- ~~Ubuntu~~: I decided that, if I invest in the `.deb` world, Debian is the way
  to go. Ubuntu remains solid for commercial / enterprise usage, but this is a
  personal project.
- ~~Void Linux~~: too niche, no enthusiasm for Void Linux in my circle these
  days. If I ever tried it, I feel it would be used as a Desktop distro.
- ~~Slackware Linux~~: updated on 2025-09-11. Too niche, no enthusiasm for it in
  my circle these days.

> This list is still quite large.
> I will need to trim it down further in the following days. Stay tuned.

Now it's shorter: 4 less distros. Progress!

One big question is whether I'll treat my Raspberries [as pets or as
cattle](https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/0).

To be continued ■[^3].

[^1]: [Life is short](https://sive.rs/n).
[^2]: More specifically: linking related posts to each other, and having an easy
    way to go from the previous to the next post in a series.
[^3]: Wishful thinking.
