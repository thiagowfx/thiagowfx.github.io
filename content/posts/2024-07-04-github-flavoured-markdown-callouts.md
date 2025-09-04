---
title: "Github-flavoured Markdown: Callouts"
date: 2024-07-04T10:17:08+02:00
tags:
  - dev
---

Since the end of the last year it's possible to add callouts to markdown files
on GitHub. They are treated specially and rendered in a visually distinct way:

```md
> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
```

In the spirit of [xg2xg](https://github.com/jhuangtw/xg2xg), this feature has a
direct 1:1 mapping with the classic g3doc callouts at Google (except for
"caution"):

```md
Note: This is a note.

Tip: This is a tip.

Warning: This is a warning.

Important: This is important.
```

Sources:

- https://github.blog/changelog/2023-12-14-new-markdown-extension-alerts-provide-distinctive-styling-for-significant-content/
- https://github.com/orgs/community/discussions/16925
