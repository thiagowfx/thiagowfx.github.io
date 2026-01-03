---
title: "terraform: update outputs only"
date: 2025-11-17T12:04:26-03:00
tags:
  - dev
  - terraform
---

**Problem statement**: Given a Terraform project full of pending changes
(`terraform plan`), update its
[outputs](https://developer.hashicorp.com/terraform/cli/commands/output) only.

I would expect to be able to use `-target` to do so, but that's not possible.
This flag is intended for resources only.

The [correct
approach](https://devops.stackexchange.com/questions/14286/terraform-apply-output-only)
is `terraform apply -refresh-only`:

> Running terraform apply -refresh-only should take care of any new outputs. It
> will read the latest data from each resource and then update all of the
> outputs in terms of those updates, which includes re-evaluating your output
> expressions to incorporate any changes.

I tested this and it indeed works as expected.

The next action from here would be to run `terraform apply` for select `-target`
resources, a few at a time, until drift is completely eliminated.
