---
title: "PostgreSQL: get database size"
date: 2025-10-27T22:47:56+01:00
tags:
  - dev
---

**Problem statement**: Given a PostgreSQL DB, obtain is total size, preferably
in a human-readable format (pretty-printed).

## Option 1: SQL query

```sql
SELECT pg_size_pretty(pg_database_size('dbname'));
11 GB
```

## Option 2: `psql` CLI

```sql
\l+ dbname
                                                    List of databases
        Name        | Owner | Encoding |   Collate   |    Ctype    | Access privileges | Size  | Tablespace | Description
--------------------+-------+----------+-------------+-------------+-------------------+-------+------------+-------------
 dbname             | me    | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 11 GB | pg_default |
(1 row)
```
