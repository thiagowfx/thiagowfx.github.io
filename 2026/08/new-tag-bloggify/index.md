---
title: "new tag: bloggify"
url: https://perrotta.dev/2026/08/new-tag-bloggify/
last_updated: 2026-08-16
---


[Previously]({{< ref "2026-06-09-bloggify" >}}).

**Problem statement**: some readers may not want AI-assisted posts in their feed
reader, even with my edits. I support making it easier for people to opt out
from such posts. They should be able to filter them out without unsubscribing
from the whole blog.

Every post the [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md)
skill drafts already carries a footer disclosing it. What was missing was a
machine-readable signal, not just a line at the bottom a feed reader can't act
on. So I grepped for the marker and tagged every post that has it:

```shell
% grep -rl "Drafted with \[\`/bloggify\`\]" content/posts/ | wc -l
27
```

```shell
% git show 79018e8cf1 -- content/posts/2026-06-09-bloggify.md
diff --git content/posts/2026-06-09-bloggify.md content/posts/2026-06-09-bloggify.md
index b0a5a8ee86..9d15d656fd 100644
--- content/posts/2026-06-09-bloggify.md
+++ content/posts/2026-06-09-bloggify.md
@@ -3,6 +3,7 @@ title: "bloggify"
 date: 2026-06-09T16:50:11+02:00
 tags:
   - ai
+  - bloggify
   - claude
   - dev
   - meta
```

Every post's `tags:` list ends up in the RSS `<item>` as a `<category>`
element, one per tag (see `layouts/_default/rss.xml`). So `bloggify` is now a
regular, filterable category in the feed, same as any other tag.

For those of you who use [Miniflux](https://miniflux.app/), filtering it out is the same trick from
[blocking an entry matching a URL]({{< ref
"2026-02-13-miniflux-block-entry-matching-url" >}}) and the [global
blocklist]({{< ref "2024-12-28-miniflux-global-blocklist" >}}), except on the
`EntryTag` field instead of `EntryURL` or `EntryTitle`:

```ini
EntryTag=(?i)^bloggify$
```

Added as a global block rule in miniflux, and every future `/bloggify`-drafted
post never reaches the inbox. `/tags/bloggify/` on the blog itself works too,
for anyone who'd rather subscribe to the opposite: only the AI-assisted posts.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

