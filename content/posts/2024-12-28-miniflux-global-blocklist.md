---
title: "Miniflux: global blocklist"
date: 2024-12-28T18:04:19-03:00
tags:
  - dev
---

One of the best features of [miniflux](https://miniflux.app/) rolled out [this year](https://github.com/miniflux/v2/blob/main/ChangeLog)[^1]
was the ability to globally block feed items that match certain patterns.

Previously it was possible to do so only in an individual feed basis.

[The Miniflux documentation](https://miniflux.app/docs/rules.html#global-filtering-rules):

> Global filters are defined on the Settings page and are automatically applied to all articles from all feeds.

My usage is like this:

```
EntryTitle=(?i)(Apple TV|\bCrypto\b|iPad)
```

To add new terms, I add more regular expressions with an or (`|`).
Whenever the term is a common substring, I add word boundaries with `\b`.
The `(?i)` is to make the matching case insensitive.

This approach helps me fight against information overload.

There are some people I like to follow via Miniflux, but I am simply not interested in some of their kinds of posts.

For example, there are excellent bloggers like [John Gruber](https://daringfireball.net/) and [Nick Heer](https://pxlnv.com/),
but they post way too much about Apple. There are some classes of Apple products I am simply not interested in, because
I do not own any of them, nor plan to e.g. Apple TV or iPad or Vision Pro.
A global block list is a much more effective way to address mass filtering out of posts than per-feed ones.

[^1]: Since `miniflux` version 2.1.4 (July 9, 2024).
