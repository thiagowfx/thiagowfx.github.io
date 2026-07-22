---
title: "pi: caveman mode"
url: https://perrotta.dev/2026/07/pi-caveman-mode/
last_updated: 2026-07-22
---


[Previously]({{< ref "2025-12-23-pi" >}}),
[previously]({{< ref "2026-06-25-caveman-talk-like-caveman-save-tokens" >}}).

**Problem statement**: adopt [caveman](https://github.com/JuliusBrussee/caveman)
in [pi](https://github.com/earendil-works/pi).

Pi isn't one of the 30+ agents caveman auto-detects. The install matrix
(`INSTALL.md`) lists agent detection rules one by one — `claude`, `cursor`,
`windsurf`, `opencode`, `openclaw`, etc — and pi isn't in it. Running the
one-liner installer here would just skip everything silently. Booo!

Rather than run someone else's `curl | bash` against an agent it wasn't built
for, """I""" reimplemented the terse-speak part natively, since `pi` already ships the
two primitives needed: [skills](https://agentskills.io/specification) and
[extensions](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md).

A
[skill](https://github.com/thiagowfx/.dotfiles/blob/7c495489141fd6036e4be70de9a065c53f7a8394/pi/.pi/agent/extensions/caveman.ts)
for `/skill:caveman` documentation, and an extension that rewrites the system
    prompt on every turn via `pi.on("before_agent_start", (event) => ...)`:

```typescript
const INSTRUCTIONS = `Caveman mode: on. Respond terse. Drop articles (a/an/the), filler (just/really/basically), pleasantries, hedging. Fragments OK. Short synonyms. Technical terms exact. Pattern: [thing] [action] [reason]. [next step]. Example — not: "Sure! I'd be happy to help you with that." yes: "Bug in auth middleware. Fix:"
Boundaries, always: code blocks, commit messages, and PR descriptions stay normal full verbosity, never compressed. Drop caveman style for security warnings, irreversible/destructive actions, or when the user seems confused — resume caveman after.`;

export default function (pi: ExtensionAPI) {
  let on = true; // auto-on by default, every session

  const applyStatus = (ctx: { ui: { setStatus: (k: string, v?: string) => void } }) => {
    ctx.ui.setStatus("caveman", on ? "[caveman]" : undefined);
  };

  pi.on("session_start", async (_event, ctx) => applyStatus(ctx));

  pi.on("before_agent_start", (event) => {
    if (!on) return;
    return { systemPrompt: `${event.systemPrompt}\n\n${INSTRUCTIONS}` };
  });

  pi.registerCommand("caveman", {
    description: "Toggle caveman terse-response mode: on|off (default: on)",
    handler: async (args, ctx) => {
      const arg = args.trim().toLowerCase();
      if (arg === "off" || arg === "stop" || arg === "normal") on = false;
      else if (arg === "on" || arg === "") on = true;
      else return ctx.ui.notify(`Unknown arg "${arg}". Use: on | off`, "error");
      applyStatus(ctx);
      ctx.ui.notify(on ? "Caveman mode on." : "Caveman mode off.", "info");
    },
  });
}
```

[`before_agent_start`](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md#before_agent_start)
fires on **every prompt**, before the agent loop starts, so
the instructions are re-appended each turn instead of relying on one message
that could get pruned from context. Dropped in
`~/.pi/agent/extensions/caveman.ts`, auto-discovered, no `/reload` needed after
the first load.

Unlike the Claude Code plugin, I skipped `lite`/`full`/`ultra`/`wenyan` — I
called that bloat back in June, and I'm not adding it to my own version
either. On or off is enough.

The result, _unprompted_:

> **user**: caveman on or off now?
>
> **assistant**: Caveman: on.
>
> **user**: how to turn it off?
>
> **assistant**: `/caveman off`

I also skipped the parts that don't have a pi equivalent: the statusline
savings counter, `/caveman-stats`, the `caveman-shrink` MCP proxy that rewrites
tool descriptions (a proxy that rewrites what an agent sees is exactly the
kind of thing worth reading before installing). The 40-line extension above
covers what I actually wanted.

One rule baked into both the skill and the extension: code, commits, and PRs
stay full verbosity, never compressed.

This experience was an eye-opener for me to realize how bloated the upstream
caveman project became.

- - -

🤖 *Drafted with `/bloggify`.*

