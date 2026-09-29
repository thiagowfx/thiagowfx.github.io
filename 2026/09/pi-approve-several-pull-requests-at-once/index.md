---
title: "pi: approve several pull requests at once"
url: https://perrotta.dev/2026/09/pi-approve-several-pull-requests-at-once/
last_updated: 2026-09-29
---


[Previously]({{< ref "2026-02-04-github-approve-prs-from-cli" >}}).

**Problem statement**: how can I approve several reviewed pull requests without
opening each one individually?

I pasted six pull request URLs into [Pi](https://pi.dev/) and asked it to
approve all of them. It ran the same `gh` command for each URL:

```bash
prs=(
  https://github.com/[redacted]/[redacted]/pull/7692
  https://github.com/[redacted]/[redacted]/pull/7695
  https://github.com/[redacted]/[redacted]/pull/7689
  https://github.com/[redacted]/[redacted]/pull/7694
  https://github.com/[redacted]/[redacted]/pull/7693
  https://github.com/[redacted]/[redacted]/pull/36196
)
status=0
for pr in "${prs[@]}"; do
  if gh pr review --approve "$pr"; then
    printf 'APPROVED %s\n' "$pr"
  else
    printf 'FAILED %s\n' "$pr" >&2
    status=1
  fi
done
exit "$status"
```

```text
APPROVED https://github.com/[redacted]/[redacted]/pull/7692
APPROVED https://github.com/[redacted]/[redacted]/pull/7695
APPROVED https://github.com/[redacted]/[redacted]/pull/7689
APPROVED https://github.com/[redacted]/[redacted]/pull/7694
APPROVED https://github.com/[redacted]/[redacted]/pull/7693
APPROVED https://github.com/[redacted]/[redacted]/pull/36196
```

One prompt, six approvals, no repository checkouts.

