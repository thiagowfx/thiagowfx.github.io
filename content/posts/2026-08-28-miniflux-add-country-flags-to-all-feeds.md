---
title: "miniflux: add country flags to all feeds 🌐"
date: 2026-08-28T01:20:26+02:00
tags:
  - bestof
  - dev
  - selfhosted
---

**Problem statement**: given my miniflux server with hundreds of RSS feed
subscriptions, add emoji country flags to each feed title, representing their
country of origin and/or the country they're associated with[^1].

[^1]: Why? Purely as a matter of context, and for an extra dose of serendipity
    via diversity. For example, it's often exciting to me to read posts from
    other Canadians, for no particular reason.

For example:

- **Before**: Not Just Serendipity by Thiago Perrotta
- **After**: Not Just Serendipity by Thiago Perrotta 🇧🇷🇨🇦

Some feeds may be identified with multiple flags. The distinction is purposely
loose.

I started to do this tagging process manually, throughout several weeks, until I
exhausted the ones I knew about.

The next natural step, in 2026, is to resort to Gen AI to finish the heavy
lifting, now that the initial pattern has been established.

With my [OpenAI Codex]({{< ref
"2026-08-19-chatgpt-openai-codex-plan-usage" >}}) subscription

- Pi, I prompted away:

> ╭ user ─────────────────────────────────────────────────────────╮
> │                                                               │
> │ List all prompts I ran in this session, bulleted list:        │
> │                                                               │
> ╰───────────────────────────────────────────────────────────────╯
>
> Thinking: Listing all user prompt messages
>
> - "Are you able to connect to my miniflux database in knol?
>    (ssh knol) Creds are in /etc/miniflux.conf in knol."
> - "Note that Alpine Linux uses doas, not sudo."
> - "Are you able to find my list of subscriptions / feeds? There
>    should be 687 of these."
> - "Observe that some feed titles have flags in them."
> - "I want to add a flag for the origin of each blog. Source a
>    few feeds lacking flags and suggest which flags to add."
> - "LGTM."
> - "Source 10–15 more blogs."
> - "LGTM."
> - "Write a blog post about this work using /bloggify."
> - "List all prompts I ran in this session, bulleted list."

Here are a few interesting bits produced by the agent. Note that I run the
coding harness (`pi`) from my laptop, not from my server. As such, all commands
that interact with the server do so via `ssh`. This is good enough for my
purposes.

Count all feeds:

```shell
% ssh knol 'doas sh -c '\''. /etc/miniflux.conf; psql "$DATABASE_URL" -X -Atqc "SELECT count(*) FROM feeds"'\'''
687
```

Some titles already followed the convention:

```text
780|37signals jobs 🇩🇰🇺🇸
818|A cup of coffee by Quentin JOLY 🇫🇷
1366|AI Engineer Guide 🇮🇳
562|Adam Gordon Bell: Cascade Of Insights 🇨🇦
916|Adam Johnson 🇬🇧
```

A pair of Unicode regional indicators forms a flag. Export the titles and
count those pairs:

```shell
% ssh knol 'doas sh -c '\''. /etc/miniflux.conf; psql "$DATABASE_URL" -X -q -c \
  "COPY (SELECT id, title FROM feeds ORDER BY title) TO STDOUT WITH CSV"'\''' | \
  python3 -c 'import csv,sys,re; rows=list(csv.reader(sys.stdin)); p=re.compile(r"[\U0001F1E6-\U0001F1FF]{2}"); found=[(i,t,p.findall(t)) for i,t in rows if p.search(t)]; print(f"feeds_with_flags={len(found)} flags={sum(len(x[2]) for x in found)}")'
feeds_with_flags=148 flags=158
```

I did not infer origin from a name, domain, language, or current residence. Each
addition needed an explicit source. For example, [Jeremy
Keith](https://adactio.com/about/) says "I'm from Ireland originally", [Andre
Garzia](https://andregarzia.com/about.html) says he is originally from Brazil,
and [Christian Rebischke](https://shibumi.dev/about/) describes himself as being
from Germany.

The title itself is the metadata. Exact old-title guards made each update
idempotent and prevented an accidental edit to a renamed feed:

```sql
BEGIN;
UPDATE feeds
SET title = 'Christian Rebischke: shibumi 🇩🇪'
WHERE id = 207 AND title = 'Christian Rebischke: shibumi';
UPDATE feeds
SET title = 'Adactio: Journal by Jeremy Keith 🇮🇪'
WHERE id = 1106 AND title = 'Adactio: Journal by Jeremy Keith';
UPDATE feeds
SET title = 'Adactio: Articles by Jeremy Keith 🇮🇪'
WHERE id = 1107 AND title = 'Adactio: Articles by Jeremy Keith';
UPDATE feeds
SET title = 'Andre Alves Garzia 🇧🇷'
WHERE id = 1481 AND title = 'Andre Alves Garzia';
COMMIT;
```

```text
BEGIN
UPDATE 1
UPDATE 1
UPDATE 1
UPDATE 1
COMMIT
```

A second sourced batch added 12 more titles. Compound origins stay compound:

```text
430|Burak Karakan: ps 🇩🇪🇹🇷
1022|Amjad Masad 🇯🇴🇺🇸
1076|Christopher Olah 🇨🇦
1100|Cognitive Medium by Michael Nielsen 🇦🇺🇺🇸
1174|Andrej Karpathy 🇸🇰🇨🇦
1489|Jeff Geerling 🇺🇸
```

The same audit now reports:

```text
total=687
feeds_with_flags=164
flags=178
without_flags=523
```

Only 523 to go.

This is a practical excuse to tokenmaxx, eh?!

Web searches are done with [pi-web-search](https://github.com/thiagowfx/.dotfiles/tree/e6d1452118ad2b2c317545571fd0923519bf7a41/pi/.pi/agent/local/web-search).
