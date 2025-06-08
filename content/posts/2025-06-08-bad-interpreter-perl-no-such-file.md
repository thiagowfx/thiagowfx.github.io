---
title: "bad interpreter: perl: no such file or directory"
date: 2025-06-08T17:48:35+02:00
tags:
  - dev
---

The full error message is:

```shell
% ack -i nmap
zsh: /opt/homebrew/bin/ack: bad interpreter: /opt/homebrew/opt/perl/bin/perl: no such file or directory
```

This keeps happening, I am not sure why. [Previously]({{< ref
"2024-09-22-life-without-ack" >}}).

The fix is quite simple though:

```shell
% brew reinstall perl
```
