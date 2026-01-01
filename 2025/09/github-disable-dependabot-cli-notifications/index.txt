
Good morning!

```
% git push
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 189 bytes | 189.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: GitHub found 247 vulnerabilities on org/repo's default branch (8 critical, 86 high, 92 moderate, 61 low). To find out more, visit:
remote:      https://github.com/org/repo/security/dependabot
[...]
```

These are simply non-actionable by our team; we have a dedicated security team
to look into these matters. Even worse: the constant output makes us accustomed
to it, until it becomes background noise.

GitHub allows us to
[disable](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#configuring-notifications-for-dependabot-alerts)
these CLI notifications: Settings > Notifications
> System > "Dependabot alerts: New vulnerabilities" > "Notify me": "on GitHub"
> only.

