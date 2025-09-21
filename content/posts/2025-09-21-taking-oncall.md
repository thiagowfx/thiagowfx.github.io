---
title: "Taking oncall"
date: 2025-09-21T22:23:19+02:00
tags:
  - dev
---

When performing routine planned maintenance, one often needs to "take oncall".

This is standard terminology; for the uninitiated, it can be more formally
defined as "adding a schedule override to a given oncall shift". The override is
often brief (e.g. one hour), though it does not have to be.

Note that, in this definition, "taking oncall" is _not_ the same as swapping a
given oncall shift with a coworker.

Pedantries satisfied, now here we go:

**Problem statement**: make the action of taking oncall in [JIRA Service
Management (JSM)](https://www.atlassian.com/software/opsgenie/migration) (neé
OpsGenie) quick and efficient.

When using the web UI (https://{corp}.atlassian.net/jira/ops/who-is-on-call) it
often takes me a significant amount of time[^1] to remember [how to do
so](https://support.atlassian.com/jira-service-management-cloud/docs/override-an-on-call-schedule/).

A quicker way is to issue a command via Slack:

```
/jsmops assign oncall to me for TechOps
```

The command works as is: "me" is a magic word, and "TechOps" is the name of the
oncall rotation.

But I cannot remember this command, no matter how often I run it. I can
re-create it by running `/jsmops help`[^2], reading the documentation and then
crafting it. However, now a few wasted precious minutes were gone!

In order to streamline it in the future, I'll use [espanso]({{< ref
"2025-05-16-espanso-hello-world" >}}) to define this snippet (via `espanso
edit`):

```yaml
matches:
  - trigger: ":oncall"
    replace: "/jsmops assign oncall to me for TechOps"
```

From this point on, I just need to type `:oncall<ENTER>` on Slack. From
O(minutes) to O(seconds)!

I should probably introduce some structured organization to my espanso snippets
at some point. As they grow in quantity, it becomes more challenging to manage
them. For example, I thought of arranging this one with `:slack:oncall`, but I
don't have any other Slack commands to justify that yet.

[^1]: It should be a first-class operation of such a platform, 1-click away, in
    a place that is prominently visible in the UI.
[^2]: Oops, you can't run slack commands in threads; try again, in a channel.
