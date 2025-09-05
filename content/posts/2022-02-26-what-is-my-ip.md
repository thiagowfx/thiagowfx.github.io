---
title: "What is my IP?"
date: 2022-02-26T17:55:38-05:00
tags:
  - dev
---

This post contains a small handful of distinct services to query your machine
external IP address.

## [Google](https://www.google.com/search?q=what+is+my+ip)

URL: https://www.google.com/search?q=what+is+my+ip

As of this writing, this doesn't work on duckduckgo:
https://duckduckgo.com/?q=what+is+my+ip. I suppose this is related to their
philosophy of not tracking their users.

This is the easiest method when you have a web browser as you do not need to
memorize any URL.

## [I can haz ip](https://icanhazip.com/)

URL: https://icanhazip.com/

```shell
$ curl icanhazip.com
NNN.NNN.NNN.NNN
```

I love the simplicity of _I can haz ip_. It just returns your IP address in
plain text, nothing else. It also works from the web browser. You can find
details about it [in the FAQ](https://major.io/icanhazip-com-faq/). **TL;DR**: It was
an [open source](https://github.com/major/icanhaz) pet project of a single
person ([Major Hayden](https://major.io/)), then it was eventually bought by
Cloudflare as it immensely grew.

It's also possible to query your IPv6 address [in case you have
one](https://apenwarr.ca/log/20170810):

```shell
$ curl -6 icanhazip.com
```

## [IPInfo](https://ipinfo.io/)

URL: https://ipinfo.io/

IPInfo returns structured data beyond just your IP address. There are several
similar services that do this, for example, [What is my
IP?](https://www.whatismyip.com/) and https://ifconfig.co/, however IPInfo is the cleanest one I have
seen.

## [ping.eu](https://ping.eu/)

URL: https://ping.eu/

I'll also give an honourable mention to ping.eu as it contains a small handful
of utilities to check for things like Traceroute, DNS, whois, port check, etc.

## [`ifconfig.io`](https://ifconfig.io/)

**Update** (2024-07-11): Add `ifconfig.io`.

URL: https://ifconfig.io/

```shell
$ curl ifconfig.io
```
