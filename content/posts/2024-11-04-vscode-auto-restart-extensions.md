---
title: "VSCode: auto restart extensions"
date: 2024-11-04T11:34:36+01:00
tags:
  - dev
---

Whenever I open VSCode, there are some extension updates. Every time, I need to
manually click "Extensions" in the left-side navigation bar and then "Restart"
so that the upgrades take effect.

This should be automated.


There is a solution: add the following to your `settings.json` (`Cmd + ,`)

```json
"extensions.autoRestart": true
```

Documentation:

> // If activated, extensions will automatically restart following an update if
> the window is not in focus.

**Source**: https://code.visualstudio.com/docs/getstarted/settings
