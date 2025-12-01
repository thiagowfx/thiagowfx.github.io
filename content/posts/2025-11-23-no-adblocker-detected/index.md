---
title: "No adblocker detected"
date: 2025-11-23T00:23:26-03:00
tags:
  - dev
  - selfhosted
  - serenity
---

https://maurycyz.com/misc/ads/:

> Internet ads are horrible: They waste your time, and the advertising industry
> makes the internet a worse place. Payouts are so small that the only way to
> survive is to turn your site into an ad filled hellhole with no real
> substance.
>
> If you want to support your favorite authors: send them money. A dollar helps
> more than viewing ads ever would.
>
> However, most people see advertising as a part of the internet experience, which is why I added this message to my site:
>
> > No adblocker detected. Consider using an extension like uBlock Origin to
> > save time and bandwidth. Click here to close.
>
> It's shown off to the side, and never covers content. It won't be shown if
> there isn't enough space. The close button actually works and it stays closed.
>
> The specific recommendation is important because a lot of people have only
> heard of adblockers from ads. Commercial adblockers range from sketchy to
> outright scams: If they are paying to be promoted, they must expect to make
> money from users.

This is a very cool activist idea.

I prototyped it in this blog:

![ad](ad.webp)

However I would need to add a cookie in order to implement the close button
effectively, and I'd rather not do so.
