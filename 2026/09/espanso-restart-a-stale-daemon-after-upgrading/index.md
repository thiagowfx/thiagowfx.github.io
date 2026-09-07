---
title: "espanso: restart a stale daemon after upgrading"
url: https://perrotta.dev/2026/09/espanso-restart-a-stale-daemon-after-upgrading/
last_updated: 2026-09-07
---


**Problem statement**: why did Espanso stop expanding text while its service was
running?

The CLI reported a healthy service on version 2.4.1:

```shell
% espanso --version
2.4.1
% espanso status
espanso is running
```

The daemon log disagreed:

```shell
% rg 'espanso version:' ~/Library/Caches/espanso/espanso.log | tail -1
16:50:24 [daemon(2251)] [INFO] espanso version: 2.4.0
```

The app had been upgraded on September 3, but the launcher and daemon still
came from August 24. Restarting the worker had not replaced either one:

```shell
% ps -p 1899,2251,92631 -o pid,lstart,command
  PID STARTED                      COMMAND
 1899 Mon Aug 24 16:50:17 2026     /Applications/Espanso.app/Contents/MacOS/espanso launcher
 2251 Mon Aug 24 16:50:23 2026     /Applications/Espanso.app/Contents/MacOS/espanso daemon
92631 Mon Sep  7 14:55:26 2026     /Applications/Espanso.app/Contents/MacOS/espanso worker --monitor-daemon --start-reason manual_restart
```

A full service restart replaced all three processes:

```shell
% espanso service restart
% ps -p "$(pgrep -d, -f '/Applications/Espanso.app/Contents/MacOS/espanso (launcher|daemon|worker)')" -o pid,lstart,command
  PID STARTED                      COMMAND
 3049 Mon Sep  7 15:01:47 2026     /Applications/Espanso.app/Contents/MacOS/espanso launcher
 3063 Mon Sep  7 15:01:47 2026     /Applications/Espanso.app/Contents/MacOS/espanso daemon
 3064 Mon Sep  7 15:01:47 2026     /Applications/Espanso.app/Contents/MacOS/espanso worker --monitor-daemon
% rg 'espanso version:' ~/Library/Caches/espanso/espanso.log | tail -1
15:01:47 [daemon(3063)] [INFO] espanso version: 2.4.1
```

Text expansion worked again.

So now I'll need to remember to restart `espanso` whenever it is upgraded.

