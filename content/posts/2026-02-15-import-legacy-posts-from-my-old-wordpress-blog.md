---
title: "Import legacy posts from my old WordPress blog"
date: 2026-02-15T15:25:25+01:00
tags:
  - ai
  - dev
  - serenity
---

I used to have a blog during my university years.

It was in WordPress, hosted at https://thiagoperrotta.wordpress.com/, called
"Everyday Serendipity".

At first I would write in my mother tongue (Portuguese), then I would switch to
English. This was a great way to practice and improve my English back then.

At some point I deleted it. I know, I know, shame on me, [Cool URIs don't
change](https://www.w3.org/Provider/Style/URI).

However, as a future-conscious person even back then, I made a full backup
before doing so.

And now, fast-forward almost 10 years later, I find myself with the desire of
restoring it.

That was my weekend project!

I introduced a new tag: [legacy]({{< ref "/tags/legacy" >}}), under which I've been
slowly restoring my old posts, one by one.

There's one ground rule: I am not making any editorial changes to them. **All
posts are preserved as is**, including their poor grammatical errors and typos.
If anything, it's very cool to see how I've come a long way since then.

I am also not bothering to audit anything that may have become politically
incorrect since then. This is not social media.

The only active effort I am doing is to convert the original formatting from
WordPress to a markdown-friendly form, as supported by [Hugo](https://gohugo.io/).

I am also deleting and/or rephrashing a couple of sentences that point out to
dead links or that include images or videos that are no longer available.

## Workflow

First, download the backup file: `everydayserendipity.wordpress.2015-03-30.xml`.
To give you an idea of its size:

```shell
% wc -l everydayserendipity.wordpress.2015-03-30.xml
24165 everydayserendipity.wordpress.2015-03-30.xml

% du -sh everydayserendipity.wordpress.2015-03-30.xml
1.5M    everydayserendipity.wordpress.2015-03-30.xml
```

Then I asked an LLM ([Amp Code](https://ampcode.com)) to extract its posts,
noting that it is from a WordPress backup, to Hugo-friendly markdown.

I also asked it to add the legacy tag to all such posts, to make it easier for
me to identify them.

Afterwards I proceeded to read them one by one (nostalgia!), notice a couple of
poor formatting patterns, then asked the LLM to fix them one by one.

It's a bit tedious but it worked well! This is currently a work-in-progress:

```shell
% git st | wc -l
67
```
