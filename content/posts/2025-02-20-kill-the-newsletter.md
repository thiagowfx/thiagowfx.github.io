---
title: "Kill the Newsletter"
date: 2025-02-20T15:34:30+01:00
tags:
  - dev
  - privacy
---

I don't like to sign up for newsletters. They are too noisy, pollute my inbox,
and have a lot of tracking built-in.

Instead, I prefer RSS.

Most newsletters provide a way to subscribe to them via RSS. Notably, Medium and
Substack do so. Most...but not all.

What to do when the only option is a newsletter? A popular example: James
Clear, author of Atomic Habits, with his [3-2-1
Thursday](https://jamesclear.com/newsletter) newsletter.

Use [Kill the Newsletter](https://ktnrs.com/) by Leandro Facchinetti.

Usage is quite simple:

- create a new entry e.g. "foo"
- it will generate an email e.g. `abcdef@ktnrs.com`
- it will generate a RSS feed e.g. `https://ktnrs.com/feeds/abcdef.xml`
- use the email to sign up for the newsletter
- use the RSS feed to subscribe to in your feed reader

And that's it!

> Don't share these addresses.
>
> They contain an identifier that other people could use to send you spam and to
> control your newsletter subscriptions.

It's [open source](https://github.com/leafac/kill-the-newsletter):

> Convert email newsletters into Atom feeds

Most blogs I subscribe to provide RSS feeds out-of-the-box, therefore I don't
see the need to self-host this service merely for a few one-offs.
