---
title: "miniflux: cull old posts"
url: https://perrotta.dev/2026/04/miniflux-cull-old-posts/
last_updated: 2026-04-02
---


Until a few months ago, I had the following in my `/etc/miniflux.conf`:

```conf {filename="/etc/miniflux.conf"}
[...]
# 3 years
FILTER_ENTRY_MAX_AGE_DAYS=1095
[...]
```

The intent is clear: every blog post older than 3 years would be automatically
filtered out. Including when subscribing to new feeds.

This has worked reliably for ages, until it didn't.

A few months ago, I kept seeing super old entries (many years old), all the
time.

I thought it was related to
[this](https://github.com/miniflux/v2/issues/4075#issuecomment-3940866237)
issue.

Today I had time to look deep into it and traced the pattern down to [this
snippet](https://github.com/miniflux/v2/blob/932e013590a8276e587e47cce7fd690202eb3c3e/internal/config/parser.go#L172):

```golang
if key == "FILTER_ENTRY_MAX_AGE_DAYS" {
    slog.Warn("Configuration option FILTER_ENTRY_MAX_AGE_DAYS is deprecated; use user filter rule max-age:<duration> instead")
}
```

Aha!

Then what? As per the [docs](https://miniflux.app/docs/rules.html#filtering-rules):

> `max-age:duration` - Match entries that are not older than a specific duration
> (e.g., max-age:7d for 7 days). Valid time units are "ns", "us" (or "µs"),
> "ms", "s", "m", "h", "d".

As such, now I have the following in Settings > Global Feed Settings > Entry
Blocking Rules[^1]:

```
EntryDate=max-age:730d
```

Old posts no more!

[^1]: Shortened from 3 to 2 years.

