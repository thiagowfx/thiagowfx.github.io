---
title: "Running multiple servers in a single bash script"
date: 2024-12-23T22:52:40-03:00
tags:
  - dev
---

Inspired by [Simon
Willison](https://github.com/simonw/til/blob/main/bash/multiple-servers.md)'s
TIL.

When I was working on the [Stadia](https://stadia.com/) Partner Portal as a
full-stack tech lead, I wrote and maintained a `run.sh` script that would start
up our two (front-end and back-end) Boq[^1] server instances.

It resembled the following:

```bash
#!/usr/bin/env bash

cleanup() {
  kill $pid_fe $pid_be
  exit 0
}

trap cleanup SIGINT

start_fe() {
  # [...init deps...]
  boq run //java/com/google/chrome/cloudcast/[...]/publishing/partnerportal/ui &
  pid_fe=$!
}

start_be() {
  # [...init deps...]
  boq run //java/com/google/chrome/cloudcast/[...]/publishing/partnerportal &
  pid_be=$!
}

start_fe
start_be

wait
```

This version is heavily simplified, but that was its gist. It worked perfectly.
Back in ~2018, it took quite a bit of trial-and-error to get it right. Now it
seems so easy to just ask GenAI to generate it for you! Yikes. Our profession
might get obsoleted in just a few more years to come...


[^1]: A proprietary / internal framework for web applications.
