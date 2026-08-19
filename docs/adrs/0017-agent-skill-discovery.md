# ADR-0017: Agent Skill Discovery

## Status

Proposed

## Date

2026-08-19

## Context

Personal Agent Skills are published from
[`thiagowfx/skills`](https://github.com/thiagowfx/skills). The repository is the
canonical source for skill instructions, support files, installation methods, and
updates.

The blog already publishes [`/llms.txt`](https://perrotta.dev/llms.txt). The
[`llms.txt` proposal](https://llmstxt.org/) permits arbitrary second-level sections
that contain links and descriptions. It does not assign special meaning to a
`## Skills` section.

Agent Skills standardizes each skill directory and its `SKILL.md`. It does not yet
standardize remote skill discovery. Two draft mechanisms address that gap:

- [Publishing Agent Skills through `llms.txt`](https://img.automators.work/docs/rfc-skills-in-llms-txt.md)
  defines a `## Skills` section. This remains an
  [open Agent Skills discussion](https://github.com/agentskills/agentskills/discussions/329).
- [Agent Skills Discovery via Well-Known URIs](https://github.com/cloudflare/agent-skills-discovery-rfc)
  defines `/.well-known/agent-skills/index.json`. Adoption into the Agent Skills
  specification remains an
  [open pull request](https://github.com/agentskills/agentskills/pull/254).

Both mechanisms work with static hosting. Neither is a final standard. Agent support
and proactive discovery are also limited.

## Decision

Add a `## Skills` section to the generated `/llms.txt` file. Link to the canonical
skills repository and describe its scope. This documents the skills through the
blog's existing LLM-facing index without copying skill content into the blog.

Do not publish `/.well-known/agent-skills/index.json` yet. Reconsider it after the
Agent Skills project accepts a remote-discovery specification and agent clients
implement it.

Do not describe the `## Skills` section as standards-compliant skill distribution.
It is valid `llms.txt` content and follows a draft convention, but the current
standards do not assign it machine-installation semantics.

## Alternatives Considered

- **Publish individual raw `SKILL.md` links in `/llms.txt`**: Closely follows the
  draft `## Skills` proposal, but skills with scripts and references need complete
  bundles. It also duplicates the repository's catalog and creates update drift.
- **Publish the draft well-known index now**: Provides structured metadata, artifact
  hashes, and direct downloads. Its schema and path can change before acceptance.
- **Use only the GitHub repository README**: Keeps one source of truth, but the blog
  does not expose the skills in its agent-facing index.
- **Copy skills into the blog**: Enables same-origin hosting, but creates a second
  source of truth and a synchronization requirement.

## Consequences

- Agents that read `/llms.txt` can find the personal skills repository.
- GitHub remains the source for installation and complete skill content.
- The blog adds no skill archives, hashes, or synchronization process.
- Clients that only probe `/.well-known/agent-skills/index.json` will not discover
  these skills through `perrotta.dev`.
- The decision must be reviewed when either discovery proposal becomes part of the
  Agent Skills specification.
