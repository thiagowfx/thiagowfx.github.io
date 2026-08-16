---
title: "terraform: fileset does not respect gitignore"
date: 2026-08-07T11:27:13+02:00
tags:
  - aws
  - bloggify
  - coding
  - dev
  - git
  - terraform
---

**Problem statement**: a terraform project planned clean locally (`terraform
plan`), but CI insisted on a diff. Every apply fixed it for one side and broke
it for the other, back-and-forth.

The culprit was a `null_resource` that rebuilds an AWS Lambda for a NodeJS app
bundle whenever its sources change, keyed on a hash of the whole directory:

```terraform
resource "null_resource" "lambda_build" {
  triggers = {
    dir_sha = sha256(join("", [for f in sort(fileset("${path.module}/lambda", "**")) : "${f}:${filesha256("${path.module}/lambda/${f}")}"]))
  }

  provisioner "local-exec" {
    command = "cd ${path.module}/lambda && npm ci && npm run build"
  }
}
```

[`fileset()`](https://developer.hashicorp.com/terraform/language/functions/fileset)
walks the filesystem. It has no idea `.gitignore` exists. So `node_modules/`
and `dist/`, present locally after a build, but absent in a fresh CI checkout,
creates the discrepancy.

A minimal reproduction test case, with `node_modules/` and `dist/` gitignored:

```shell
% git ls-files lambda | wc -l
2
% echo 'sha256(join("", [for f in sort(fileset("./lambda", "**")) : "${f}:${filesha256("./lambda/${f}")}"]))' | terraform console
"a0af67e204ae2b73a7452d0c2755be1f665b377b5d49e7cc520bd31607adb832"
```

Then with `npm ci && npm run build`:

```shell
% find lambda -type f | wc -l
4
% git status --porcelain | wc -l
0
% echo 'sha256(join("", [for f in sort(fileset("./lambda", "**")) : "${f}:${filesha256("./lambda/${f}")}"]))' | terraform console
"728a40d04abc2b8292d57465d1f037f833a67d4cc0607a6c64cef487292d9be6"
```

Git says nothing changed; Terraform says everything did (ugh!).

That's the issue. CI plans one value, my laptop plans the other, and each
apply sets up the next one to "detect drift" again.

Nothing in AWS had changed. The deployed artifact was byte-identical the whole
time; only the build trigger churned.

The fix is to hash the build *inputs*, not the build *directory*:

```terraform
dir_sha = sha256(join("", [for f in sort(setunion(
  fileset("${path.module}/lambda", "src/**"),
  ["package.json", "package-lock.json"],
)) : "${f}:${filesha256("${path.module}/lambda/${f}")}"]))
```

Same value on both sides, and still sensitive to anything that actually matters:

```shell
% # dirty tree, after npm ci
"a0af67e204ae2b73a7452d0c2755be1f665b377b5d49e7cc520bd31607adb832"
% # pristine `git archive` checkout
"a0af67e204ae2b73a7452d0c2755be1f665b377b5d49e7cc520bd31607adb832"
% # after editing lambda/src/handler.ts (hypotetically)
"53ef69e287a65f9785cf05985942a5c62a8175348c91c7d9c83039bfc31b8714"
```

`terraform console` is the right tool here — it evaluates an expression against
the real filesystem without an apply, so both variants can be diffed against a
pristine `git archive` tree and a working one before committing anything.

The general shape: any `fileset()` over a directory that also holds build
artifacts, virtualenvs, or vendored dependencies is environment-dependent, and
will read as permanent drift for exactly as long as nobody looks closely.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
