---
title: "Espanso for Github PR templates"
date: 2025-06-16T14:04:36+02:00
tags:
  - dev
---

It is super tedious to fill in [github PR templates]({{< ref
"2025-05-04-github-pull-request-template" >}}) manually.

It is more efficient to use a text snippet expander such as [Espanso]({{< ref
"2025-05-16-espanso-hello-world" >}}).

I found the following trigger works well:

```shell
% espanso edit
Editing file: /Users/thiago.perrotta/Library/Application Support/espanso/match/base.yml
```

```yaml
matches:
  - trigger: ":github:repo1"
    replace: |
      ## Summary

      $|$

      ## Jira Task

      - [ ] No ticket needed (check only if level of impact is No-op)

      https://corp.atlassian.net/browse/XXX

      ## Level of Impact

      Please select exactly one option. To change the level of impact, first
      unselect the current level of impact and then select the new level of
      impact.

      - [ ] 1 - High
      - [ ] 2 - Medium
      - [ ] 3 - Low
      - [x] 4 - No-op

      ## Impact Analysis

      N/A

      ## Test Plan

      TODO Insert test plan here.

      ## Checklist

      Check each when they are done or confirmed to not apply. If something
      here isn't checked, this isn't ready to be merged. Seriously. You are
      making your colleagues lives a lot easier by doing this consistently.

      - [x] Test Plan Fully Executed
      - [x] Does not require security review or security review complete
```

Usage:

- create a PR via the github UI
- type in `:github:repo1` in the PR description text area
- the cursor will automatically move to the Summary section (that's what `$|$`
  does as per [docs](https://espanso.org/docs/matches/basics/#cursor-hints)).

It's much quicker to trigger that expansion than to fill in the PR template
manually every single time. Of course, I still need to update the JIRA ticket
and the test plan in each PR.

Each repository has its own template. I use the repo name as the trigger. For
example: to trigger the template expansion for `https://github.com/corp/foo`,
map it to `:github:foo`.
