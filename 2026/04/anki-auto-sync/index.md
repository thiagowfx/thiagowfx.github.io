---
title: "anki: auto-sync"
url: https://perrotta.dev/2026/04/anki-auto-sync/
last_updated: 2026-04-12
---


[Previously]({{< ref "2026-04-08-anki-corrupted-database" >}}).

**Problem statement**: enable auto-sync to AnkiWeb.

First layer: enable sync on open/close: `Preferences > Syncing > Automatically
sync on profile open/close`

Second layer: for manual syncs, press `y`
([source](https://old.reddit.com/r/Anki/comments/1bxrkbn/is_there_a_way_to_sync_automatically_whenever_a/)).

Third layer: install and enable an auto sync add-on such as [this
one](https://ankiweb.net/shared/info/501542723):

> This addon will automatically synchronize your collection with AnkiWeb at time
> intervals you can choose. It will never interrupt you while you are using
> Anki.
>
> By default, the first sync will start 1 minute after your last activity. While
> Anki is sitting idle in the background, it will sync every 10 minutes. You can
> change those settings in the options dialog.

Someone forked that add-on to improve upon it, enabling [background auto
sync](https://ankiweb.net/shared/info/226796325).

Should I trust a random add-on though? Even if the Anki community is generally
decent and well-intentioned, these days we can't trust anyone.

I asked [Opus 4.6](https://www.anthropic.com/news/claude-code-security) (Claude)
to analyze it for potential malware:

```
⏺ I've now read every single source file in the addon. Here's my analysis:

  ---
  Malware Analysis: Background Auto Sync (226796325)

  Addon: Background Auto Sync for Anki
  Author: athulkrishna2015
  Source: GitHub
  Fork of: Auto-Sync-Anki-Addon by Robin-Haupt-1
  License: GPL-3.0
  Files reviewed: All 8 Python source files + manifest.json

  Verdict: No malware detected. Appears safe.

  What the code actually does

  1. sync_routine.py (core logic) — Sets up timers to periodically call Anki's built-in
  mw.col.sync_collection(). Saves/restores window state so sync doesn't steal focus. All sync goes
  through Anki's native sync infrastructure (AnkiWeb auth, mw.pm.sync_auth()).
  2. utils.py — Single function: has_internet_connection() which opens a TCP socket to 8.8.8.8:53
  (Google DNS) to check connectivity. This is a standard, benign connectivity check. No data is
  sent.
  3. config.py — Reads/writes config to Anki's own config storage (mw.col.set_config/get_config). No
   external communication.
  4. main.py — Wires up hooks (profile_did_open, profile_will_close, sync_will_start,
  sync_did_finish) and adds a menu item. Standard Anki addon boilerplate.
  5. log_window.py — Simple in-memory log viewer (QDialog + QTextEdit). No file I/O, no network.
  6. options_dialog.py — Qt settings dialog with spinboxes/checkboxes. The support tab loads a Ko-fi
   widget (https://storage.ko-fi.com/cdn/widget/Widget_2.js) via an embedded AnkiWebView. Also
  displays crypto donation QR codes (BTC, ETH, UPI). These are static images bundled in the addon.
  7. constants.py — Config key names and defaults. Pure data.
  8. bump.py / make_ankiaddon.py — Developer build tooling only; not shipped in the .ankiaddon
  package.

  Specific things I checked for

  ┌────────────────┬────────────────────────────────────────────────────────────────────────────┐
  │    Concern     │                                  Finding                                   │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │                │ Only socket.create_connection("8.8.8.8", 53) for connectivity check +      │
  │ Network calls  │ Anki's own sync API. No external HTTP requests, no telemetry, no phoning   │
  │                │ home.                                                                      │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │ File system    │ Only os.path.dirname(__file__) and os.path.join to load bundled QR code    │
  │ access         │ images. No reading/writing arbitrary files.                                │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │ Code execution │ None. No exec(), eval(), subprocess, os.system, importlib, or dynamic code │
  │  / eval        │  loading.                                                                  │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │ Data           │ No access to deck content, card data, or personal information beyond what  │
  │ exfiltration   │ Anki's sync already handles.                                               │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │ Obfuscation    │ None. Code is clean, readable, well-structured Python.                     │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │ Suspicious     │ Only standard library (socket, datetime, os, json) and Anki's own APIs     │
  │ imports        │ (aqt, aqt.qt).                                                             │
  ├────────────────┼────────────────────────────────────────────────────────────────────────────┤
  │                │ Loads JavaScript from storage.ko-fi.com in the support tab — this is a     │
  │ Ko-fi widget   │ standard donation button, not a concern, and only loads when you open the  │
  │                │ options dialog's "Support" tab.                                            │
  └────────────────┴────────────────────────────────────────────────────────────────────────────┘

  Minor notes (not security concerns)

  - The author has 18 other shared items on AnkiWeb, suggesting an active community member rather
  than a throwaway account.
  - The addon is relatively new (updated 2026-03-27) with 0 ratings so far, so there's limited
  community vetting.
  - The code is a clean, well-documented fork of the established Robin-Haupt Auto-Sync addon.

  Bottom line: The code does exactly what it claims — periodic background sync using Anki's native
  sync mechanism. No signs of malicious intent, data exfiltration, backdoors, or obfuscated code.

✻ Cooked for 2m 36s
```

I am not installing it though, I am happy with the second layer for now.

