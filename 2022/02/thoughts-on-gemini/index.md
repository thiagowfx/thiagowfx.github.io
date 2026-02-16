
From the [homepage](https://gemini.circumlunar.space):

> Gemini is a new internet protocol which:
>
> — Is heavier than gopher
> — Is lighter than the web
> — Will not replace either
> — Strives for maximum power to weight ratio
> — Takes user privacy very seriously

That's too abstract though. I prefer the way [Kev Quirk](https://kevq.uk/gemini-isnt-the-solution-to-the-broken-web/) puts it:

> To put that into human-digestible form; Gemini is basically a very light, text-only alternative to HTML.

Gemini aims to replace "lightweight HTML", but it already starts with a big barrier for entry and adoption: It's not obvious what it is by just reading its project homepage alone. This in my opinion comes off as elitist.

Furthermore, you need a custom piece of software in order to consume the so-called gemini _capsules_ (a fancy name for what's the equivalent of a plain-text [SSG](https://jamstack.org/generators/) website).

I tried out [`amfora`](https://github.com/makeworld-the-better-one/amfora) which is a popular CLI one[^1]. Amfora is pretty decent and lightweight. The experience is very similar to a hybrid of using a CLI RSS reader like [`newsboat`](https://newsboat.org) to keep track of your favorite capsules, and a CLI Web browser like `elinks` or `w3m` to navigate them.

And that's part of the adoption problem: Why would you subject yourself to purposely using a text-only browser in the 2020s? It is a painful experience, and there's not any extra value compared to just using a minimalist RSS reader like [miniflux](https://miniflux.app) to keep track of your favorite blogs / news portals via RSS.

Nowadays there are plenty of SSGs, for every programming language you can think of, even in plain shell scripting (POSIX `sh`). There's little reason to learn a new niche protocol given that it's relatively easy to publish simple blogs.

Conclusion: As Kev puts it:

> I'm not sure if you heard, but [The Web Is F*cked](https://thewebisfucked.com) and techies everywhere are touting the Gemini protocol as its saviour. I disagree. A lot.

I will end this article with a praise for Gemini, courtesy of [Drew DeVault](https://drewdevault.com/2020/11/01/What-is-Gemini-anyway.html). Drew argues that:

> My disdain for web browsers is well documented. Web browsers are extraordinarily complex, and any attempt to build a new one would be a Sisyphean task. Successfully completing that implementation, if even possible, would necessarily produce a Lovecraftian mess: unmaintainable, full of security vulnerabilities, with gigabytes in RAM use and hours in compile times. And given that all of the contemporary web browsers that implement a sufficiently useful subset of web standards are ass and getting assier, what should we do?

Fine, but the beloved plain duo of HTML + CSS still works just fine. There's no need to create a new, difficult-to-use protocol to _force_ people to keep things simple. Unless you just wanna have fun and treat it like a toy or learning project; then go for it. Nothing wrong with that.

My interest for Gemini ends as soon as this post is published. Q.E.D.

[^1]: [Packaged](https://repology.org/project/amfora/versions) for every relevant platform out there nowadays.

