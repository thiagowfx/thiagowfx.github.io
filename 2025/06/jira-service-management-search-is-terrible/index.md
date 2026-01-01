
[JIRA Service
Management](https://www.atlassian.com/software/jira/service-management) is a
platform that tries to do way too many things (poorly) and has been plagued with
AI hype, but today we're only concerned with its Alerting platform (think
PagerDuty).

An anecdote from today:

I searched for the list of all alerts (open and closed) that match
[`chartmuseum`](https://chartmuseum.com/). Simple, right? That is one of the
main user journeys of the platform.

It returned no results. Zero. Nada. Zilch.

That cannot be! I just received an alert about chartmuseum. What gives?

The alerts have this title form:

- `[AWS CloudWatch]: chartmuseum-cpu-alarm-container-insights`
- `[AWS CloudWatch]: chartmuseum-cpu-alarm`

Surely `chartmuseum` should match them?

After some back-and-forth, I realized that searching for `chartmuseum-cpu-alarm`
would work, as well as `chartmuseum-cpu-alarm-container-insights`.

Aha! So they are doing an implicit word boundary search (think `\bterm\b` in
PCRE regex terms).

This is, frankly, a horrible default. I could not find any way to make a
substring match. Yet, it is unreasonable to expect us users to search for the
whole word like that. Sometimes I don't know what alert I am looking for.

There's a workaround. From their [docs](https://support.atlassian.com/jira-service-management-cloud/docs/search-syntax-for-alerts/):

> **Using asterisk (*) as a wildcard**
>
> Wildcards can only be used after characters and will only match from the start
> of character sequences. Character sequences need to be separated by a space
> for the wildcard to try and match to each sequence of characters.

Therefore `chartmuseum*` works. Or, even better: `*chartmuseum*`.

It's a pity, but the way forward here is to memorize that I need to add `*`
every single time.

Come on Atlassian, surely you can do better than this?

