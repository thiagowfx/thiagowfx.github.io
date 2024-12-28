---
title: "Site performance with Lighthouse"
date: 2024-12-28T05:14:38-03:00
tags:
  - dev
  - selfhosted
---

Lighthouse can be used to assess overall site performance. There is a myriad of
ways to run it:

- Google (cloud): https://pagespeed.web.dev/
- Chrome DevTools (locally): Lighthouse tab
- CLI tool: https://github.com/GoogleChrome/lighthouse
- Github Actions: https://github.com/GoogleChrome/lighthouse-ci

It has four metrics scored from 0 to 100 each:

- performance
- accessibility
- best practices
- SEO

I ran it against [my blog](https://pagespeed.web.dev/analysis/https-perrotta-dev/f7pfqerk0f?form_factor=mobile).

My score was 100 / 83 / 96 / 100, respectively, which is quite good. It's not
unexpected either, because I am running a static website.

It offered me a couple of suggestions:

> - Image elements do not have explicit width and height
> - Serve images in next-gen formats Potential savings of 18 KiB
> - Serve static assets with an efficient cache policy 2 resources found
> - Properly size images Potential savings of 23 KiB

I addressed most of the suggestions.
