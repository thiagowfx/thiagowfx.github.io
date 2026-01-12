
The first time I heard about [Architectural Decision
Records](https://adr.github.io/) (ADRs) was with [George
Fairbanks](https://www.georgefairbanks.com/) (GHF) and [Titus
Winters](https://www.linkedin.com/in/tituswinters) in an internal training for
software engineers at Google Canada.

The concept has resonated with me:

> An Architectural Decision (AD) is a justified design choice that addresses a
> functional or non-functional requirement that is architecturally significant.
>
> [...]
>
> An Architectural Decision Record (ADR) captures a single AD and its rationale;
> Put it simply, ADR can help you understand the reasons for a chosen
> architectural decision, along with its trade-offs and consequences.
>
> The collection of ADRs created and maintained in a project constitute its
> decision log. All these are within the topic of Architectural Knowledge
> Management (AKM), but ADR usage can be extended to design and other decisions
> ("any decision record").

Some people liken these to
[RFCs](https://en.wikipedia.org/wiki/Request_for_Comments), although they are
not quite the same concept. RFCs tend to be much more formal and go through
rigorous review/approval before it becomes a standard.

ADRs, on the other hand, tend to be lightweight and objective. An archetypical
ADR captures a single decision about architecture in document form, alongside
its **rationale**, context and alternatives considered. **Rationale** is the
keyword here.

Rephrasing, in simpler terms: ADRs are a collection of rationales about a
project (software repository, if you will). They are incremental, long-living,
ever-evolving guidelines / rules of engagement for a given software realm.

ADRs (and RFCs as well, for that matter) are typically stored alongside source
code in a version‑controlled repository (_cof_ git _cof_):

```
% tree
.
└── adrs
    ├── 0001-foo.md
    ├── 0002-bar.md
    └── 0003-baz.md
```

They are usually numbered, though there's no hard rule saying that you have to
do so with monotonically increasing numbers. You could use calendar versioning
    (`2025-11-11-foo.md`), or any other numbering scheme if desired.

GHF has an introductory
[article](https://www.georgefairbanks.com/blog/comparch-wicsa-2011-panel-discussion-and-haiku-tutorial/)
about them. At the time (2011!), the coined term was "Architecture Haiku":

> You can't say anything in one page — or can you? An Architecture Haiku is a
> one-page, quick-to-build, über-terse design description. No project wants
> "shelfware" documentation, but many must communicate their design to others.
> Brevity is hard — what would you say in one page? With no page limit, experts
> suggest documenting everything but the kitchen sink. The one-page limit forces
> you to convey the essence of your design using compact language and concepts.

Enough introduction, here is my hot take.

I would like to argue that codebases that continually evolve with heavy usage of
LLM coding agents will strongly benefit from ADRs now, and especially in the
future.

The [AGENTS.md](https://agents.md/) format is a starting point, but it's a far
cry from disciplined ADR enactment. Bootstrapping your git repository with
scattered `AGENTS.md` / `CLAUDE.md` all over the place is a good initial
practice to tell the agent what to do and/or how to behave, but it does not
capture _decision records_ effectively.

The workflow I am starting to adopt in important repositories wherein I work
with teammates resembles this:

```
❯ tree docs/
docs/
├── adrs
│   ├── 0001-aws-secrets-manager-migration.md
│   ├── 0002-cluster-infrastructure-architecture.md
│   ├── 0003-slack-drift-notifications.md
│   └── README.md
```

A top-level `docs/` directory is the entrypoint for all `.md` files docs. Inside
it, we store our ADRs.

A `README.md` describes how to define an ADR:

```shell
# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for significant
technical decisions in the Terraform infrastructure.

## ADRs

<!-- markdownlint-disable MD013 -->
`> echo "| Number | Title | Status | Date |"; echo "|--------|-------|--------|------|"; for f in 0*.md; do num=$(basename "$f" .md | cut -d- -f1); title=$(head -1 "$f" | sed 's/^# ADR-[0-9]*: //'); status=$(awk '/^## Status/{getline;getline;print}' "$f"); date=$(awk '/^## Date/{getline;getline;print}' "$f"); echo "| [$num]($f) | $title | $status | $date |"; done`

<!-- BEGIN mdsh -->
| Number | Title | Status | Date |
|--------|-------|--------|------|
| [0001](0001-aws-secrets-manager-migration.md) | AWS Secrets Manager Migration | Proposed (Not Yet Implemented) | 2025-11-22 |
| [0002](0002-cluster-infrastructure-architecture.md) | Cluster Infrastructure Architecture | Accepted | 2025-12-01 |
| [0003](0003-slack-drift-notifications.md) | Slack Drift Notifications | Accepted | 2024-12-01 |
<!-- END mdsh -->
<!-- markdownlint-enable MD013 -->

## Adding New ADRs

1. Create a new file: `NNNN-short-title.md` (increment the number)
2. Use this template:

```markdown
# ADR-NNNN: Title

## Status

Proposed | Accepted | Deprecated | Superseded

## Date

YYYY-MM-DD

## Context

What is the issue that we're seeing that is motivating this decision?

## Decision

What is the change that we're proposing and/or doing?
Include its rationale.
Include alternatives considered where applicable.

## Consequences

What becomes easier or more difficult to do because of this change?
```

Whenever a new significant direction is adopted in the repository, or whenever
something (a tool, a dependency, a process) _quasi_-disrupting is introduced, it
probably deserves its own ADR.

It used to be tedious to write them by hand, but nowadays your LLM agent can
draft ADRs for you. Arguably, a plan[^1] file maps naturally to an ADR. All you
have to do is to add _some_ structure to them[^2].

**See also**: https://en.wikipedia.org/wiki/Architectural_decision

[^1]: _Plan_ in the context of "planning mode" that various agents have these
    days e.g. [Claude Code](https://code.claude.com/docs/en/model-config),
    [OpenCode](https://opencode.ai/docs/modes/#plan).
[^2]: But [don't](https://danielmiessler.com/blog/personal-ai-infrastructure)
    [_overdo_](https://github.com/steveyegge/beads) it.

