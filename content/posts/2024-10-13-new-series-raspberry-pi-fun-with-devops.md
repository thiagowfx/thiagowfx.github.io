---
title: "New series: Raspberry Pi fun with DevOps"
date: 2024-10-13T11:31:13+02:00
tags:
  - dev
  - bestof
---

## Intro

I have two raspberry pi[^1] units sitting idle at home, a 3B and a 4.

For a long time I've been wanting to do something useful with them,
while increasing my DevOps toolkit knowledge.

The roadblock to do so was the most classic excuse: lack of non-interrupted time.

There's plenty of motivation, and ideas. These will likely _never_ run out, any time soon.

That said: It's very easy to get distracted and lose focus.
There is so much information today, in the form of
YouTube videos,
blog posts,
forums and communities (e.g. the likes of Hacker News and Reddit),
podcasts,
books…the list goes on, and it does not end.

Therefore, for the sake of fixing a North Star path,
I wanted to make an initial blog post with some of the ideas that are currently in my head.

There's no guarantee I will follow up on all of these ideas but,
as long as their spirit is ingrained in semi-permanent written form,
I figured that shall be enough to make me accountable to myself.

## Guiding principles

_a.k.a. rules of engagement_

1. It must run Unix

No Windows. No macOS. Anything else is fair game. Corollary: It must run either Linux or BSD.

2. It must be vanilla / upstream

No spin-offs. For example: for Ubuntu, no Xubuntu. For Arch Linux, no Manjaro. For Gentoo, no Funtoo.
And so on. Stick to the _core_ / base Linux distributions.
For BSD, this is a non-issue.

3. Every software installation _must_ come from a package

If there is no package, I will create one myself.
This is easier if I use Arch Linux or Alpine Linux, but I am willing to contribute to other distributions as well.

4. It must have no X11 nor Wayland nor a graphical system

It should be a pure server.
In the past I ran RaspberryPi OS (neé Raspbian) and it wasn't very useful, besides being super slow and sluggish.

5. Software updates must happen with a single command

There is no need for auto-updates (these are often not well-supported anyways), but a human operator should be able to upgrade
_everything_ in a single shot. It doesn't have to be a single command (e.g. `apt update` + `apt upgrade` is acceptable), but it
should be contained within a short script.

6. It should be reasonably popular and well-supported

No obscure distributions.
I don't particularly care about a sizeable community (I won't join their Discord server nor Reddit community anyway),
but there should be at least one official support channel, and it would be preferred that it is old-school (BBS / Discourse / forums, mailing lists, IRC / Matrix).
Stack Exchange is also acceptable to an extent.
The problem with the modern stuff (Discord, Reddit) is that it is too proprietary, can / will disappear at any moment, and will be heavily used to train LLMs with no scrutiny.
Commercial support is fine. For example, Red Hat backing Fedora, Canonical backing Ubuntu, and SUSE backing openSUSE is a non-issue.
I would just avoid commercial enterprises that suffocate their open counterparts.

7. It should support Raspberry Pi (the ARM architecture, for that matter) as a first-class citizen

If Raspberry Pi support is considered experimental, I would avoid the trouble at this time.

Stopping briefly here for a moment, the following list comes to mind, using [DistroWatch](https://distrowatch.com/) and [Linux Distribution timeline](https://en.m.wikipedia.org/wiki/File:Linux_Distribution_Timeline.svg) as an aid:

- Debian
  - RaspberryPi OS
- Ubuntu
- Fedora
- openSUSE
- Alpine Linux
- Arch Linux (Arch Linux ARM)
- Void Linux
- Gentoo
- NixOS
- FreeBSD
- OpenBSD
- ~~Slackware Linux~~ (Updated on 2025-09-11)

This list is still quite large.
I will need to trim it down further in the following days. Stay tuned.

Some observations before I make a final decision:

- I have two units, so one decision to make is whether to choose the same distribution for both or distinct distributions for each. One Linux and one BSD, for example.
- I never used the following distros: Void Linux, NixOS, OpenBSD, Slackware Linux. There's always an appeal to trying out something new, even if just ephemerally.
- I am heavily experienced in Debian / Ubuntu, Arch and Alpine (with a tad of Gentoo as well). There's an appeal to using something I am already familiar with to get the OS out of the way, and thus focus more on DevOps.
- NixOS is very tempting for the purposes of reproducibility, but every time I look at it I feel lost in its sea of complexity. And it oftentimes feels bloated. Reproducibility comes with a non-trivial upfront cost.
- OpenBSD feels very tempting as a self-contained, "do one thing and do it well", KISS & secure system. It lacks on integration with third-party software, but perhaps that's a feature.
- Let's be honest, as much as Slackware has its charm, realistically I am not choosing it. Its ecosystem is too small today. It doesn't provide any value when compared to the rest of the list. Between Slack and Alpine, I'd easily pick Alpine with no effort.

Hence we can already eliminate one: ~~Slackware Linux~~.

To be continued ■

[^1]: _Two units_ is a safer choice than "raspberry pies" or "raspberry pis".
