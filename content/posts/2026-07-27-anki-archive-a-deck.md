---
title: "Anki: archive a deck"
date: 2026-07-27T10:49:00+02:00
tags:
  - dev
  - pkm
---

[Previously]({{< ref "2024-12-23-anki-workflow" >}}).

The [Anki official docs](https://docs.ankiweb.net/) do not provide explicit
instructions about the archival of decks that are no longer needed.

Archiving is better than deleting because you never know when you may need a
deck again.

One way to archive a deck is to simply export it as a backup and save it
elsewhere. But then you collection becomes scattered. I'd really like to manage
all my decks in a [single place](https://ankiweb.net/about).

So I came up with a simple workaround.

First, create an `Archive::`
[subdeck](https://docs.ankiweb.net/deck-options.html?highlight=subdeck#subdecks).
A subdeck creates a parent-child relationship which, for our purposes, bundles
all archived decks within an umbrella parent. It's visually easier to manage and
organize, effectively hiding archived decks from the deck list view.

Second, move the desired deck(s) within `Archive::`.

Third, one by one, open the cards/notes list ("Browse") of a deck, select all
cards/notes (`Cmd-A`), then
[suspend](https://docs.ankiweb.net/browsing.html?highlight=suspend#cards) them
all (`Cmd-J` or right click, "Toggle suspend").

**Side effect**: cards/notes from the deck will no longer show up for review. At the
same time, your past progress is kept, should you ever want to unarchive them.
