---
title: "ssh: pipe SQL through doas with base64"
date: 2026-08-29T02:44:43+02:00
tags:
  - bloggify
  - dev
  - linux
  - ssh
---

**Problem statement**: nested shell quotes made a remote PostgreSQL update
harder to run than the update itself.

The target is an Alpine Linux host. Its Miniflux configuration contains the database
connection string, so `psql` must run after sourcing `/etc/miniflux.conf` through
`doas`.

An inline command quickly becomes a quoting puzzle. SQL contains single quotes,
Unicode, and sometimes apostrophes. The local shell also expands unquoted
characters before `ssh` sends anything to the server.

I wrote SQL to a temporary file, encoded it locally, and sent only base64 over
SSH:

```shell
% base64 /tmp/miniflux-flags.sql | tr -d '\n' | \
  ssh knol 'doas sh -c '\''
    . /etc/miniflux.conf
    base64 -d | psql "$DATABASE_URL" -X -v ON_ERROR_STOP=1
  '\''
```

Remote shell receives a simple command. `base64 -d` reconstructs SQL on the
server. `psql` reads it from standard input. `ON_ERROR_STOP=1` makes a SQL
error stop the command instead of continuing to later statements.

The file contained real, guarded updates:

```sql
BEGIN;
UPDATE feeds SET title = title || ' 🇺🇸'
WHERE id = 1394 AND title = 'furbo.org: Craig Hockenberry'
RETURNING id, title;
UPDATE feeds SET title = title || ' 🇨🇦'
WHERE id = 1406 AND title = 'Ansuz: Matthew Skala'
RETURNING id, title;
UPDATE feeds SET title = title || ' 🇬🇧'
WHERE id = 1411 AND title = 'Ian Jackson'
RETURNING id, title;
-- eight more exact-title guards
COMMIT;
```

The remote output stayed useful:

```text
BEGIN
 id  |              title
-----+---------------------------------
1394 | furbo.org: Craig Hockenberry 🇺🇸
(1 row)
UPDATE 1
...
UPDATE 1
COMMIT
```

A second query verified every ID after commit:

```text
 id  |              title
-----+---------------------------------
1394 | furbo.org: Craig Hockenberry 🇺🇸
1406 | Ansuz: Matthew Skala 🇨🇦
1411 | Ian Jackson 🇬🇧
1444 | Matthew Garrett: mjg59 🇬🇧
1459 | Cloudscaling by Randy Bias 🇺🇸
1460 | Marcin Juszkiewicz 🇵🇱
1464 | Liss is More by Casey Liss 🇺🇸
1472 | Jerod Santo 🇺🇸
1482 | Matthias Kirschner 🇩🇪
1545 | Charles Leifer 🇺🇸
(10 rows)
```

Base64 does not encrypt anything. It only moves one opaque payload through
several shells. That is enough to keep local parsing away from SQL.
