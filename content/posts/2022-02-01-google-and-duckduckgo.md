---
title: "Google and Duckduckgo"
date: 2022-02-02T18:51:00-05:00
tags:
  - privacy
  - selfhosted
---

My search engine of choice is [Google][google], nonetheless I still enjoy [DuckDuckGo][duckduckgo] occasionally.

The main reason to stick with Google is its superior quality, by the means of better search results. 20 years later, it's still arguably the best search engine. Of course, part of the reason for that is contingent upon how much data it collects, but that's a topic for another day...

There are at least three reasons to use DuckDuckGo as an _alternative_:

- it's privacy-focused, there's no tracking and no bubbling[^1]
- its search results stem from sources other than Google; these days, mostly from Bing
- it has [**!bangs**][bangs], lots of them

The quest(ion) then becomes: How can I use mostly Google, but still have quick access to DuckDuckGo bangs?

<!--more-->

There are several ways to do so.

## DuckDuckGoog

[DuckDuckGoog][duckduckgoog] is a search engine which does exactly that:

> Searches Google and !bangs DuckDuckGo. Tell your browser!

- If I search for `i3`, it will open https://www.google.com/search?q=i3 and probably think I am interested in Intel i3 CPUs.
- If I search for `!aw i3`, using the ArchWiki bang, it opens https://wiki.archlinux.org/title/I3 and goes straight to the `i3` window manager page in the ArchWiki, exactly what I wanted.
- If I search for `!ddg i3`, it opens https://duckduckgo.com/?q=i3, on DuckDuckGo.

Caveat: You cannot add custom search engines to Safari, therefore this method only works in other browsers (Firefox, Chrome, etc).

### Self-Hosted

DuckDuckGoog [claims][duckduckgoog-privacy] to collect no data:

> It's quite simple. DuckDuckGoog doesn't track any queries submitted whatsoever, It simply redirects you to DuckDuckGo or Google depending on whether your search contains a !bang or not.

If you still don't trust it for some reason, you could also self-host it in your own server, as it's [open source][duckduckgoog-source].

One advantage of doing so is using (and owning) your own infrastructure, which is probably more reliable in terms of bandwidth and latency than a random guy's server in the wild.

## !Bang Quick Search

[!Bang Quick Search][bang-quick-search] is a Chrome extension:

> This extension adds DuckDuckGo !bang search to chrome. You can use it from the URL bar as long as your default search engine is either google or bing (for now). You can also use it directly on google's and bing's websites.

So long as your search engine is set to either Google or Bing, it will intercept `!bangs` from your query to redirect them to DuckDuckGo.

Tip: Use `!ddg` to search on DuckDuckGo.

Caveat: As a Chrome extension, it obviously only works in Chrome (or any of its derivatives like Edge or Vivaldi).

## DuckDuckGo

Another simple way is to just use DuckDuckGo directly. Whenever you want to go to Google, just add `!g` to your query.

## Final words

I used all three methods in the past. My favorite one these days is the Chrome Extension because Chrome is my current browser.

As a fallback I find that using DuckDuckGo directly is acceptable as well, however it quickly becomes quite annoying to constantly add `!g` to every query. Defaults matter.

## Related

- [Switching to DuckDuckGo](https://blog.meain.io/2019/switching-to-duckduckgo/)


[google]: https://google.com/
[duckduckgo]: https://duckduckgo.com/
[bangs]: https://duckduckgo.com/bang
[duckduckgoog]: https://www.duckduckgoog.com/
[duckduckgoog-source]: https://github.com/mikecrittenden/duckduckgoog
[duckduckgoog-privacy]: https://www.duckduckgoog.com/privacy
[bang-quick-search]: https://chrome.google.com/webstore/detail/bang-quick-search/kcopjlobikiakoacoadbnghpdcmngali

[^1]: Biased search results based on your past searches.