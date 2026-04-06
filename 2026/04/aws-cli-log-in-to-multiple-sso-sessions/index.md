---
title: "AWS CLI: log in to multiple SSO sessions"
url: https://perrotta.dev/2026/04/aws-cli-log-in-to-multiple-sso-sessions/
last_updated: 2026-04-05
---


**Problem statement**: given multiple AWS organizations, log in to all of them
using the `aws` CLI via SSO.

```shell
aws sso login --sso-session {corp1}
aws sso login --sso-session {corp2}
```

The `--sso-session` name comes from `~/.aws/config`:

```ini {filename="~/.aws/config"}
[sso-session {corp1}]
sso_start_url = https://{id}.awsapps.com/start
sso_region = us-east-2
```

