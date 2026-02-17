---
title: "RSS: bridging the gap"
date: 2022-02-09T00:00:00+00:00
tags:
  - dev
  - socialmedia
---

Not everything is available via RSS. However, there are some decent workarounds in a few situations. For my RSS reader setup, see [Miniflux]({{< ref "2022-01-03-miniflux-rolling-my-own-rss-reader" >}}).

## Why This Matters

The shift away from RSS and open standards represents a broader trend of [enshittification](https://en.wikipedia.org/wiki/Enshittification) on the web—where platforms prioritize lock-in and data collection over user freedom. RSS embodies the original spirit of the open web: user control, interoperability, and freedom from algorithmic manipulation.

By using RSS bridges and alternatives, we push back against this trend and reclaim control over how we consume content online.

## Newsletters

Some blogs and authors refuse to provide RSS feeds to their websites. Instead, they will only provide newsletters.
This is very hostile to the open web, and the main reason why it's done is so that these authors can own a direct channel to reach out to their audience directly,
which is better for (their) business, making it easier for them to push sponsored and promoted content and measure engagement metrics and analytics.

[Kill the Newsletter](https://kill-the-newsletter.com/) is a service that proxies those newsletters, publishing them as RSS feeds.

You can either [self-host](https://github.com/leafac/kill-the-newsletter) it or use its official hosted version at https://kill-the-newsletter.com/.

## Twitter

Use Nitter:

> Nitter is a free and open source alternative Twitter front-end focused on privacy. The source is available on GitHub at https://github.com/zedeus/nitter

Furthermore, it has built-in RSS support!

For example, you can see @taylorswift13's profile on Nitter at https://nitter.net/taylorswift13
and follow her via RSS with https://nitter.net/taylorswift13/rss — by merely appending `/rss` to it.

You can either self-host it or use one of its [public instances](https://github.com/zedeus/nitter/wiki/Instances).
At the time of this writing the official instance is https://nitter.net.

## Reddit

Reddit famously includes RSS support for every subreddit, for example[^1]: https://www.reddit.com/r/archlinux/.rss.
It has a lot of noise though as it includes all recent posts including the ones with a few number of votes.

To experience a higher quality, filtered version of the latest given subreddit posts with more than a certain threshold (of your choosing) of upvotes, check out the [reddit-top-rss](https://github.com/johnwarne/reddit-top-rss) project:

> Reddit Top RSS is a set of scripts for Reddit's API that generates RSS feeds for specified subreddits with score thresholds. To preview your outputted feed items there is a front end that utilizes the Bootstrap v4 framework.

You're supposed to self-host it, but there's a demo version available at https://reddit-top-rss.herokuapp.com/.

## Appendix

For more RSS bridges and resources, see:

- https://github.com/RSS-Bridge/rss-bridge
- https://github.com/AboutRSS/ALL-about-RSS

**Disclaimer**: I do not endorse these lists of resources. Use them at your own risk.

[^1]: The last slash isn't strictly necessary: https://www.reddit.com/r/archlinux.rss is also valid.
