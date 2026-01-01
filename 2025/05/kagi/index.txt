
**TL;DR**: [Kagi](https://kagi.com/) is a web search engine.

Why would you use something other than Google, you may ask? [That's out of scope
of this post](https://blog.kagi.com/age-pagerank-over). If you think Google is
the best and there's no need to replace your search engine, this post is not for
you.

A while ago I had [switched]({{< ref
"2024-12-24-switching-from-google-to-chatgpt-search" >}}) my default search
engine from Google to ChatGPT Search, but that didn't last long; eventually I
settled on [DuckDuckGo](http://duckduckgo.com/).

Last week, a friend told me he got a trial of Kagi. It wasn't the first time
I've heard of it: [John
Gruber](https://daringfireball.net/2025/04/try_switching_to_kagi) also blogged
about it.

Then I decided to try it out myself as well. In general I am happy with
DuckDuckGo, but we can always try something new, and the company materials have
really impressed me.

I emailed someone at the company and got an 1-month trial of their
[Professional plan](https://kagi.com/pricing)[^1] – which includes **unlimited**
searches. This is important: there should be no decision fatigue nor anxiety
about hitting a ceiling in the number of monthly searches.

What is Kagi? In a Nutshell:

> Kagi has no ads and is fully supported only by its users. We worked very hard
> to provide high quality, fast and tracking-free results at a minimum cost to
> ensure sustainability of our operation. By choosing a paid Kagi plan, you are
> also helping accelerate our mission of humanizing the web.

> Why should I pay for search?
>
> You're already paying with your time and attention to advertisers who
> manipulate your search results, waste your time, and exploit your privacy. Pay
> with your wallet instead of your life, and get pure, powerful search that
> works for you - not advertisers. Read more.

> What happens if I don't use any searches?
>
> In months where you don't utilize any searches on your plan, we will
> automatically apply a full credit to your account. This credit will be applied
> to your next billing cycle, effectively covering your subsequent month's
> subscription at no additional cost.

See also their [FAQ](https://help.kagi.com/kagi/faq/faq.html) and [privacy
policy](https://kagi.com/privacy):

> Why does Kagi return so few results?
>
> Kagi only shows you actually relevant search results, so you may be confused
> when Kagi returns 57 results and another, ad supported, search engine returns
> 2.6 million results. This is, in part, because ad supported search engines
> have different incentives and want you to stay on their site longer, going
> through pages and pages of results, as every interaction is another
> opportunity to serve ads.
>
> Kagi, conversely, strives to deliver the most relevant, unique results within
> the top three.

> What data does Kagi collect?
>
> Only bare necessities to run the service. Please see our privacy policy and
> our documentation about privacy protection for more information.

> Kagi's business model is unlike any other search engine in the world. This
> means we don't need or want your personal information (it would just be an
> unwelcome liability). By choosing this business model we know that we are
> going to have far less users than mainstream search engine for example, but we
> have also removed any incentive to misuse any information you have shared with
> us.
>
> Privacy is a Kagi Feature
>
> At Kagi, you are our customer, not the product being sold The deal is simple:
> Our customers pay for a service and we provide them with a service. This
> business model ensures Kagi's and our customers' interests are always aligned.
>
> We value your privacy, and whenever possible we will choose not to require or
> save any user data. For Kagi, user data is only a liability - we do not need
> or want it. Still, operating a paid service may require some basic information
> from our customers, and this document describes how we use it to the best of
> our ability.
>
> See for yourself Our technology choices show we're serious about privacy. You
> can check them in your browser.
>
> Unlike most websites, we do not load any analytics or telemetry.
>
> Unlike most search engines, we do not track which search result you choose to
> click.
>
> When viewing images, videos or other media results, or using the Kagi
> Assistant, we protect your privacy by proxying all connections and data
> through our servers.
>
> We store only the bare minimum of cookies, those required to handle basic
> application functionality, such as logging in.

I am currently digging through their
[documentation](https://help.kagi.com/kagi/). There's a lot to read! There's no
need to, but I am trying to assess whether to pay for them once the trial ends.

Overall I am quite bullish about them. I have already updated all my browsers in
all my devices (including work) to them. I believe immersion is a very effective
way to evaluate a product.

They support [bangs](https://help.kagi.com/kagi/features/bangs.html), just like
DuckDuckGo, meaning that I can append (for example) `!g` or `!ddg` to bail out
to Google or DuckDuckGo, respectively. I find their user experience around bangs
much better than DuckDuckGo's:

- first, there's a [bang explorer](https://kbe.smaertness.net/)
  (community-created), and the bang sources are
  [open](https://github.com/kagisearch/bangs)
- it's possible to add custom bangs
- it's possible to add custom search engines

As a practical example: I can invoke their
[Summarizer](https://kagi.com/summarizer) to make a summary of a page:

```
!sum <url>
```

Or "I am feeling lucky" with `! {search term}`.

There's [API access](https://help.kagi.com/kagi/api/overview.html).

There's built-in [Translation](https://blog.kagi.com/kagi-translate) (Kagi
Translate), accessible at
[https://translate.kagi.com/](https://translate.kagi.com/):

> Add translate.kagi.com/ before any URL for instant translation. No apps
> needed. Access 244 languages with zero tracking. Install our browser
> bookmarklet for quick access.
>
> Kagi Translate is free for everyone. If you're not a logged in Kagi user,
> you'll encounter a simple captcha to prevent automated abuse - a small step
> that helps us maintain quality while keeping the service free. Kagi members
> get direct access without captchas, integrating seamlessly with their existing
> workflow.

[Kagi Search Stats](https://kagi.com/stats): it keeps healthily growing.

[Kagi Performance](https://help.kagi.com/kagi/search-details/search-speed.html):
it is fast and lightweight.

If you append a question mark (`?`) to a search query, then it automatically
invokes a LLM (['quick
answer'](https://help.kagi.com/kagi/ai/quick-answer.html)) to summarize results:

> Even with an engine as powerful as Kagi you may not be interested in reading
> every resulting page and want a synthesis of the information as well as
> references to important pages in the search result. Kagi's Quick Answer
> quickly produces a summary of the results across the pages returned and
> provides references to the pages that are used. This functionality allows you
> to quickly consume the desired information from the search while giving you
> the pointers to dive deeper into the information if desired.
>
> Once you have search results returned you can select Quick Answer to quickly
> transform the information on the page into the easier to digest format.
> Additionally, if you add a question mark at the end of your query ("?") Quick
> Answers will trigger automatically, making it even more convenient to get to
> the information you need swiftly. You can also trigger Quick Answer by
> pressing 'q' on your keyboard, after the results have loaded.

I'll end this post now, otherwise I'd just be parroting the entire Kagi
Documentation here. **TL;DR**: So far, so good.

- - -

**Edit(2025-05-14)**: After using Kagi for about 10 days, I am happy to report
that I've been quite happy with them. There's no doubt they have a great
product.

The question to ask yourself is whether it's worth paying $10 / month for
their professional plan, or whether DuckDuckGo is enough for you. If you can
have your company expense them, then it's definitely a no-brainer.

[^1]: Their standard [trial](https://kagi.com/pricing) sign-up has a limitation
    of 100 searches.

