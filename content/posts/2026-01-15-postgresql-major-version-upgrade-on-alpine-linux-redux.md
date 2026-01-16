---
title: "PostgreSQL major version upgrade on Alpine Linux, redux"
date: 2026-01-15T22:25:09-03:00
tags:
  - alpine-linux
  - dev
---

[Previously]({{< ref "2025-05-24-postgresql-major-version-upgrade-on-alpine-linux" >}}).

## Problem statement

Given Alpine Linux 3.23 running PostgreSQL 17, upgrade to PostgreSQL 18. For
this specific example, consider a [miniflux](https://miniflux.app/) database.

The [previous]({{< ref "2025-05-24-postgresql-major-version-upgrade-on-alpine-linux" >}}) post still applies, with only one exception:

[PostgreSQL 18 enables data‑checksums by default](https://www.credativ.de/en/blog/postgresql-en/postgresql-18-enables-datachecksums-by-default):

> Version 18 enables data‑checksums by default. In earlier versions, initdb
> required the `--data‑checksums` flag. The new release notes explicitly list
> the change in the incompatibilities section: "Change initdb default to enable
> data checksums… Checksums can be disabled with the new `--no‑data‑checksums`
> option".

This is a better sensible default, but it breaks the normal upgrade flow:

```
~/18/tmp $ pg_upgrade -b /usr/libexec/postgresql17/ -B /usr/libexec/postgresql18/ -d /var/lib/postgresql/17
/olddata/ -D /var/lib/postgresql/18/data
Performing Consistency Checks
-----------------------------
Checking cluster versions                                     ok

old cluster does not use data checksums but the new one does
Failure, exiting
```

The stable upgrade path is to initialize the new cluster database (v18) with
`--no-data-checksums`:

```
~/18/tmp $ initdb --no-data-checksums -D /var/lib/postgresql/18/data --locale=en_US.UTF-8 --encoding=UTF8
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/18/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default "max_connections" ... 100
selecting default "shared_buffers" ... 128MB
selecting default time zone ... America/Toronto
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.

Success.
```

Then perform the migration as usual. Once the migration is complete, for the
sake of improving the reliability of the database, enable checksums:

```
~/18/tmp $ pg_checksums --enable -D /var/lib/postgresql/18/data
Checksum operation completed
Files scanned:   1380
Blocks scanned:  89609
Files written:  1151
Blocks written: 89605
pg_checksums: syncing data directory
pg_checksums: updating control file
Checksums enabled in cluster
```

**Note**: You must run `pg_checksums` while the cluster is off-line, otherwise:

```
~/18/tmp $ pg_checksums --enable -D /var/lib/postgresql/18/data
pg_checksums: error: cluster must be shut down
```

Remember to delete the previous package once the upgrade is fully complete:

```
/var/lib/postgresql # doas apk del postgresql17
(1/3) Purging postgresql17-openrc (17.7-r1)
(2/3) Purging postgresql17 (17.7-r1)
  Executing postgresql17-17.7-r1.pre-deinstall
(3/3) Purging postgresql17-client (17.7-r1)
Executing busybox-1.37.0-r31.trigger
Executing postgresql-common-1.3-r0.trigger
OK: 1271.3 MiB in 577 packages
```

That's all!
