---
title: "pi: asynchronous exit summaries"
date: 2026-07-27T18:18:38+02:00
tags:
  - ai
  - coding
  - dev
  - pi
  - pkm
---

**Problem statement**: `ctrl+d` in [pi](https://github.com/earendil-works/pi)
took several seconds to quit.

The culprit was [`pi-memory`](https://www.npmjs.com/package/pi-memory)'s
`session_shutdown` handler. It sent one last LLM request to summarize the
session, wrote its answer to the daily log, then ran `qmd update`. Pi awaits
all shutdown handlers, correctly, so quitting waited for everything:

```diff
pi.on("session_shutdown", async (event, ctx) => {
  const result = await generateExitSummary(ctx);
  fs.writeFileSync(filePath, entry, "utf-8");
  await runQmdUpdateNow();
});
```

Making that promise fire-and-forget would not work: Pi exits immediately after
shutdown, and either the in-flight request keeps Node alive or gets killed
before it can write anything.

Instead, I made the shutdown path write a durable job, synchronously:

```typescript
const job: ExitSummaryJob = {
  version: 1,
  id: randomUUID(),
  createdAt: new Date().toISOString(),
  date: todayStr(),
  reason,
  sessionId: shortSessionId(ctx.sessionManager.getSessionId()),
  conversationText: truncated.text,
  truncated: truncated.truncated,
  totalChars: truncated.totalChars,
};

const jobPath = path.join(
  EXIT_SUMMARY_JOBS_DIR,
  `${job.createdAt.replace(/[:.]/g, "-")}-${job.id}.json`,
);
fs.writeFileSync(jobPath, `${JSON.stringify(job)}\n`, { encoding: "utf-8", flag: "wx" });
```

The next interactive session starts an unref'ed worker. It atomically renames
one job to claim it, generates summary with active model, writes it back to
original day's daily log, and deletes job. Failed jobs return to queue. A
stale claimed job retries after ten minutes.

I kept upstream package intact by replacing it with a local package, effectively
forking it:

```shell
% pi remove npm:pi-memory
Removed npm:pi-memory
% pi install ~/.pi/agent/local/pi-memory-async
Installed /Users/thiago.perrotta/.pi/agent/local/pi-memory-async
% pi list
User packages:
  local/pi-memory-async
    /Users/thiago.perrotta/.pi/agent/local/pi-memory-async
```

Jobs live in `~/.pi/agent/memory/exit-summary-jobs/`. `ctrl+d` only writes one
JSON file now; summary happens during next session, without blocking exits.

**Source code**:
[pi-memory-async](https://github.com/thiagowfx/.dotfiles/tree/1f175b77a960a460b4e5cc677d6d6390e0cc0530/pi/.pi/agent/local/pi-memory-async).

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
