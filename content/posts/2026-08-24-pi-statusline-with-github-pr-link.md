---
title: "pi: statusline with GitHub PR link"
date: 2026-08-24T01:14:47+02:00
tags:
  - ai
  - bloggify
  - dev
  - git
  - pi
---

[Previously]({{< ref "2026-01-30-starship-github-pr" >}}).

**Problem statement**: the [`@narumitw/pi-github-pr`](https://www.npmjs.com/package/@narumitw/pi-github-pr)
statusline entry reports much more than I care about:

```text
PR #123: checks failing (2), changes requested, 3 comments
```

I want the clickable PR link and nothing else. Checks live in `gh pr checks`,
comments live on GitHub, they are the source of truth.

There's no knob for it in this particular pi extension. The wording is hardcoded
in `formatCompactStatus()`, and the single option the extension takes
(`refreshIntervalMs`) is unreachable, because pi calls the default export with
`pi` alone. Nothing lighter exists on the registry either — everything else is a
full footer replacement:

```shell
% for q in "pi-extension%20pull%20request" "pi-extension%20statusline"; do
    curl -s "https://registry.npmjs.org/-/v1/search?text=$q&size=25" |
      jq -r '.objects[].package | select(.name | test("^(@[^/]+/)?pi-")) | "\(.name) — \(.description)"'
  done | grep -iE "pull request|statusline|footer" | sort -u
@feniix/pi-statusline — Fixed two-line status footer for pi with model, thinking, context, git, token, worktree, and skill indicators
@narumitw/pi-github-pr — Pi extension that shows GitHub pull request review, checks, and comment status.
@narumitw/pi-statusline — Pi extension that replaces the footer with an information-rich statusline.
[...]
```

Then we'll simply fork it away: 65 lines of local extension replace the 600+ of
the extension:

```typescript {filename="agent/extensions/github-pr-link.ts"}
export function formatPrLink(stdout: string): string | undefined {
	let pr: { number?: unknown; url?: unknown; state?: unknown };
	try {
		pr = JSON.parse(stdout);
	} catch {
		return undefined;
	}
	if (pr.state !== "OPEN") return undefined;
	if (typeof pr.number !== "number" || !Number.isFinite(pr.number)) return undefined;
	const label = `PR #${pr.number}`;
	return typeof pr.url === "string" ? osc8Link(pr.url, label) : label;
}

export default function (pi: ExtensionAPI) {
	let request = 0;

	const refresh = async (ctx: ExtensionContext) => {
		request += 1;
		const current = request;
		let status: string | undefined;
		try {
			const result = await pi.exec("gh", ["pr", "view", "--json", "number,url,state"], {
				cwd: ctx.cwd,
				signal: ctx.signal,
				timeout: GH_TIMEOUT_MS,
			});
			if (result.code === 0 && !result.killed) status = formatPrLink(result.stdout);
		} catch {
			status = undefined;
		}
		if (current === request && !ctx.signal?.aborted) ctx.ui.setStatus(STATUS_KEY, status);
	};

	pi.on("session_start", async (_event, ctx) => refresh(ctx));
	pi.on("agent_end", async (_event, ctx) => refresh(ctx));
	pi.on("session_shutdown", async (_event, ctx) => {
		request += 1;
		ctx.ui.setStatus(STATUS_KEY, undefined);
	});
}
```

The `osc8Link()` helper wraps the number in an OSC 8 hyperlink, so the entry is
clickable in the terminal (Cmd + click in Ghostty, for example):

```shell
% node --experimental-strip-types -e '
const { formatPrLink } = await import("/Users/thiago.perrotta/.pi/agent/extensions/github-pr-link.ts");
const { execFileSync } = await import("node:child_process");
const out = execFileSync("gh", ["pr", "view", "14215", "-R", "cli/cli", "--json", "number,url,state"], { encoding: "utf8" });
console.log("gh stdout:", out.trim());
console.log("status:", JSON.stringify(formatPrLink(out)));
'
gh stdout: {"number":14215,"state":"OPEN","url":"https://github.com/cli/cli/pull/14215"}
status: "\u001b]8;;https://github.com/cli/cli/pull/14215\u0007PR #14215\u001b]8;;\u0007"
```

Dropping the counters also dropped the second network call: the package pairs
every `gh pr view` with a GraphQL query for comment and review totals, and polls
every 60 seconds on top of session start, branch changes, and agent turns. One
`gh pr view` on session start and after each turn is enough. A branch switch
lands on the next turn end anyway, because switching branches means running
`git checkout`.

Every failure path — no PR, merged PR, missing `gh`, unauthenticated `gh` — just
clears the entry:

```shell
% node --experimental-strip-types --test agent/extensions/tests/github-pr-link.test.ts
✔ formatPrLink links open PRs and hides everything else (0.601333ms)
✔ osc8Link rejects non-http schemes (0.079ms)
✔ session start shows the PR link (0.526625ms)
✔ agent end clears the entry when gh fails (0.094167ms)
✔ agent end clears the entry when gh is missing (0.093125ms)
✔ aborted turn keeps the previous entry (0.466084ms)
✔ session shutdown clears the entry (0.104292ms)
✔ a stale refresh does not overwrite a newer one (0.165791ms)
ℹ pass 8
ℹ fail 0
```

The whole swap:

```shell
% pi uninstall npm:@narumitw/pi-github-pr
Removing npm:@narumitw/pi-github-pr...
Removed npm:@narumitw/pi-github-pr

% git --no-pager show --stat --oneline HEAD
4dadda2 pi: replace pi-github-pr with a link-only extension
 pi/.pi/README.md                                   |   4 +-
 pi/.pi/agent/extensions/github-pr-link.ts          |  65 ++++++++++
 .../agent/extensions/tests/github-pr-link.test.ts  | 139 +++++++++++++++++++++
 pi/.pi/agent/settings.json                         |   3 +-
 4 files changed, 207 insertions(+), 4 deletions(-)
```

Files under `~/.pi/agent/extensions/*.ts` are auto-discovered, so `/reload`
picks it up without restarting the session.
