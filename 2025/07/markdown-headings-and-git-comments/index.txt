
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

**Update**: A teammate pointed out the following workaround, which is the most
elegant of them:

[`core.commentChar`](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecommentChar):

> Commands such as `commit` and `tag` that let you edit messages consider a line
> that begins with this character commented, and removes them after the editor
> returns (default `#`).
>
> If set to "auto", git-commit would select a character that is not the
> beginning character of any line in existing commit messages.

And that's exactly what I did:

```shell
% git config set --global core.commentChar "auto"
```

The effect, it automatically picks `;` as the comment character:

```
## Summary

<!-- Provide a clear and concise description of the changes.
Provide a link to the corresponding PR in other repositories if applicable. -->

; Please enter the commit message for your changes. Lines starting
; with ';' will be ignored, and an empty message aborts the commit.
;
; On branch master
; Your branch is up to date with 'origin/master'.
;
; ------------------------ >8 ------------------------
; Do not modify or remove the line above.
; Everything below it will be ignored.
```

[^1]: I am always forgetting whether to call them "headings" or "headers".

