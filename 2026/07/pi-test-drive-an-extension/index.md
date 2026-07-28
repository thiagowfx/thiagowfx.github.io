---
title: "pi: test drive an extension"
url: https://perrotta.dev/2026/07/pi-test-drive-an-extension/
last_updated: 2026-07-28
---


**Problem statement**: using [pi](https://pi.dev/), install an extension
(package) as an one-off, without persisting it, for the sake of test-driving it,
akin to [`pre-commit try-repo`](https://pre-commit.com/#pre-commit-try-repo).

**Solution**:

```shell
% pi --help
[...]
--extension, -e <path> Load an extension file (can be used multiple times)
[...]
```

For example:

```shell
% pi -e npm:@tmustier/pi-usage-extension

added 1 package, and audited 2 packages in 1s

found 0 vulnerabilities
```

...then I can run `/usage` in that session.

