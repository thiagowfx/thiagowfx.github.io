---
title: "Tracking cheap flights from Munich"
date: 2024-10-06T00:31:23+02:00
tags:
  - dev
  - serenity
---

## Overview

I wanted to be notified whenever a flight deal from Munich[^1] appeared. The
destination doesn't really matter.

<!--more-->

There are several ways to do so semi-automatically, I tried all of them at least
once:

- follow travel blogs
- sign up for newsletters
- follow instagram pages or influencers that relay promos
- visit the websites from airlines directly
- use bots / scraping
- ask friends periodically
- date a flight attendant

The list above is overwhelming, and I have no time for all of it. Furthermore, I
have zero desire to inundate myself with (even) more social media posts, that
are often empty in nature.

Moreover I wanted to build a permanent and long-lasting solution on top of my
personal infrastructure.

Hence the only real options were: (i) travel blogs, (ii) newsletters, (iii)
scraping.

The first phase is implemented as a Telegram channel:
https://t.me/bavariabudgetbirds.

Whenever there are new deals my server pushes an update to the Telegram channel
above for each of them. The deals[^2] are tracked via a list of curated RSS feed
subscriptions, which is filtered to only match keywords that are pertaining to
Munich. It is not perfect, but it is good enough for my purposes, virtually
marginally free to run, and needs zero maintenance.

## Technical Details

I have a VPS that runs [Alpine Linux](https://www.alpinelinux.org/). The VPS
provider is not important.

The OS runs the excellent [Miniflux](https://miniflux.app/) app, managed via
OpenRC. In this specific deployment, there is no `systemd`, and there is no
virtualization (`docker`, `kubernetes`, etc). It is 100%
[KISS](https://en.wikipedia.org/wiki/KISS_principle). Miniflux is actively
developed and Alpine Linux package releases happen frequently and quickly. Even
if they do not, I have the means to create `APKBUILD`s myself when needed
  (see previous posts).

Miniflux is populated with the list of travel blogs I follow, filtering out
non-relevant posts, polled roughly every 2 hours. There is a separate Miniflux
user for this purpose, so that my own subscriptions do not get mingled
in-between.

I use the Miniflux integration with Telegram to ensure that new posts are
immediately pushed to the aforementioned channel with my Telegram bot.

Wishlist for the future:

1. Add the ability to integrate with websites that do not support
RSS directly and/or that block RSS readers. Examples:

  - https://lowcost.pro/route/MUC/XXX/EN/
  - https://www.secretflying.com/posts/category/cities-countries/germany/
  - https://www.trabber.de/en/flights-from-germany-de/

2. Convert newsletters-only sources to RSS feeds.

This solution can easily be generalized for any location; there is absolutely
nothing special about Munich in this context.

[^1]: Munich, Memmingen or Nuremberg (Nürnberg)
[^2]: Blog posts, really.
