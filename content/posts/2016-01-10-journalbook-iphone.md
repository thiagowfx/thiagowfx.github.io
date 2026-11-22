---
title: "journalbook: iphone"
date: 2016-01-10
tags:
  - dev
  - legacy
---

These are highly opinionated (thus, biased) suggestions of configurations for an
iOS device. They seem to work well for me, so I decided to share them.

## Settings — part I

All of these configurations can be found in the 'Settings' app.

* **Wi-fi**:
  * Pre-connect, on-the-fly, to all Wi-Fi networks you intend to automatically
    join.
  * Leave "Ask to join networks" off. This feature is also present on Android
    and proved to be annoying.
* **Bluetooth**: leave it off, turn it on only when you intend to use it.
* **Cellular data**:
  * should be on most of the time, unless you have a very limited data plan[^1]
    or a very limited battery life[^2].
  * leave "Wi-fi assist" on if you have a big 3g/4g plan; it is very useful. It
    uses the cellular network instead of Wi-Fi when you're connected to a weak
    Wi-Fi hotspot.
  * disable cellular data for these apps:
    * Find Friends
    * Game Center
    * News
    * Stocks
    * Tips
    * Watch
* **Notifications**:
  * Sort order: recent
  * Group by app: off
  * Disable notification for these apps:
    * Game Center
    * Tips
* **Control center**:
  * Allow access on Lock Screen: on
  * Access within apps: on
* **Do not disturb**: silence 'only while iphone is locked'
* **General**:
  * **Siri**: leave it off. It is mostly useless, unless you need its
    accessibility features or it is your first week with it.
  * Spotlight search: leave everything on, except these:
    * Find Friends
    * Game Center
    * News
    * Stocks
    * Tips
    * Watch
  * Suggested apps: turn off "Installed apps".
  * **Background app refresh**: disable for these apps:
    * News
    * Stocks
  * **Auto-lock**: 1 minute.
  * Date and time: set timezone automatically.
  * **Keyboards**:
    * Enable those two: Emoji and English
    * Disable auto-correction.
    * Enable auto-capitalization.
  * **Language**: English, period.
* Enable auto-brightness. It is awesome in the iPhone.
* **Sounds**: disable lock sounds and keyboard clicks. Too noisy.
* Use touchID for everything you can. Require passcode immediately.
* Erase data on the iPhone after 10 failed attempts.
* Don't allow access to anything when locked, except, maybe, "reply with
  message".
* Show the battery percentage.
* **Privacy**:
  * **Location services**: on, but:
    * Disable 'share my location' (for 'Find my Friends')
    * Allow google maps to use your location 'while using' the app.
    * Always allow the wheater app to use your location.
    * System services > enable the status bar icon.
    * Disable 'location-based iAds'.
  * Motion and fitness: enable 'fitness tracking' and allow the health app to
    use it.
  * Advertising > limit ad tracking.
  * Diagnostics & usage: that depends on your test, but I'd say to leave these
    settings on (i.e., share data with app developers and with Apple)
* **iCloud**:
  * Enable iCloud drive and let everything access it.
  * **Photos**: disable everything. Don't upload them to iCloud. The main reason
    for that is fact the free space is way too little (5 GB), and it is shared
        with backup data too.
  * Mail: off. You don't want an `@icloud` e-mail.
  * Everything else: on, specially iCloud keychain.
  * **Backup**: on.
  * Find my iPhone: on.
  * Share my location: off.
* **iTunes & App Store**:
  * Apps and updates should be automatically downloaded, but without using
    cellular data.
* **Apple pay and wallet**: IMHO, it is useless, at least at the time of this
  post. I tried to use it but it proved to be way too limited right now.

## Settings — part II

* **E-mail**: if you have a Google account, add it now. In particular, enable
  mail, contacts and calendar. Then, in its advanced settings, make 'discard
  messages' delete instead of archive e-mails.
* Fetch new data: 'push' (instead of fetch), as much as you can. Fetch: hourly
  or more. At the moment of this post, 'hourly' is the maximum time interval you
  can put.
* Show to/cc label: on.
* Flag style: shape.
* Don't ask before deleting.
* Organize by thread (a la Gmail).
* Signature: a popular one is 'Sent from my iPhone'.
* Sort order: First, Last.
* Don't prefer nicknames.
* Disable all 'default alert times'.
* Default calendar: prefer Google's over iCal.
* Messages: send MSM when iMessage is unavailable. Unless you have a limited
  plan.
* Keep messages: 1 year, or less. Don't put 'never'.
* **Safari**
  * Use Google as search engine.
  * Preload top hit.
  * Content blockers: [Adblock Plus](https://itunes.apple.com/us/app/adblock-plus-abp/id1028871868?mt=8)
    and [Focus by Firefox](https://itunes.apple.com/us/app/focus-by-firefox-content-blocking/id1055677337?mt=8)
  * 'Do not track': that depends on you. I'd say to leave it on in the US, but
    off in Brazil.
* **News**: disable everything.
* Camera: enable grid. Don't keep normal photo for HDR.
* **Podcasts**:
  * Disable all notifications.
  * Enable background app refresh.
  * Enable cellular data (for streaming).
  * Sync podcasts and only download on Wi-Fi.
  * Refresh every: choose either daily or weekly.
  * Limit episodes: either 1 or 2 most recent.
  * Download episodes: only new.
  * **Do** delete played episodes.
* Twitter: sign in, but don't install the app.
* Facebook: sign in, and enable calendar and contacts.
* Flickr: if you have it, then sign in.

## Footnotes

**Meta**: this is the first *journalbook* style post in this blog.

[^1]: for example, in Brazil I used to have 200 MB monthly, but here in the
    United States I have 10 GB. Of course, the prices are different.

[^2]: in this case you could also use the "low battery" mode feature too.
