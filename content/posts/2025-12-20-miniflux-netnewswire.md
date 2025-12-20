---
title: "Miniflux: NetNewsWire integration"
date: 2025-12-20T14:39:24-03:00
tags:
  - dev
  - selfhosted
---

[NetNewsWire](https://netnewswire.com/) is a great RSS **client** reader for
macOS and iOS.

I already use [miniflux](https://miniflux.app/) though. It's too bad NetNewsWire
does not support miniflux as a server back-end:

> Syncing via iCloud, Feedbin, Feedly, BazQux, Inoreader, NewsBlur, The Old
> Reader, and FreshRSS

Or does it?

Thanks to [Luke Harris](https://www.lkhrs.com/blog/app-defaults-2025/), I just
realized it does _in fact_ support Miniflux, albeit indirectly!

When adding your self-hosted miniflux server, select the "FreshRSS" option,
which is also compatible with the Google Reader API.

**Note**: Add the URL without a trailing slash.

Why use NetNewsWire instead of accessing Miniflux directly on iOS as a web app?

1. It works off-line (e.g. read your feeds while flying) – in the meantime,
   there's a [Feature Request](https://github.com/miniflux/v2/issues/1395) for
   Miniflux to support an off-line mode
2. It caches articles and posts locally: a) saving mobile data when syncing
   upfront via Wi-Fi and b) yielding faster transitions between feed entries
