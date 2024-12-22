---
title: "AWS S3: search by suffix"
date: 2024-09-05T17:09:38+02:00
tags:
  - dev
---

Given an AWS S3 bucket, how to recursively list all objects within it that match
a given suffix?


The following example searches for all objects that end with `thiagowfx`.

```shell
aws s3 rm --profile {aws_profile} s3://example.com/my/path/ --recursive --dryrun --exclude '*' --include "*thiagowfx"
```

This is a hack with a dry-run deletion operation.

Alternatively, use `aws s3 ls`[^1] plus `grep` / `awk` / `sed`:

```shell
aws s3 ls --profile {aws_profile} s3://example.com/my/path | awk -F ' ' '{print $4}' | grep 'thiagowfx$'
```

Why would you use `rm` in lieu of `ls`? Mostly because of the built-in
`--include` / `--exclude` options. If you happen to have millions of objects in
your S3 bucket, then you do not need to list them all.

[^1]: https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html
