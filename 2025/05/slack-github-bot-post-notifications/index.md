
Assume your organization has the [Github
bot](https://github.com/integrations/slack)
[integrated](https://slack.github.com/) with Slack, and it's
already properly configured.

Assume you have a channel called `#team-reviews`.

**Problem statement**: subscribe the github repository `my-org/my-repo` to post
updates to that channel.

As per the
[documentation](https://github.com/integrations/slack?tab=readme-ov-file#subscribing-and-unsubscribing),
use the `/subscribe` and `/unsubscribe` commands. Send them in the
`#team-reviews` channel:

```
/github subscribe my-org/my-repo
```

> ✅ Subscribed to my-org/my-repo. This channel will receive notifications for
`issues`, `pulls`, `commits`, `releases`, `deployments`

In case you wish to subscribe to only pull requests and commits, follow up with:

```
/github unsubscribe my-org/my-repo issues,releases,deployments
```

> ✅ Subscribed to my-org/my-repo. This channel will receive notifications for
`pulls`, `commits`

Repeat for as many repositories as needed.

