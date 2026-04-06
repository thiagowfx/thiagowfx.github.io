# 0012 — AI Scraper Poisoning

## Status

Rejected (not feasible with current hosting)

## Context

AI scraper bots are increasingly aggressive, ignoring `robots.txt` and consuming server resources while harvesting content for LLM training. [iocaine](https://lwn.net/Articles/1056953/) is a Rust-based tool that combats this by serving Markov-generated nonsense to detected bots, poisoning their training data instead of trying to block them.

## Decision

Not adopting iocaine or similar scraper-poisoning tools. The blog is hosted on GitHub Pages, which only serves static files. iocaine requires running as a reverse proxy / server process that inspects incoming requests and conditionally serves poisoned content — this is incompatible with static hosting.

## Alternatives Considered

- **`robots.txt`**: Already in place, but aggressive bots ignore it.
- **Cloudflare in front of GitHub Pages**: Would provide bot management, WAF rules, and rate limiting. Most practical option if protection is ever needed.
- **`ai.txt` / well-known metadata**: Newer convention, same honor-system problem as `robots.txt`.

## Notes

- GitHub Pages bears the server cost of scraping, not us — the impact is philosophical (content used for training without consent), not operational.
- If hosting moves to a VPS or similar in the future, iocaine becomes viable and this decision should be revisited.
