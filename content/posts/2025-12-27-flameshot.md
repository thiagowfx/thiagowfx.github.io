---
title: "Flameshot"
date: 2025-12-27T17:42:44-03:00
tags:
  - dev
  - macos
---

Install Flameshot.app on macOS:

```shell
brew install flameshot
sudo xattr -rd com.apple.quarantine /Applications/flameshot.app
open -a Flameshot
```

The `xattr` is [necessary](https://github.com/flameshot-org/flameshot/issues/3572) or else:

> "flameshot" cannot be opened because the developer cannot be verified
