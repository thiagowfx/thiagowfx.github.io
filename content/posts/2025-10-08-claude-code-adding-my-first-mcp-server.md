---
title: "Claude Code: adding my first MCP server"
date: 2025-10-08T00:31:31+02:00
tags:
  - ai
  - bestof
  - dev
---

Lovely readers, I promise this is not turning into an AI blog[^1]. I am merely
documenting my baby steps.

I use JIRA all the time. It's our ~~bug~~[^2] issue tracker of choice.

And, now that I am slowly incorporating Claude Code in my daily workflow for git
commits and pull requests, it only feels natural to connect JIRA to it, even if
only for the sake of retrieving information from existing tickets and/or adding
context to PRs.

So here we go.

[From the Anthropic documentation](https://docs.claude.com/en/docs/claude-code/mcp):

> **Atlassian**
>
> Manage your Jira tickets and Confluence docs

```shell
% cd <gitops project>
% claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
Added SSE MCP server atlassian with URL: https://mcp.atlassian.com/v1/sse to local config
File modified: /Users/thiago.perrotta/.claude.json [project: /Users/thiago.perrotta/gitops]
```

[SSE](https://docs.claude.com/en/docs/claude-code/mcp#option-2%3A-add-a-remote-sse-server) stands for "Server-Side Events":

> SSE (Server-Sent Events) servers provide real-time streaming connections. Many
> cloud services use this for live updates.

That command is idempotent:

```shell
% claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
MCP server atlassian already exists in local config
```

What if I want to have it available for all projects? Use `--scope user`:

```shell
% claude mcp add --scope user --transport sse atlassian https://mcp.atlassian.com/v1/sse
Added SSE MCP server atlassian with URL: https://mcp.atlassian.com/v1/sse to user config
File modified: /Users/thiago.perrotta/.claude.json
```

The modification to `~/.claude.json`:

```json
{
  [...]
  "mcpServers": {
    "atlassian": {
      "type": "sse",
      "url": "https://mcp.atlassian.com/v1/sse"
    }
  }
}
```

So far so good. However no auth config was supplied yet.

```
% claude
> /mcp
Manage MCP servers
❯ 1. atlassian            △ disconnected · Enter to login
```

After pressing Enter and authenticating against our JIRA instance in a web
browser:

```shell
% claude mcp list
Checking MCP server health...

atlassian: https://mcp.atlassian.com/v1/sse (SSE) - ✓ Connected

% claude mcp get atlassian
atlassian:
  Scope: User config (available in all your projects)
  Status: ✓ Connected
  Type: sse
  URL: https://mcp.atlassian.com/v1/sse

To remove this server, run: claude mcp remove "atlassian" -s user
```

```
> /mcp
Atlassian MCP Server

Status: ✔ connected   ✔ authenticated
URL: https://mcp.atlassian.com/v1/sse
Config location: /Users/thiago.perrotta/.claude.json [project: /Users/thiago.perrotta/gitops]
Capabilities: tools
Tools: 27 tools

❯ 1. View tools
  2. Re-authenticate
  3. Clear authentication
  4. Reconnect
  5. Disable
```

```
Tools for atlassian (27 tools)

❯ 1.  Get current user information       read-only
  2.  List accessible resources          read-only
  3.  List Confluence spaces             read-only
  4.  Retrieve Confluence page           read-only
↓ 5.  List space pages                   read-only
```

Let's say I want to call the "Get current user information" tool.

```
Get current user information (atlassian) [read-only]

Tool name: atlassianUserInfo
Full name: mcp__atlassian__atlassianUserInfo

Description:
Get current user info from Atlassian
```

Just describe it in natural language:

* **Prompt**: "current user in JIRA"
* **Claude**:

```
> current user in JIRA
  ⎿  {
       "account_id": "{redacted}",
       "email": "{redacted}",
     … +22 lines (ctrl+o to expand)

⏺ Thiago Perrotta
  - Email: {redacted}
  - Account ID: {redacted}
  - Role: {redacted}
  - Department: {redacted}
  - Location: {redacted}
```

Then I tried basic CRUD operations in natural language:

* **Prompt**: "create an issue" - create: followed by further prompts with issue details ✅
* **Prompt**: "transition the issue to won't do" – update / delete ✅
* **Prompt**: "find an issue related to foo deployment in cluster bar") –  read ✅

Everything worked successfully.

I also tried:

* **Prompt** (plan mode on, thinking enabled): Propose a way to handle https://{corp}.atlassian.net/browse/INFRA-12528.

> ⏺ I'll fetch the details of the Jira issue to understand what needs to be handled.

I feel this will be quite useful from now on!

[^1]: For now?!?

[^2]: I blame _Google_, the corporation, for getting me accustomed to saying
    "file a bug" and "bug tracker". Not every ticket is a bug. Atlassian is
    trying to shovel the "work item" term onto us, but "issue" is the
    appropriate concept.
