
**Problem statement**: you follow a blog author you like via RSS on
[miniflux](https://miniflux.app/), but you're not interested in a subset of
their posts. More specifically, you're not interested in posts that match
`https://example.com/interview/paul-atreides`.

Enter [miniflux entry filtering
rules](https://miniflux.app/docs/rules.html#filtering-rules):

> Since Miniflux 2.2.10, filtering rules can be defined for each feed and
> globally on the Settings page.

In this situation we're interested in the `EntryURL` field.

The following rule should work:

```ini
EntryURL=.*/interview/.*
```

