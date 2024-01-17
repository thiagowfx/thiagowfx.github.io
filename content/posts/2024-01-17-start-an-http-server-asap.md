---
title: "Start an HTTP server ASAP"
date: 2024-01-17T16:41:41-03:00
tags:
  - dev
  - web
---

Sometimes I need to start a local HTTP server for a quick one-off task, often
just to serve static content. It is not important which one it is, so long as I
can do it quickly.

<!--more-->

## Option #1: use `python`

```shell
% python3 -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

This is often the most universal and convenient option, as `python` is widely
available out-of-the-box.

## Option #2: use `darkhttpd`

[`darkhttpd`](https://unix4lyfe.org/darkhttpd/) is available [almost
everywhere](https://repology.org/project/darkhttpd/versions).

```shell
% darkhttpd .
darkhttpd/1.14, copyright (c) 2003-2022 Emil Mikulic.
listening on: http://0.0.0.0:8080/
```

Their own `README` states:

> When you need a web server in a hurry.

This is the most convenient option when you are in control of a package
manager, as it is one installation command away from your system. In
particular, it's available in both homebrew and nixpkgs.

## Option #3: use `nodejs`

```shell
% npx http-server -p 8000
Starting up http-server, serving ./

http-server version: 14.1.1

http-server settings:
CORS: disabled
Cache: 3600 seconds
Connection Timeout: 120 seconds
Directory Listings: visible
AutoIndex: visible
Serve GZIP Files: false
Serve Brotli Files: false
Default File Extension: none

Available on:
  http://127.0.0.1:8000
Hit CTRL-C to stop the server
```

If you're already within the node ecosystem, this is also just one installation
away. I would typically not recommend this setup though if you don't already
have `npm` installed on your system.

## Option #4: use `busybox`

This option seemed very attractive for use on Linux systems:

```shell
% busybox httpd -f -p 8080
```

However in an up-to-date Alpine Linux system (3.20) it does not work:

```shell
% busybox httpd -f -p 8080
httpd: applet not found
```

Therefore I don't consider it universal enough.

**Reference**: https://gist.github.com/willurd/5720255
