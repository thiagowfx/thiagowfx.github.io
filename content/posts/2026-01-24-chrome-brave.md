---
title: "Chrome → Brave"
date: 2026-01-24T18:08:51+01:00
tags:
  - dev
  - privacy
---

[Earlier]({{< ref "2025-11-30-chrome-orion" >}}) I tried to switch from
Chrome to Orion (from the [Kagi](https://kagi.com/) folks). That did not last.

Even though Orion has various interesting and innovative features, it did
not prove to be stable for my workflow. There were various times it has totally
frozen or crashed, making me lose track of my open tabs. This is not acceptable,
reliability is prime.

You can only realize this by fully switching to it. It is not reproducible, it's
not idempotent; only "vibes" can make you perceive its instability.

I'd be willing to retry it in a few years. Not in 2026 though.

I am not even keeping it around as a secondary browser: I have simply
uninstalled it.

The situation on mobile is better. Orion for iOS is great. I've been using it as
my default iOS browser for ages. Presumably it is stable on iOS because it is
actually employing Safari / WebKit underpinnings, as every browser in iOS is
required to do.

Now let's go back to the elephant in the room: I did not want to switch back to
Google Chrome:

```shell
% brew uninstall google-chrome
==> Uninstalling Cask google-chrome
==> Backing App 'Google Chrome.app' up to '/opt/homebrew/Caskroom/google-chrome/141.0.7390.55/Google Chrome.app'
==> Removing App '/Applications/Google Chrome.app'
==> Purging files for version 141.0.7390.55 of Cask google-chrome
```

Upon re-evaluating my options, I decided to give Brave a try. There are many
things I dislike about Brave in terms of philosophy and politics (for example,
Web3 and Crypto), so I cannot endorse it in any way.

However, I realized there are many things that Brave does right out-of-the-box.
It has a very decent focus on privacy and adblocking. It strips off Google
telemetry and sync (e.g. bookmarks, passwords) features. Its performance and
stability is comparable to Chrome – well, they both use Chromium underneath.

I've been daily driving Brave as my default / main desktop browser for about 2
months now and I've been quite happy with it. It hasn't crashed at all, not even
once. All familiar Chromium features are there. All the Google-proprietary
nuisance is gone.

Again, I'd have a hard time to recommend Brave personally. Still, it has been
working well for me, so far.
