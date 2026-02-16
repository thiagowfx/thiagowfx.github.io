---
title: "Kindle Paperwhite: KOReader: calibre sync"
date: 2025-06-15T03:49:24+02:00
tags:
  - dev
  - serenity
---

One of the best reasons to [jailbreak]({{< ref
"2025-05-17-winterbreak-hello-world" >}}) a Kindle is to leverage wireless
[Calibre](https://calibre-ebook.com/) sync via [KOReader](http://koreader.rocks/).

Instructions:

**from Calibre**:

- Click Connect/share
- Start wireless device connection
- Set "Optional fixed port" to 9090 and check off 'Use a fixed port'
- Confirm

**from KOReader**:

- Click Settings > Calibre > Wireless Settings
  — Check off 'Enable wireless client'
  — Set inbox folder > `/mnt/us/documents`
  — Server address > Add the IP address + port[^1] of the calibre server (visible in the calibre UI)
- Click Settings > Calibre > Connect

At this point, the Calibre UI should change, recognizing the KOReader client.

From there, it is trivial to send books from the Calibre library to KOReader.
Select the desired books and then click 'Send to device'.

Stefan Svartling has a great [video
tutorial](https://www.youtube.com/watch?v=AQHbOTEJAak) about this.

[^1]: There's an "automatic" mode, however it did not work for me.
