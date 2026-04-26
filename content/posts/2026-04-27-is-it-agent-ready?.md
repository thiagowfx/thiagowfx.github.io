---
title: "Is it agent ready?"
date: 2026-04-27T01:34:34+02:00
tags:
  - ai
  - dev
---

[Is it agent ready?](http://isitagentready.com/) by Cloudflare:

> Scan your website to see how ready it is for AI agents. We check multiple
> emerging standards — from robots.txt and Markdown negotiation to MCP, OAuth,
> Agent Skills and agentic commerce.

How do I "perform"[^1]? See [perrotta.dev](http://isitagentready.com/perrotta.dev):

> Level 1 — Basic Web Presence
>
> - Discoverability: 67/100 (2/3): robots.txt and sitemap
> - Content: 0/1
> - Bot Access Control: 50/100 (1/2): robots.txt
> - API, Auth, MCP & Skill Discovery: 0/6

I see value in [Content Signals](https://contentsignals.org/):

> Introducing Content Signals, Cloudflare's implementation of a mechanism for
> allowing website publishers to declare how automated systems should use their
> content.

As such, I just updated my [robots.txt](https://perrotta.dev/robots.txt) with:

```
Content-Signal: search=yes, ai-train=no, ai-input=yes
```

"AI Input" is the _de facto standard_ in 2026, and I am a heavy user of Gen AI
agents myself, therefore there's no point to attempt to block it.

Nonetheless, I am still doing my best to flag AI training as disallowed.

[^1]: Achieving 100% scoring is not an end goal here. These metrics are
    arbitrary, by Cloudflare. I use them merely as an inspiration / starting
    point to decide what's worth to explore and/or adopt.
