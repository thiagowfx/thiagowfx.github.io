---
title: "terrateam: plan from drift issues"
date: 2026-08-24T18:38:39+02:00
tags:
  - bloggify
  - dev
  - terraform
  - terrateam
---

**Problem statement**: Terrateam opens drift reports as GitHub issues, but `terrateam plan` only works on pull requests.

The distinction is explicit in Terrateam's [issue comment handler](https://github.com/terrateamio/terrateam/blob/cc723447ff80023b8627df6f8719bfb38462cf87/code/src/terrat_vcs_service_github/terrat_vcs_service_github_ep_events3.ml#L550-L655):

```ocaml
{ primary = Primary.{ number = pull_request_id; pull_request = Some _; _ }; _ };

| Gw.Issue_comment_event.Issue_comment_created _ ->
    Logs.debug (fun m -> m "%s : NOOP : ISSUE_COMMENT_CREATED" request_id);
    Prmths.Counter.inc_one (Metrics.comment_events_total "noop");
    Abbs_future_combinators.return_ok ()
```

Calling the repository workflow directly was not an option either. Its work token comes from the Terrateam backend.

So I kept Terrateam in charge and gave it the pull request it expects. A GitHub Actions relay checks that the source is an open Terrateam drift issue and that the commenter has repository write access. It then puts a comment-only Terraform file in each selected drift directory:

```python
markers = [
    InputGitTreeElement(
        path=f"{directory}/terrateam_issue_relay.tf",
        mode="100644",
        type="blob",
        content=f"# Terrateam plan relay for drift issue #{issue_number}, comment {comment_id}.\n",
    )
    for directory in directories
]
```

That path change gives Terrateam a real dirspace without changing infrastructure. The relay opens a temporary draft PR and posts the original command on it:

```python
pull = repo.create_pull(
    base=repo.default_branch,
    head=branch,
    title=f"Terrateam plan relay for drift issue #{issue_number}",
    body=relay_body(issue_number, comment_id, event["comment"]["html_url"]),
    draft=True,
)
pull.as_issue().create_comment(command)
```

Terrateam uses its normal locks, hooks, credentials, and batching. Another workflow copies its comments back to the drift issue. `apply` remains unsupported: an issue has no PR approval or review intent.

The live test planned the requested directory and returned the result:

```text
## Plans :thumbsup:

## Terrateam Plan Output :thumbsup:

**Plan: 0 to add, 8 to change, 0 to destroy**
```

The temporary PR ended where it should:

```shell
% gh pr view 6687 --json number,state,headRefName,title
{"headRefName":"bot/terrateam-issue-relay/6663-5398113346","number":6687,"state":"CLOSED","title":"Terrateam plan relay for drift issue #6663"}
```

```shell
% ./ci/run_python_tests.sh ci/terrateam_issue_relay
collected 19 items
tests/test_relay.py ...................                                  [100%]
============================== 19 passed in 1.45s ==============================
```

A scheduled job deletes inactive relay branches after 30 hours. Terrateam still owns plan execution; the relay only translates the issue command into its existing PR protocol.
