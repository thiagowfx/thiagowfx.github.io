---
title: "Cloudflare: Email Workers"
date: 2025-01-11T01:48:44-03:00
tags:
  - bestof
  - dev
  - privacy
  - selfhosted
---

My journey into the
[serverless](https://en.wikipedia.org/wiki/Serverless_computing) world hereby
starts.

And I am very happy to have chosen [the best™
provider](https://www.cloudflare.com/) in the universe to delight me in this
sweet learning curve. ✨

**Problem statement**: I have my own domain, you have probably noticed that.

Given a specific hypothetical email address `neetflex@`[^1] within my own
domain, make it an email recipient that automatically forwards to both
`user1@example.com` and `user2@example.com`.

The first attempt involves setting up an [Email
Routing](https://developers.cloudflare.com/email-routing/) rule. The issue is
that you can only do 1:1 mappings: `neetflex@` -> `user1@example.com`
would work, but it is impossible to add `user2@example.com` for the same
recipient.

**Workaround**: [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/):

> With Email Workers you can leverage the power of Cloudflare Workers to
> implement any logic you need to process your emails and create complex rules.
> These rules determine what happens when you receive an email.

_Aside_: The platform is such a delight to use, I am deeply enchanted. Their
documentation is absolutely superb. I am getting seduced and couldn't agree more
with [Daniel
Miessler](https://danielmiessler.com/blog/google-has-opened-the-door-to-cloudflare).

I proceed to create an Email Worker with the following code[^2]:

```ts
export default {
  async email(message, env, ctx) {
    if (message.from !== "info@account.neetflex.com") {
      return;
    }

    for (const address of [
      // keep-sorted start
      "user1@example.com",
      "user2@example.com",
      // keep-sorted end
    ]) {
      await message.forward(address);
    }
  }
}
```

...named `neetflex-magic-link`.

There's an integrated testing tool that makes it a breeze to ensure my worker
logic works as intended.

Once I am satisfied with the results, I deploy the email worker.

**Final step**: create an email route rule from `neetflex@{domain}` to the
aforementioned email worker. Done, profit!$![^3].

At the time of this post, you can
[choose](https://developers.cloudflare.com/workers/languages/) among JavaScript,
TypeScript, Python and Rust to code your worker in.

Original idea:
[source](https://community.cloudflare.com/t/routing-an-email-to-more-than-one-address-from-the-same-user/437169/2)
from Cloudflare Community.

[^1]: Don't judge me if I am a fan of [neetcode](https://neetcode.io/)'s sense
    of humour.

[^2]: I miss(ed) programming in TypeScript! (even if only such a small snippet).

[^3]: _Literally_.
