---
title: "pre-commit: internal hook repos, take two"
date: 2026-09-03T14:03:03+02:00
tags:
  - bloggify
  - dev
  - git
  - pre-commit
  - ssh
---

[Previously]({{< ref "2026-06-18-pre-commit-authentication-in-internal-github-repos" >}}).

**Problem statement**: an internal hook repo has to be cloned by CI *and* by
every developer, and the credentials each side owns are not the same.

A `.pre-commit-config.yaml` refers to hooks by repository:

```yaml
repos:
  - repo: https://github.com/<org>/pre-commit-hooks
    rev: 528e165cff8a11bc4f9f49a9b25f3249e09e4237 # frozen: v0.0.22
    hooks:
      - id: just-format
```

Before every run, `prek` clones each of those repositories into its cache. A
public repo clones anonymously and nobody thinks about it again. Ours moved out
of a personal account into an org-owned repo, which is `INTERNAL` — so the
clone now needs credentials, from whoever is running.

In June I gave the runners a short-lived app token and called it done. CI went
green. The next morning, a coworker could no longer commit:

```text
$ prek run -a
error: Failed to init hooks
  caused by: Failed to initialize repo `https://github.com/<org>/pre-commit-hooks`
  caused by: Command `git full clone` exited with an error:

[status]
exit status: 128

[stderr]
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

Not a permissions problem: the same coworker could open and clone the repo by
hand. `prek` clones non-interactively, and an internal repo over `https://`
needs a credential helper to answer. Mine had a token cached; theirs did not:

```shell
% git -c credential.helper= clone https://github.com/<org>/pre-commit-hooks
Cloning into 'pre-commit-hooks'...
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

`SKIP=` does not rescue this. The clone happens while hooks are being
initialized, long before `SKIP` is consulted, so the whole run dies and commits
with it. Three days after the migration, I reverted it everywhere:

```text
4f74a46a Revert: ci: migrate pre-commit hooks to <org>/pre-commit-hooks
ea747ebe Revert: ci: migrate pre-commit hooks to <org>/pre-commit-hooks
4ec7e8063 Revert: ci: migrate pre-commit hooks to <org>/pre-commit-hooks
```

That June token was handed to git as a URL rewrite: `https://github.com/`
became `https://x-access-token:$TOKEN@github.com/` on the runner. I had also
considered `git@github.com:<org>/pre-commit-hooks` back then, and dropped it
because runners have no SSH key. The premise was right and the conclusion was
backwards — a rewrite runs in whichever direction we point it, and I had pointed
it at the side that could not adapt.

So the config takes the URL that developers already have credentials for:

```diff
-  - repo: https://github.com/<org>/pre-commit-hooks
-    rev: 528e165cff8a11bc4f9f49a9b25f3249e09e4237 # frozen: v0.0.22
+  - repo: git@github.com:<org>/pre-commit-hooks
+    rev: 3030e9389488a2e4543a4d5d45d78a63bb591864 # frozen: v1.1.0
```

And the keyless runner rewrites that SSH prefix back to HTTPS, with the same
short-lived app token as before:

```yaml
- name: Authenticate git for the internal hooks repo
  env:
    TOKEN: ${{ steps.generate-token.outputs.token }}
  run: git config --global url."https://x-access-token:${TOKEN}@github.com/<org>/".insteadOf "git@github.com:<org>/"
```

A warm cache is what hid the bug the first time, so both paths were verified
against a cold one. The developer path, cloning over SSH:

```shell
% XDG_CACHE_HOME=$(mktemp -d) prek run -a just-format
Format Justfiles.........................................................Passed
```

The runner path, with SSH made unusable and nothing but the rewrite in `$HOME`:

```shell
% export HOME=$(mktemp -d)
% printf '[url "https://x-access-token:%s@github.com/<org>/"]\n\tinsteadOf = git@github.com:<org>/\n' "$(gh auth token)" > "$HOME/.gitconfig"
% SSH_AUTH_SOCK= GIT_SSH_COMMAND=/bin/false XDG_CACHE_HOME="$HOME/.cache" prek run -a just-format
Format Justfiles.........................................................Passed
```

That second run also exposed where the rewrite belongs. Asking for a single hook
populated the cache with every hook repo in the config:

```shell
% ls "$HOME/.cache/prek/repos" | wc -l
      13
```

`prek` initializes all of them up front, so the rewrite goes in *every* job that
runs `prek` — not only the linting one.
