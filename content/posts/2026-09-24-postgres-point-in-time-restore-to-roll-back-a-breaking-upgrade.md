---
title: "postgres: point-in-time restore to roll back a breaking upgrade"
date: 2026-09-24T02:11:43+02:00
tags:
  - aws
  - bloggify
  - dev
  - kubernetes
---

**Problem statement**: how to roll back a self-hosted app upgrade when its
database migrations have no down path?

A new release of an internal tool started to enforce a license limit that
the old one did not. Pinning the old image back in GitOps was not enough:

```text
[ERROR] Migration failed - inconsistent migrations
Traceback (most recent call last):
  File "/etc/service/app/./run", line 145, in <module>
    main()
subprocess.CalledProcessError: Command '['/usr/local/bin/app', 'migrate', '--verbosity=debug']' returned non-zero exit status 1.
```

The old binary refused to start against the new schema. RDS automated
backups were on, with 30-day retention:

```shell
% aws rds describe-db-instance-automated-backups \
    --db-instance-identifier shared-db \
    --query 'DBInstanceAutomatedBackups[].[Status,RestoreWindow.EarliestTime,RestoreWindow.LatestTime]' \
    --output table
----------------------------------------------------------------------
|                 DescribeDBInstanceAutomatedBackups                 |
+--------+-----------------------------+-----------------------------+
|  active|  2026-08-24T22:41:45+00:00  |  2026-09-23T22:41:45+00:00  |
+--------+-----------------------------+-----------------------------+
```

Several apps share that instance. An in-place restore would have rolled back
all of their databases. RDS point-in-time restore always creates a new
instance anyway:

```shell
% aws rds restore-db-instance-to-point-in-time \
    --source-db-instance-identifier shared-db \
    --target-db-instance-identifier shared-db-restore-20260910 \
    --restore-time 2026-09-10T12:00:00Z \
    --db-instance-class db.t4g.micro \
    --no-multi-az --no-publicly-accessible --no-deletion-protection
shared-db-restore-20260910	creating
```

With the app scaled to zero, a throwaway pod in the cluster moved only the
app's database across:

```shell
% pg_dump -h shared-db-restore-20260910.xxx.rds.amazonaws.com \
    -d app -Fc -f /tmp/app.dump
% psql -h shared-db.xxx.rds.amazonaws.com -d postgres \
    -c "ALTER DATABASE app RENAME TO app_upgraded_bak;" \
    -c "CREATE DATABASE app OWNER app;"
% pg_restore -h shared-db.xxx.rds.amazonaws.com \
    -d app --no-owner --role=app -j 2 /tmp/app.dump
```

Rename, not drop: rollback stays two `ALTER DATABASE` statements away. With
the old schema back, the pinned image started cleanly:

```text
[INFO] Migrations to perform
[INFO] Performing migration for add-unified-comment-output-details
[INFO] Completed migration for add-unified-comment-output-details
[INFO] Migration complete
[INFO] Starting server
```

The cost: everything the app wrote after the restore point was gone.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
