---
title: "Anki: corrupted database"
url: https://perrotta.dev/2026/04/anki-corrupted-database/
last_updated: 2026-04-12
---


Life is hard.
Today, when opening [Anki](https://apps.ankiweb.net/) on macOS:

```
DbError { info: "SqliteFailure(Error { code: DatabaseCorrupt, extended_code: 11 }, Some(\"database disk image is malformed\"))", kind: Other }
```

Database corrupt? What is this, are we in the 2000s? Goodness.

I have automatic backups enabled. For 4 years I haven't needed them. Today
is the day. Never say never!

```shell
% ls -lt "$HOME/Library/Application Support/Anki2/Thiago/backups/"
total 234496
-rw-r--r--@ 1 tperrotta  staff  3911921 Apr  8 00:12 backup-2026-04-08-00.12.17.colpkg
-rw-r--r--@ 1 tperrotta  staff  3911921 Apr  7 00:16 backup-2026-04-07-00.16.26.colpkg
```

I try:

```shell
open "$HOME/Library/Application Support/Anki2/Thiago/backups/backup-2026-04-07-00.16.26.colpkg"
```

...but apparently that file is corrupt as well.

I am not particularly worried because I sync my notes to
[AnkiWeb](https://ankiweb.net/). Even if the entire local collection were corrupt,
my flashcards are in the cloud.

So I decided to simply start from scratch[^1].

```shell
mv ~/Library/Application\ Support/Anki2/Thiago/collection.anki2 ~/Library/Application\ Support/Anki2/Thiago/collection.anki2.corrupt
rm -f ~/Library/Application\ Support/Anki2/Thiago/collection.anki2-shm ~/Library/Application\ Support/Anki2/Thiago/collection.anki2-wal
```

Then I open Anki.

It prompts me to download my decks from AnkiWeb.

And now everything works as usual! Last cleanup:

```shell
trash ~/Library/Application\ Support/Anki2/Thiago/collection.anki2.corrupt
```

No idea why this has happened. First time. Life goes on.

!next

[^1]: The idea was mine. The decision was mine. The LLM suggested the command on
    how to do so. I can still self-troubleshoot, _mmmkay_?

[Previously]({{< ref "2025-10-08-anki-find-all-suspended-cards" >}}).

