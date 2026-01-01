
[via Connor Edwards](https://cedwards.xyz/github-actions-are-an-impending-security-disaster/):

> Since git tags can be moved arbitrarily by the author, there's nothing stopping them going rogue and changing the Action to be malicious at any time. The author could change the code to exfiltrate the repository itself, the GITHUB_TOKEN (which in many cases can have more power than it should), or other CI/CD secrets.

Hence, bad:

```
uses: actions/checkout@v4
```

Good:

```
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4
```

I find an effective way to address and enforce this practice is via [pre-commit](https://pre-commit.com/):

```yaml
- repo: https://github.com/lalten/check-gha-pinning
  rev: v1.2.0 # or whatever is the latest version
  hooks:
    - id: check-gha-pinning
```

Try this to check whether there are any existing violations in your repositories:

```shell
% pre-commit try-repo https://github.com/lalten/check-gha-pinning --all-files
```

I had some in my blog:

```
GitHub Actions Pinning...................................................Failed
- hook id: check-gha-pinning
- exit code: 1

.github/workflows/gh-pages.yml:22: peaceiris/actions-hugo@v3 is not pinned to commit (should be e3b661c523413d13d642651a5ba5fc0d2b344c0d # v3)
.github/workflows/gh-pages.yml:27: extractions/setup-just@v2 is not pinned to commit (should be dd310ad5a97d8e7b41793f8ef055398d51ad4de6 # v2.0.0)
.github/workflows/gh-pages.yml:33: peaceiris/actions-gh-pages@v4 is not pinned to commit (should be e9c66a37f080288a11235e32cbe2dc5fb3a679cc # v4)
```

They are now fixed.

