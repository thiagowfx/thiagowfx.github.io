---
title: "Anki: find all notes with an empty field"
date: 2024-01-29T00:06:49-03:00
tags:
  - dev
---

Gabriel Wyner recommends, in its [Fluent
Forever](https://fluent-forever.com/index.html) book, that each
[Anki](https://apps.ankiweb.net/) note (card) has at least one image
associated to it. This is intended to improve overall retention.

<!--more-->

Back when I started my German Anki deck for language learning, I did not add
any images. Now I find myself slowly backfilling my already existing notes
with images. However, the more images I add, the harder it becomes to find
notes without images.

Upon reading the [Anki manual](https://docs.ankiweb.net/) I figured out a way to find out which notes are still missing images:

1. Open Anki.
1. Open the deck you want to modify – in my case, `Languages::German`.
1. Click "Browse".
1. Type in `deck:current "Front Example:"`.

"Front Example" is the name of the field of my note template wherein I add images; you should replace it with the corresponding one you use. This syntax isn't intuitive at all. Initially I was trying something like `-"Front Example:*"`.
