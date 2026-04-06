---
title: "git: list branches by recent activity"
url: https://perrotta.dev/2025/10/git-list-branches-by-recent-activity/
last_updated: 2026-01-03
---


Tweak `~/.gitconfig`:

```ini
[alias]
  xl = branch -vv

[branch]
	sort = -committerdate
```

**Result**: `git xl` will print your repository branches sorted by the most
recent ones in terms of activity, instead of the alphabetical default.

I have this setting for a long time, and IMHO it's a better default.

[This post](https://tekin.co.uk/2021/11/listing-most-recent-git-branches) by
Tekin Süleyman prompted me to share it.

