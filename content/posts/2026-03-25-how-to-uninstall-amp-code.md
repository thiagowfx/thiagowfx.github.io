---
title: "How to uninstall Amp Code"
date: 2026-03-25T11:48:21+01:00
tags:
  - ai
  - dev
---

[Previously]({{< ref "2026-03-25-goodbye-amp-code" >}}).

The [Amp Code Manual](https://ampcode.com/manual) does not contain
uninstallation instructions.

It contains _only_ installation instructions.

Every software installation method _should_ have an easy way to be reverted.

I hereby fill in this gap.

**How to uninstall Amp Code from your system?**

It's likely installed globally via `npm`. To remove it:

```shell
# 1. Remove the npm package
npm uninstall -g @sourcegraph/amp

# 2. Remove data directory
rm -rf ~/.amp

# 3. Remove config (symlinked from my dotfiles)
rm -rf ~/.config/amp
```
