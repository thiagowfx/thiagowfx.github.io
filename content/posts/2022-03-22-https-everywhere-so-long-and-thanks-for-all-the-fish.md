---
title: "HTTPS Everywhere: So long and thanks for all the fish"
date: 2022-03-22T01:09:13-03:00
tags:
  - privacy
  - security
---

EFF's[^1] [HTTPS Everywhere](https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp) is a browser extension available for all major browsers that automatically upgrades HTTP to HTTPS on supported websites.

Other than adblocking, it's one of the first extensions I add to a fresh browser installation.

Today I learned it is apparently not needed anymore. Both Google Chrome and Firefox have settings these days to perform exactly the same functionality of the extension.

In Google Chrome do: [chrome://settings](chrome://settings) -> Security and Privacy -> Advanced -> Toggle 'Always use secure connections' on.

In Firefox the option is located on Settings -> Privacy & Security -> HTTPs only mode.

[^1]: EFF is a big proponent and advocate for a secure web, being one of the core responsible actors for [certbot](http://certbot.eff.org) and [Let's Encrypt](https://letsencrypt.org).
