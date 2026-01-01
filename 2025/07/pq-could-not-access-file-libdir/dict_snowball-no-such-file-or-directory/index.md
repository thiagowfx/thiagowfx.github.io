
My [miniflux](http://miniflux.app/) instance broke yesterday. All feeds had the
following error:

```
3 errors - Database error: store: unable to update entry "{redacted}": pq: could not access file "$libdir/dict_snowball": No such file or directory.
```

The error is from PostgreSQL (`pq`).

I recall I did a full system upgrade yesterday (`doas apk upgrade`).

Upon checking the logs in `/var/log/apk.log`...

```
Running `apk upgrade --no-self-upgrade` at 2025-07-09 13:57:09
apk-tools 3.0.0_rc5_git20250613-r0, compiled for x86_64.
( 1/60) Purging postgresql-zsh-completion (5.9-r5)
( 2/60) Purging postgresql17-contrib (17.5-r2)
( 3/60) Purging postgresql17-openrc (17.5-r2)
( 4/60) Purging postgresql17 (17.5-r2)
postgresql17-17.5-r2.pre-deinstall: Executing script...
postgresql17-17.5-r2.pre-deinstall: *
postgresql17-17.5-r2.pre-deinstall: * You are uninstalling your default PostgreSQL version (17) which seems to be
postgresql17-17.5-r2.pre-deinstall: * in use! If it's *not* intentional and you want to preserve this version,
postgresql17-17.5-r2.pre-deinstall: * install it explicitly: `apk add postgresql17`.
postgresql17-17.5-r2.pre-deinstall: *
postgresql17-17.5-r2.pre-deinstall: * Please note that to upgrade your cluster to a new major version using
postgresql17-17.5-r2.pre-deinstall: * pg_upgrade(1), you must have both the old and new versions installed.
postgresql17-17.5-r2.pre-deinstall: *
ERROR: postgresql17-17.5-r2.pre-deinstall: exited with error 1
```

For whatever reason (!?), the `postgresql17*` packages were removed.

The fix is straightforward:

```shell
% doas apk add postgresql17
% doas service miniflux restart
```

Why did it break in the first place?!

There's nothing suspicious on `postgresql17` in the
[aports](https://gitlab.alpinelinux.org/alpine/aports/-/commits/master/main/postgresql17)
repo 🤷

What is `dict_snowball`?

> `dict_snowball` is a PostgreSQL text search dictionary module that uses the
> Snowball stemming algorithms for full-text search.

