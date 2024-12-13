---
title: "Bypass news article paywalls"
date: 2022-03-06T21:49:53-05:00
tags:
  - privacy
---

I try to avoid websites with paywalls. If I really like the website and it
deserves my attention, I will throw in a monthly subscription for it.
High-quality content deserves to be supported. The fragmentation isn't always
great and it's often hard to keep track of multiple distinct news sources and
portals / subscriptions, but that's a topic for another day.

Sometimes people will link to news articles or websites with paywalls from
various sources (blogs, social media, other news articles, etc). I'd rather
know in advance that those articles are paywalled, but that's not always
possible. After clicking them, curiosity already killed the cat.

There are several ways to access those as one-offs. I will add a disclaimer
that I do not publicly endorse any of those methods, they are just mentioned
for educational purposes.

<!--more-->

The most typical way is to open an incognito tab or window in your browser with
the desired URL. This works because many paywalls are often implemented with
browser cookies.

The second most typical way is to use a VPN to appear that you're accessing the
URL from another IP address. This works for websites that add rolling article
limits per IP address.

Occasionally some large news websites will implement paywalls poorly:

> The idea is pretty simple, news sites want Google to index their content so
> it shows up in search results. So they don't show a paywall to the Google
> crawler. We benefit from this because the Google crawler will cache a copy of
> the site every time it crawls it.
>
> All we do is show you that cached, unpaywalled version of the page.

[12ft](https://12ft.io/) automatically uses this mechanism to display cached
versions of news articles. If you're in `<url>`, just prepend `12ft.io` to it:
`https://12ft.io/<url>`.

Alternatively, [Outline](https://outline.com/) used to be another
website/service to do so, but apparently it is
[unavailable](https://news.ycombinator.com/item?id=30564665) since last week.
Outline displays a _pretty printed_ version of text from an article, looking a
lot like a markdown-rendered version of a web page.

Someone on Hacker News suggested [txtify.it](https://txtify.it/) as a
replacement to it. Indeed, Txtify is very similar to Outline, however it
displays plain text instead (i.e. no formatting at all).

Apparently some people even go further by installing [browser
extensions](https://github.com/iamadamdev/bypass-paywalls-chrome) to do so.

Ultimately, whenever possible, prefer to access news sources from news portals
that aren't paywalled and/or that you are a subscriber of.
