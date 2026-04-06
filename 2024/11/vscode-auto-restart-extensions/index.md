---
title: "VSCode: auto restart extensions"
url: https://perrotta.dev/2024/11/vscode-auto-restart-extensions/
last_updated: 2025-09-05
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

