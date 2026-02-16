---
title: "GitHub: set up scheduled reminders on Slack"
date: 2025-08-05T12:03:10+02:00
tags:
  - bestof
  - dev
---

If your organization uses GitHub and Slack, it's neat to have daily
notifications be delivered to you, to remind you of pending pull request
reviews.

How to configure: start from https://github.com/settings/reminders. There will be
an entry in "Available organizations". Click (+) "Configure reminder".

In the next screen (`https://github.com/settings/reminders/{organization}`),
you'll need to authorize the slack workspace integration.

Once that is done, pick your settings. I like:

- Weekdays
- Times: 09:00 AM in your local timezone
- Check off "Review requests assigned to you"
- Optionally check off "Review requests assigned to your team" (I leave this
  disabled as it's too noisy)
- Check off "Enable real-time alerts for pull requests"
  — Then check off all checkboxes under it except "Your team's pull request
    review is requested" (no team notifications) and Your pull request has
    failed checks (CI is too noisy).

Now, once a weekday, the github app will slack you messages like these:

```
Reviews assigned to you on {org}/gitops
[gitops#13172] Forget the old RabbitMQ instance (jason-bourne)
 2 hours stale · 2 hours old · Waiting on @Thiago Perrotta, SRE

Reviews assigned to you on {org}/secret-project
[secret-project#49852] Deploy Container: Mooney's proxy (joe-goldberg)
 5 days stale · 6 days old · Waiting on @Love Quinn
```

Be kind to your teammates. Don't leave them blocked on your reviews for more
than 24 hours!
