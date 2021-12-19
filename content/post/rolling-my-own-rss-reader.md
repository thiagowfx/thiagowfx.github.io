---
title: "Miniflux: Rolling my own RSS Reader"
date: 2021-12-19T12:52:56-05:00
draft: true
---

This article describes my experience setting up and using the [Miniflux](https://miniflux.app/) RSS reader.

<!--more-->

## Journey: The Early Years

I always kind of enjoyed following blogs via RSS, even though RSS has never been a key part of my workflow. That said, I am not here to convince you why RSS is great, there are great existing resources[^kevq] out there that do a better job than me to describe that.

My journey was roughly as follows:

**2010(?) - 2012(?)**: Google Reader. Very lightweight, occasional usage. Then Google Reader was [killed](https://en.wikipedia.org/wiki/Google_Reader).

2013 - 2019: Social media (mainly Facebook, Twitter and Reddit) shadowed RSS existence off my life. I mostly resorted to 'liking' and 'following' my favorite authors and/or projects through them. It was never great because there was a lot of cruft: ads (that became increasingly frequent over the years), fluff, noise. I always knew I had to try something different.

During those years I have occasionally tried Feedly and Inoreader, which are hosted solutions. They are kind of OK, especially if you only have a handful of feeds. Their free offerings are quite decent, with a limit of a hundred or so feeds. They also have native mobile apps (Android, iOS) which are a must these days. I was never fully converted, though. Some common barriers:

- their recommendations and 'machine learning' was a consistent source of stress, with a fear of missing out (FOMO) similar to social media. I felt pressured to keep following new blogs just like I am pressured to constantly 'like' and 'follow' new pages in tradicional American social media.

- a lot of context switching: many RSS feeds aren't great and provide excerpts (summaries) only, meaning I'd always have to visit the website directly if I wanted to read full articles. This doesn't scale well long term, attention is a precious resource and our brains aren't great at keeping steady attention if we keep context switching. A classical example of this is [Paul Graham's RSS feed](http://www.aaronsw.com/2002/feeds/pgessays.rss).

- lack of ability to filter out certain posts from a feed: for example, sponsored posts, ads and alike. Or posts with certain keywords in their titles. A classical example is [John Gruber's Daring Fireball](https://daringfireball.net/) sponsored posts which usually have 'Sponsor' in their titles. Why do I have to manually skip these posts, why can't my RSS software automatically do it for me?

- lock-in: if I star/save posts that I like for future reference, they would be stuck in the specific cloud provider I chose.

These were some of my gripes.

During those years I had also occasionally tried to self-host [TinyTinyRSS](https://tt-rss.org/) but it didn't really scale for me. First, I wasn't a seasoned sysadmin; second, I didn't have any cloud resources nor local server in my home, an instance in my laptop doesn't really scale; third, its stack is relatively bloated, requiring a full PHP installation alongside a webserver (apache, nginx or similar) and a database. Suddenly there was a lot of complexity to maintain all that.

Then 2020 and the COVID-19 pandemic came along.

## Journey: The Shift from Social Media to RSS

Suddenly many people had a lot of extra time on their hands.

TODO(thiagowfx): Continue this post.

[^kevq]: https://kevq.uk/please-add-rss-support-to-your-site/
