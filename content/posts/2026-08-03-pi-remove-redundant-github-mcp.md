---
title: "pi: remove redundant github MCP"
date: 2026-08-03T18:47:51+02:00
tags:
  - ai
  - dev
  - pi
---

[Previously]({{< ref "2025-10-17-mcp-model-context-protocol-considered-harmful" >}}).

I've finally removed the GitHub MCP server from my [Pi](https://pi.dev/)
configuration, after piloting it for a while with [`pi-mcp-adapter`](https://github.com/nicobailon/pi-mcp-adapter).

GitHub already has a mature CLI (`gh`) installed and authenticated:

```shell
% gh --version
gh version 2.97.0 (2026-07-31)
https://github.com/cli/cli/releases/tag/v2.97.0

% gh auth status
github.com
  ✓ Logged in to github.com account thiagowfx (keyring)
  - Active account: true
  - Git operations protocol: ssh
```

`gh` handles pull requests, issues, workflows, and releases directly. Anything
else remains available through `gh api`, including GraphQL. The MCP server added
another interface without adding capability.

```diff
 {
   "mcpServers": {
-    "github": {
-      "auth": "bearer",
-      "bearerToken": "!gh auth token",
-      "url": "https://api.githubcopilot.com/mcp"
-    },
     "slack-mcp": {
```

MCP remains useful for APIs without a better (or any) CLI, but it should be
avoided wherever possible.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
