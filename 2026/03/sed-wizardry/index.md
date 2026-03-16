
Surely this is some GNU `sed` wizardry for the sake of replacing a hallucinated
link in a GitHub pull request:

```shell
⏺ Bash(BRANCH="thiagowfx/garden-aitools-azure-module"
      REPO="corp/terraform"
      OLD_LINK="docs/adrs/0018-azure-aitools-module-extraction.md"
      NEW_LINK="https://github.com/${REPO}/blob/${BRANCH}/${OLD_LINK}"
      BODY=$(cat /tmp/pr_body.txt | sed "s|](${OLD_LINK})|](${NEW_LINK})|")
      gh pr edit 1253 --body "$BODY")
```

It is quite simple and effective though.

The `s` command in `sed` does not need to use a `/` exclusively (`s/foo/bar`).
The pipe (`|` -> `s|foo|bar`) is a common readable alternative.

And the rest of the expression replaces the link within markdown parentheses
(think of `[link](https://example.com)`).

Courtesy of Claude Code. You can tell it because of the "⏺" bullet character and
the indentation.

