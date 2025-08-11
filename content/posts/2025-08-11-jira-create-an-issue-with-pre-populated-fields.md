---
title: "JIRA: create an issue with pre-populated fields"
date: 2025-08-11T14:31:09+02:00
tags:
  - dev
---

It is somewhat tedious to create issues[^1] in JIRA. It is a bloated and complex web
app, slow to load, with a myriad of fields to fill in.

Most of these input fields do not significantly change when working within a
single team. The common exceptions are the **Summary** (Issue title) and
**Description**. Priority and Assignee can be determined later on, during bug
triage.

It turns out JIRA supports [creating issues using direct links](https://confluence.atlassian.com/jirakb/how-to-create-issues-using-direct-html-links-in-jira-159474.html).

The documentation isn't the most user-friendly[^3] but, upon figuring it out, you
can build a URL such as:

```
https://{company}.atlassian.net/secure/CreateIssueDetails!init.jspa?pid={project-id}&issuetype=10003&summary=Component%3A%20Title&description=&customfield_10249=SRE&labels=quick-win
```

Notes:

- **Project ID**: you can figure out which one to use by following their
  [docs](https://support.atlassian.com/jira/kb/how-to-get-the-id-of-a-jira-project-from-a-web-browser/).
  **TL;DR**: Navigate to `<JIRA_BASE_URL>/rest/api/latest/project/{project-key}`, wherein
  the project key is something such as `INFRA` or `POPS`. This returns a JSON
  object, look for its top-level `id` field.

- **Issue Type**: 10003 = Story, 10004 = Task. If you want another type, see
  [docs](https://support.atlassian.com/jira/kb/finding-the-id-for-issue-types-in-jira-server-or-data-center/).

- **Summary** and **Description** are self-descriptive. They need to be URL-escaped.

- `customfield_12345` is for...well, custom fields. For example, we have a
  custom field to track which team the work item is assigned to.

Bookmark the URL for quick access from your web browser bookmarks bar[^2], or
perhaps from an app such as [RayCast](https://www.raycast.com/).


[^1]: "Issues" were [recently
    renamed](https://community.atlassian.com/forums/Jira-articles/It-s-here-Work-is-the-new-collective-term-for-all-items-you/ba-p/2954892)
    to "Work items". Do you have an issue with this?

[^2]: I prefer this option. The bookmark label (name) is `+`, very mnemonic.

[^3]: Google's [Issue Tracker](https://developers.google.com/issue-tracker/guides/access-ui) (_Buganizer_) supports a similar approach. For example, https://goo.gle/cftbug redirects to https://issues.chromium.org/issues/new?component=1456689&title=Chrome%20for%20Testing:%20&noWizard=true&pli=1&template=0 (I created this link back in the [CfT](https://goo.gle/chrome-for-testing) days).
