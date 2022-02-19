---
title: "Miniflux: Rolling my own RSS Reader"
date: 2022-01-03T17:56:56-05:00
tags:
  - linux
  - rss
  - selfhosted
showtoc: true
---

This article describes my experience transitioning to, setting up and using the
[Miniflux](https://miniflux.app/) RSS reader for the first time.

<!--more-->

## Preamble

I always kind of enjoyed following people and blogs via RSS, even though it has never been a key part of my workflow (nor of the mainstream web). That said, I am not here to convince you why RSS is great, there are good existing resources[^kevq][^laura] for that already.

Initially I had used Commafeed, Feedly and Inoreader, which are hosted solutions. They are mostly OK, especially if you only have a handful of feeds. Their free offerings are quite decent, with a limit of a hundred or so feeds. They also have mobile clients (Android, iOS) which are a must these days. I was never fully converted to them though, and my workflow therein would only last for a few weeks or months. Some common barriers were:

- their recommendations and 'machine learning' fluff were a consistent source of stress, with a fear of missing out (FOMO) akin to social media. I felt pressured to keep following new blogs just like I am pressured to constantly 'like' and 'follow' new pages in traditional American social media.

- there was a lot of context switching: many upstream RSS feeds aren't great, for example, by providing excerpts (summaries) only I'd always have to visit the website directly if I wanted to read full articles. This doesn't scale well long term, attention is a precious resource and our brains aren't great at keeping steady and focused attention if we constantly context switch. A classical feed like this is [Paul Graham's](http://www.aaronsw.com/2002/feeds/pgessays.rss).

- there was no ability to filter out (exclude) posts from feeds. For example, deleting posts with a certain title (Sponsor, Ad, some boring mainstream topic). A classical example is [John Gruber's Daring Fireball](https://daringfireball.net/) sponsored posts which usually have 'Sponsor' in their titles. Why do I have to manually skip these posts, why can't I teach my RSS reader to do it automatically for me?

- lock-in: whenever I starred/saved posts that I liked for future reference, they would be stuck in the specific cloud provider I chose.

These were some of my gripes.

During those years I had also tried to self-host [TinyTinyRSS][tinytinyrss] but it didn't really last for me:

1. first, its stack is relatively bloated: hosting and maintaining a typical LAMP stack takes some considerable amount of effort — TinyTinyRSS requires a full PHP installation alongside a webserver (apache, nginx or similar) and a database. Suddenly there was a lot of complexity to maintain all that.

2. second, I didn't have any cloud resources (VPS), nor a local server in my home (e.g. a Raspberry Pi or a NUC or a NAS Appliance). An instance in my personal laptop wouldn't really scale either as I would have needed it to be always on if I wanted to have continuous access to it (e.g. from my phone).

3. third, I wasn't a seasoned sysadmin at the time and wasn't really looking forward to self-host.

Then 2020 and the COVID-19 pandemic came along with all of its imposed
government lockdowns worldwide. Suddenly many people had a lot of free time on
their hands.

## Self-hosting at home

Having an [Arch Linux](https://archlinux.org/) workstation at home, it felt natural to try out Miniflux there first.

Miniflux has great upstream [documentation](https://miniflux.app/docs/installation.html#debian) already, therefore it's just a matter of following it. It's out of scope of this post to duplicate the installation process here, however I will add a bit of color regarding my initial setup.

**Disclaimer**: Those instructions will probably get out-of-date at some point.

Thankfully there's already a miniflux [package](https://archlinux.org/packages/community/x86_64/miniflux/) for Arch, making my job much easier. Installing miniflux alone isn't enough though, we will also need to install a database server (PostgreSQL):

```shell
$ sudo pacman -Syu miniflux postgresql
```

The next step is to configure the PostgreSQL server. Refer to the upstream documentation for that, but the TL;DR is:

- create a `miniflux` user
- create a `miniflux` database owned by the `miniflux` user
- perform a few tweaks (extension hstore)

Then configure miniflux:

```shell
$ cat /etc/miniflux.conf
# Purge articles after a few days: These values are actually the default. Listed here just for reference.
CLEANUP_ARCHIVE_READ_DAYS=30
CLEANUP_ARCHIVE_UNREAD_DAYS=90

# Database configuration
DATABASE_URL=user=miniflux password=<password> dbname=miniflux sslmode=disable
RUN_MIGRATIONS=yes
```

We will also need to create an admin user for miniflux with `miniflux --create-admin`.

Then we start the database server and miniflux:

```shell
$ sudo systemctl enable --now postgresql miniflux
```

Afterwards it's just a matter of navigating to http://localhost:8080 and logging in with your newly created admin user.

Miniflux is a pleasure to use, and it's very easy to get acquainted with it.

It's also possible to add custom CSS in its Settings. I added the following tweaks[^system-font-stack] for improved typography:

```css
:root {
  --system-font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-family: var(--system-font-family);
  --entry-content-font-family: var(--system-font-family);
}

body {
  max-width: 900px;
}

textarea[name="custom_css"] {
  min-height: 300px;
  width: -webkit-fill-available;
}
```

**Update(2022-02-18)**: It turns out the CSS above isn't really needed as a system font stack is set out-of-the-box.

The one main limitation of running Miniflux this way is that you'll need your workstation to be always on if you want to have continuous access to it. This means if you want to read late at night you'll need to leave your computer on. Not only this is impractical and inconvenient, it's also not much environmentally friendly.

Another limitation is that in principle you'll only be able to access Miniflux from home, unless you take extra measures[^extra-measures] to make your workstation accessible from outside your home network.

## Other resources

Miniflux clients:

- **Miniflux web app** (PWA), works well enough
- [Unread](https://apps.apple.com/us/app/unread-an-rss-reader/id1363637349) (iOS) via Fever API, gesture based
- [Reeder](https://reederapp.com/) (iOS) via Fever API
- [newsboat](https://newsboat.org/releases/2.21/docs/newsboat.html#_miniflux) (CLI)

Common self-hosted alternatives to miniflux:

- [FreshRSS][freshrss]
- [TinyTinyRSS][tinytinyrss]
- [Feedbin][feedbin] (harder to self-host)


[feedbin]: https://feedbin.com/
[freshrss]: https://freshrss.org/
[tinytinyrss]: https://tt-rss.org/

[^kevq]: https://kevq.uk/please-add-rss-support-to-your-site/
[^laura]: https://laurakalbag.com/subscribe/
[^system-font-stack]: https://css-tricks.com/snippets/css/system-font-stack/
[^extra-measures]: for example: a VPN like OpenVPN, [Wireguard](https://www.wireguard.com/) or [tailscale](https://tailscale.com/); or a tool like [ngrok](https://ngrok.com/).
