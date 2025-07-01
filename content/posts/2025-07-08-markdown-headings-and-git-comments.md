---
title: "Markdown headings and git comments"
date: 2025-07-08T13:18:09+02:00
tags:
  - dev
---

Our team uses a PR template that resembles the following:

```
% cat .github/pull_request_template.md
## Summary

<!-- Provide a clear and concise description of the changes.
Provide a link to the corresponding PR in other repositories if applicable. -->

## Jira Task

- [ ] No ticket needed

https://acme.atlassian.net/browse/XXX

## Cluster(s) Affected

<!-- List the clusters affected by this change -->

## Impact

<!-- Describe the impact of these changes. Will this require downtime? Are there
any performance considerations? -->

## Testing

<!-- Describe how you've tested these changes -->
```

[Previously]({{< ref "2025-05-04-github-pull-request-template" >}}) I wrote
about how to automatically incorporate github pull request templates in `git
commit` (`COMMIT_EDITMSG`).

It turns out there's one caveat with this approach.

Markdown headings[^1] (`##` for `<h2>`) use the same character as git line comments
(`#`) for commit messages.

As a side effect, when pulling up the template locally with a plain git commit,
the headings do not show up in the final commit message.

This can be worked around by using `gh pr create` instead, but it [breaks my
setup](https://xkcd.com/1172/).

Another workaround is to convert the headings to use `----` markers, for example:

```
Summary
-------

<!-- Provide a clear and concise description of the changes.
Provide a link to the corresponding PR in other repositories if applicable. -->
```

[^1]: I am always forgetting whether to call them "headings" or "headers".
