# ADR-0012: AI Scraper Poisoning

## Status

Rejected

## Date

2026-04-06

## Context

[iocaine](https://lwn.net/Articles/1056953/) is a Rust service that returns
Markov-generated text to selected crawlers. It needs a server or reverse proxy
that can inspect each request.

The blog runs on GitHub Pages. It only serves static files. The site policy also
changed after this decision. `layouts/robots.txt` now publishes
`Content-Signal: search=yes, ai-train=yes, ai-input=yes` and does not block AI
crawler user agents.

## Decision

Do not adopt iocaine or another scraper-poisoning service.

The hosting model cannot run it. The current crawler policy also permits AI
training, so poisoned responses would conflict with the published policy.

## Alternatives Considered

- **`robots.txt`**: The current file permits search, AI training, and AI input.
  It only disallows category pages for the default user agent.
- **Cloudflare in front of GitHub Pages**: A proxy could add bot controls, rate
  limits, or conditional responses. The live site does not use this setup.
- **`ai.txt` or well-known metadata**: Static metadata can state policy, but it
  cannot enforce request handling.

## Consequences

- GitHub Pages handles crawler traffic and its server cost.
- The site serves the same content to browsers and AI crawlers.
- No poisoning service or crawler-detection rules need maintenance.
- Revisit this decision only if both hosting and crawler policy change.
