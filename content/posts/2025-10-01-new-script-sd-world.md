---
title: "New script: sd-world: perform a full system upgrade"
date: 2025-10-01T01:11:09+02:00
tags:
  - bestof
  - dev
---

[Previously]({{< ref "2024-01-28-sd-world" >}}).

> Whenever I want to upgrade any one of my systems, I run `sd-world`.

Now the script has evolved, being [hosted](https://github.com/thiagowfx/pancake/blob/9b2cc8c6df6103d4ab1457e30353fe0711290aa2/sd-world/sd-world.sh) in [pancake](https://github.com/thiagowfx/pancake):

- it handles interruptions (Ctrl-C) more efficiently (it was my biggest gripe)
- the output is more user-friendly
