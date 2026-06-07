---
title: "terraform police"
date: 2026-06-08T01:21:44+02:00
tags:
  - dev
  - serenity
  - terraform
---

The Master wakes to a pager. Coffee is ready.

> **Apprentice**: "Master, who created the drift?"
>
> **Master**: "Which drift?"
>
> **Apprentice**: "The bucket tag — live state ≠ terraform config in git."
>
> **Master**: "Show me the chain."

They follow: pipeline → cronjob → github actions container → terraform CI bot → github pull request → human.

> **Apprentice**: "We found them. Shall we ~~retaliate~~ punish?"
>
> **Master**: "What would punishing do to the state?"

> **Apprentice**: "Teach them not to drift."
>
> **Master**: "Teach the pipeline to ask 'why' first."

> **Apprentice**: "And what if entropy persists?"
>
> **Master**: "Record why. The record is a lamp in the fog."

> **Apprentice**: "Who made the first drift in all systems?"
>
> **Master**: "Entropy."
>
> **Apprentice**: "Then we'll blame entropy?"
>
> **Master**: "Blame nothing. Write the JIRA ticket."

The apprentice writes the ticket. The pipeline asks "why" and then sleeps. The
pager blinks once. Dawn sets. Just another ordinary day goes by.

- - -

What does the "Terraform police" do, you asked?

It pursues active drifts in the terraform repository.

It chases the individual(s?) responsible for deepening chaos.

It teaches them how not to do so anymore.

Rinse and repeat.

Will the workload of the "Terraform police" ever end?

Is drift an ephemeral state?

Is this world a simulation?

Is this a world simulation?
