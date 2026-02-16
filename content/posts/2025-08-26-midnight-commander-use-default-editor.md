---
title: "midnight commander: use default editor"
date: 2025-08-26T14:55:25+02:00
tags:
  - dev
---

[Previously]({{< ref "2025-08-26-git-ignore-changes-to-tracked-files" >}}).

When using [midnight commander](https://midnight-commander.org/) to edit files
(with the default `F4` keybinding), it defaults to using
[`mcedit(1)`](https://man.archlinux.org/man/mcedit.1):

> mcedit — Internal file editor of GNU Midnight Commander

This is not great for my muscle memory.
I'd rather use my `$EDITOR`[^1].

```
% GIT_PAGER=cat git show
commit 8ffb7995db8d845ca227a6e5360124bef3680113 (HEAD -> master, origin/master, origin/HEAD)
Author: Thiago Perrotta <{redacted}>
Date:   Tue Aug 26 14:54:48 2025 +0200

    mc: use_internal_edit

diff --git mc/.config/mc/ini mc/.config/mc/ini
index 487267e..13b7643 100644
--- mc/.config/mc/ini
+++ mc/.config/mc/ini
@@ -1,2 +1,3 @@
 [Midnight-Commander]
 skin=modarin256
+use_internal_edit=false
```

[^1]: Currently: `vim`.
