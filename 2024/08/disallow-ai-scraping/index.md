
Although there's never a guarantee, you can attempt to disallow "AI" from
scraping the posts in your blog, in the same spirit of "DNT — Do Not Track" in
modern web browsers.

If you have control over your
[`robots.txt`](https://perrotta.dev/robots.txt)[^1],
add something like the following to it:

```
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Claude-Web
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: cohere-ai
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: FacebookBot
Disallow: /

# Default rule
User-agent: *
Disallow:
```

The list above is non-exhaustive and will not be kept up-to-date, it's just
meant as a reference and/or starting point.

You could always use Gen AI itself to help you populate it, credits go to
https://grubz.blog/ai-scrapers-post/.

[^1]: You _really_ should.

