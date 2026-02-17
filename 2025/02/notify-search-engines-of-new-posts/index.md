
I have the following rule in the [`Justfile`](https://just.systems/man/en/) of
this blog:

```justfile
# Ping Google and Bing about changes in the sitemap
ping sitemap="https://perrotta.dev/sitemap.xml":
	curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
	curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"
```

It is invoked with `$ just ping`.

Recently I added it to CI (GitHub Actions):

```yaml
steps:
  - name: Build
    run: just build
  - name: Deploy
    [...]
  - name: Ping search engines
    run: just ping
```

Whenever I publish a new post, a sitemap notification is triggered.

When writing this post, I learned this is just wishful thinking.

Upon visiting https://google.com/ping:

> Sitemaps ping is deprecated. See
> https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping.
>
> Error 404

Deeper into the rabbit hole:

> The Sitemaps Protocol was introduced in 2005 to help search engines with the
> discovery of new URLs, and also to help with scheduling new crawls of already
> discovered URLs. It's a wildly popular protocol that hasn't changed for over
> 15 years. While the general idea is still useful, some aspects have become
> less practical in today's internet.

> To that end, we're announcing deprecation of the sitemaps "ping" endpoint and
> providing additional recommendations for the use of the lastmod element.

> The sitemap protocol defines an unauthenticated REST method for submitting
> sitemaps to search engines. Our internal studies—and also other search engines
> such as Bing—tell us that at this point these unauthenticated sitemap
> submissions are not very useful. In fact, in the case of Google Search, the
> vast majority of the submissions lead to spam. To wit, we're deprecating our
> support for sitemaps ping and the endpoint will stop functioning in 6 months.
> You can still submit your sitemaps through robots.txt and Search Console, but
> the HTTP requests ("pings") to the deprecated REST endpoint will result in a
> 404 error. Any existing code or plugins which use this endpoint will not cause
> problems for Google Search; you don't need to make any changes (but using the
> endpoint will also not do anything useful).

I'll keep pinging it anyway, the cost is virtually free. You can't just
[deprecate](https://killedbygoogle.com/) features people [rely
on](https://www.hyrumslaw.com/).

