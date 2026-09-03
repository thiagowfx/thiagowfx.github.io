---
title: "anki: migrate English notes to TTS note types"
url: https://perrotta.dev/2026/08/anki-migrate-english-notes-to-tts-note-types/
last_updated: 2026-09-03
---


[Previously]({{< ref "2026-04-15-anki-flashcards-with-claude-code" >}}).

**Problem statement**: migrate my English 🇬🇧 deck to dedicated note types with
British English text-to-speech, without adding reverse cards.

I created `English Language Card 🇬🇧` with four fields (`Front`, `Front Example`,
`Back`, and `Striked`) and only one card template:

```text
{{Front}} {{tts en_GB:Front}}

{{#Front Example}}
<br>
<i>{{Front Example}}</i> {{tts en_GB:Front Example}}
{{/Front Example}}
```

`English Grammatik Cloze 🇬🇧` uses the same TTS setup for cloze notes:

```text
{{cloze:Text}} {{tts en_GB:Text}}
```

AnkiConnect could create both types, but did not expose a `changeNoteType`
action. I closed Anki and used its own Python package instead. Before changing
the collection, I exported the English deck and copied the SQLite database:

```text
4.8M pre-english-note-type-migration-2026-08-22-13.27.44.apkg
9.9M pre-english-note-type-migration-2026-08-22-13.29.08.collection.anki2
```

The field and template maps did the migration in place:

```python {filename="/tmp/anki_migrate_english.py"}
col.models.change(basic, groups["Basic"], language, {0: 0, 1: 2}, {0: 0})
col.models.change(cloze, groups["Cloze"], english_cloze, {0: 0, 1: 1}, None)
```

I rehearsed the migration against the database copy before running it for real:

```shell
% PYTHONPATH=/Applications/Anki.app/Contents/Resources/app_packages \
  /opt/homebrew/bin/python3.13 /tmp/anki_migrate_english.py \
  ~/Library/Application\ Support/Anki2/User\ 1/collection.anki2
{
  "notes": 1089,
  "cards_before": 1096,
  "cards_after": 1089,
  "language_notes": 1086,
  "cloze_notes": 3,
  "removed_reverse_cards": 7,
  "integrity": "ok"
}
```

The script also checked every mapped field, retained card ID, and review-log
count. After a full upload to AnkiWeb, a normal sync passed.

No reverse cards, and all English notes can now speak for themselves (pun
intended!).

