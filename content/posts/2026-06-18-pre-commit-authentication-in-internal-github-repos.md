---
title: "pre-commit: authentication in internal github repos"
date: 2026-06-18T14:42:26+02:00
tags:
  - dev
  - git
  - pre-commit
---

**Problem statement**: prek can't clone a `repo:` that lives in an internal
(private) GitHub repo — `https://` clone fails without credentials.

I forked my personal
[pre-commit-hooks](https://github.com/thiagowfx/pre-commit-hooks) into an
org-owned repo and updated all our `.pre-commit-config.yaml` files to point at
it:

```yaml
- repo: https://github.com/<org>/pre-commit-hooks
  rev: 5695e23285bef67d1dee957e5c12e86f58ba843b # frozen: v1.0.0
  hooks:
    - id: check-bash-shebang
```

This approach works locally (my GitHub token is broad).

CI (github actions) fails though:

```
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

The repo is `INTERNAL`, not public. As such, `prek` clones the `repo:` URL to
fetch the hooks; with no credentials on the runner, it can't.

First instinct: `git@github.com:<org>/pre-commit-hooks`. Runners have no SSH
key though!

The fix is to keep `https://` in the config, mint a short-lived token that can read
the hooks repo, and tell git to rewrite the URL:

```yaml
- name: Generate app token
  uses: actions/create-github-app-token@bcd2ba49218906704ab6c1aa796996da409d3eb1 # v3.2.0
  id: generate-token
  with:
    client-id: ${{ vars.APP_CLIENT_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}
    owner: ${{ github.repository_owner }}
    repositories: pre-commit-hooks
    permission-contents: read
- uses: actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10 # v6.0.3
  with:
    persist-credentials: false
- name: Authenticate git for internal hook repos
  env:
    TOKEN: ${{ steps.generate-token.outputs.token }}
  run: git config --global url."https://x-access-token:${TOKEN}@github.com/".insteadOf "https://github.com/"
- uses: j178/prek-action@bdca6f102f98e2b4c7029491a53dfd366469e33d # v2.0.4
```

Two things worth noting.

- **First**: never inline `${{ steps.generate-token.outputs.token }}` directly into a `run:` shell string — [zizmor]({{< ref "2025-10-03-zizmor" >}}) (a GitHub Actions security linter) flags it as a template injection risk. Pass it via `env:` and use the shell variable instead.

- **Second**: the `repositories: pre-commit-hooks` scope only works if the App
  is actually *installed* on that repo. That one is a manual step in GitHub's UI
  — `github.com/organizations/<org>/settings/installations` → the App →
  Repository access → add the repo. No amount of YAML fixes it otherwise; it
  silently returns a 404 from the App installation endpoint otherwise.

After the installation grant, the clone goes through and `prek` runs cleanly.

- - -

🤖 *Drafted with `/bloggify`.*
