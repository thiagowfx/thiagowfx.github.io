---
title: "PostgreSQL major version upgrade on Alpine Linux"
date: 2025-05-24T16:00:23+02:00
tags:
  - bestof
  - dev
---

## Problem statement

Given Alpine Linux 3.22 running PostgreSQL 16, upgrade to PostgreSQL 17. For
this specific example, consider a [`miniflux`](https://miniflux.app/) database.

## Procedure

Install PostgreSQL 17:

```shell
% doas apk add postgres
```

It can coexist with `postgres16`.

Stop the PostgreSQL daemon:

```shell
% doas service postgresql stop
```

If you navigate to the Miniflux server with your browser, it will fail, as
expected:

```
store: unable to create app session: dial tcp [::1]:5432: connect: connection refused
```

Change the PostgreSQL system version to the desired one:

```shell
% doas pg_versions set-default 17
```

Change to the root user, for convenience, then change to the existing postgresql
directory:

```shell
% doas su
% cd /var/lib/postgresql/
```

Prepare files and directories for the upgrade:

```shell
% cd 16/
% mv data olddata
% cd ../
% mkdir 17/
% cd 17/
% mkdir data tmp
% chown postgres:postgres data tmp
```

Change to the `postgres` user:

```shell
% su postgres
% cd tmp/
```

Initialize the new cluster:

```shell
% initdb -D /var/lib/postgresql/17/data --locale=en_US.UTF-8 --encoding=UTF8 [--data-checksums]
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/17/data ... ok
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

In the previous command I chose to omit `--data-checksums`, otherwise I get the
following error:

```
old cluster does not use data checksums but the new one does
Failure, exiting
```

Upgrade the new cluster:

```shell
% pg_upgrade -b /usr/libexec/postgresql16/ -B /usr/libexec/postgresql17/ -d /var/lib/postgresql/16/olddata/ -D /var/lib/postgresql/17/data/
Performing Consistency Checks
-----------------------------
Checking cluster versions                                     ok
Checking database user is the install user                    ok
Checking database connection settings                         ok
Checking for prepared transactions                            ok
Checking for contrib/isn with bigint-passing mismatch         ok
Checking data type usage                                      ok
Creating dump of global objects                               ok
Creating dump of database schemas
                                                              ok
Checking for presence of required libraries                   ok
Checking database user is the install user                    ok
Checking for prepared transactions                            ok
Checking for new cluster tablespace directories               ok

If pg_upgrade fails after this point, you must re-initdb the
new cluster before continuing.

Performing Upgrade
------------------
Setting locale and encoding for new cluster                   ok
Analyzing all rows in the new cluster                         ok
Freezing all rows in the new cluster                          ok
Deleting files from new pg_xact                               ok
Copying old pg_xact to new server                             ok
Setting oldest XID for new cluster                            ok
Setting next transaction ID and epoch for new cluster         ok
Deleting files from new pg_multixact/offsets                  ok
Copying old pg_multixact/offsets to new server                ok
Deleting files from new pg_multixact/members                  ok
Copying old pg_multixact/members to new server                ok
Setting next multixact ID and offset for new cluster          ok
Resetting WAL archives                                        ok
Setting frozenxid and minmxid counters in new cluster         ok
Restoring global objects in the new cluster                   ok
Restoring database schemas in the new cluster
                                                              ok
Copying user relation files
                                                              ok
Setting next OID for new cluster                              ok
Sync data directory to disk                                   ok
Creating script to delete old cluster                         ok
Checking for extension updates                                ok

Upgrade Complete
----------------
Optimizer statistics are not transferred by pg_upgrade.
Once you start the new server, consider running:
    /usr/libexec/postgresql17/vacuumdb --all --analyze-in-stages
Running this script will delete the old cluster's data files:
    ./delete_old_cluster.sh
```

Now clean up:

```shell
% ^D  # go back to the root user
% /var/lib/postgresql/17/tmp/delete_old_cluster.sh
% rmdir /var/lib/postgresql/16/  # it should be empty by now
```

If you're curious about this script, it's a simple one-liner:

```shell
#!/bin/sh

rm -rf '/var/lib/postgresql/16/olddata'
```

Finally, let's get the cluster back up and vacuum it:

```shell
% ^D  # go back to your main user
% doas service postgresql start
% doas su - postgres -c '/usr/libexec/postgresql17/vacuumdb --all --analyze-in-stages'
vacuumdb: processing database "miniflux": Generating minimal optimizer statistics (1 target)
vacuumdb: processing database "postgres": Generating minimal optimizer statistics (1 target)
vacuumdb: processing database "template1": Generating minimal optimizer statistics (1 target)
vacuumdb: processing database "miniflux": Generating medium optimizer statistics (10 targets)
vacuumdb: processing database "postgres": Generating medium optimizer statistics (10 targets)
vacuumdb: processing database "template1": Generating medium optimizer statistics (10 targets)
vacuumdb: processing database "miniflux": Generating default (full) optimizer statistics
vacuumdb: processing database "postgres": Generating default (full) optimizer statistics
vacuumdb: processing database "template1": Generating default (full) optimizer statistics
```

At this point, Miniflux should be working again.
Navigate to `/about` and verify its database version: `Postgres version: 17.5`.

Last step, delete the previous package:

```shell
% doas apk del postgresql16 postgres16-contrib
```

Double-check the newer version is still installed:

```shell
% apk list -I | grep postgres
libpq-17.5-r0 x86_64 {postgresql17} (PostgreSQL) [installed]
postgresql-common-1.2-r1 x86_64 {postgresql-common} (MIT) [installed]
postgresql-common-openrc-1.2-r1 x86_64 {postgresql-common} (MIT) [installed]
postgresql-zsh-completion-5.9-r5 x86_64 {zsh} (MIT-Modern-Variant AND GPL-2.0-only) [installed]
postgresql17-17.5-r0 x86_64 {postgresql17} (PostgreSQL) [installed]
postgresql17-client-17.5-r0 x86_64 {postgresql17} (PostgreSQL) [installed]
postgresql17-contrib-17.5-r0 x86_64 {postgresql17} (PostgreSQL) [installed]
postgresql17-openrc-17.5-r0 x86_64 {postgresql17} (PostgreSQL) [installed]
```

And we're done!

## References

- https://wiki.alpinelinux.org/wiki/Postgresql
- https://beune.dev/posts/upgrade-alpine-postgresql/
