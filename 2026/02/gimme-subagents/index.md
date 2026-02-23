
**Scenario**: we're test-driving the adoption of a
[Terrateam](https://terrateam.io/) feature
[called](https://docs.terrateam.io/reference/configuration/stacks/)
[stacks](https://terrateam.io/stacks). The specifics aren't relevant here.

In a typical agentic LLM session with [Claude Code](https://claude.ai/code)[^1],
the feature was drafted (planned) and then subsequently implemented.

[^1]: Should I stop linking to their website? At this point, every Software
    Engineer has heard of Claude Code at least once, right?

Following that comes the important part: **testing**! As part of the testing
process I tend to resonate with [Thorsten
Ball](https://registerspill.thorstenball.com/p/joy-and-curiosity-71):

> Most of the time, when I work with Amp, I know in advance (a) what I want the
> resulting code to do and (b) how I will test that it does exactly that.
>
> Once Amp declares it's done writing code, I test. And what I mean is that I
> "test", in every possible meaning of the word. The goal is to make sure the
> code actually does what it's supposed to do. That can mean: asking Amp to run
> the unit tests, asking it to manually test in a browser, asking it to run a
> command, or check the data in the database, run the curl. With every tool I
> have — Amp, code, my hands and eyes — I test the happy path, the teary path,
> the edge cases. I make sure to test with existing data, no data, real data,
> fake data. I think about what might be different in production and how I could
> test that. Sometimes I ask Amp itself how I can manually verify what it just
> did and ask it to walk me through the testing.
>
> How exactly I test very much depends on what I'm testing. Not all
> functionality and code have the same blast radius. Some sit at the heart of a
> system, some are peripheral. Adjust accordingly.
>
> But once I've tested something and compared how it works with my mental model
> of how it's supposed to work, then the code, I find, becomes less important.
>
> Yes, I'll do spot-checks to make sure it isn't completely insane (less and
> less of a problem with these new models). I also go through my mental list of
> always-check-these things like (a) where and how is the data stored (b) will
> this box us in and prevent future changes (c) security (d) does it touch
> functionality I hadn't considered. Sometimes that can take a while, other
> times there's barely anything to do.

...hence I surely prompt the LLM to suggest me how to test the feature:

```
⏺ Here's how to test the stacks feature:

  1. Validate the config syntax

  just check-terrateam-tags

  This confirms all projects referenced in .terrateam/config.yml have valid tags, including the new corp-network-check tags.

  2. Verify tag assignments are correct

  Check that the right projects land in each stack:

  # Foundation layer projects
  just list-projects-by-tag network
  just list-projects-by-tag terraform-secrets
  just list-projects-by-tag atlas

  # Compute layer projects
  just list-projects-by-tag eks
  just list-projects-by-tag corp-network-check

  # Services layer (future)
  just list-projects-by-tag service-identity

  Confirm that every cluster project falls into exactly one of the three stacks.

  3. Validate the config file itself

  just validate-terrateam-config   # if this recipe exists
  # or simply:
  yamllint .terrateam/config.yml   # basic YAML syntax check

  4. Test on a real PR (the real test)

  Stacks are a Terrateam server-side feature — the ordering logic runs in Terrateam's CI, not locally. The only real end-to-end test is:

  [...]
```

For the sake of preserving the context window of my current session, I employ
the following technique:

```
❯ 1) OK (in a subagent)
  2) OK (in a subagent, in parallel)
  3) OK (in a subagent, in parallel)

  let's do these first. Prompt me before going to 4

⏺ 3 agents finished (ctrl+o to expand)
   ├─ Bash (Check terrateam tags validation) · 1 tool use · 13.3k tokens
   │  ⎿  Done
   ├─ Task (Verify tag assignments per stack) · 17 tool uses · 32.3k tokens
   │  ⎿  Done
   └─ Bash (Validate terrateam config YAML) · 7 tool uses · 16.5k tokens
      ⎿  Done
```

And that works exactly as you would expect it to.

```
⏺ All three checks passed:

  1. Tag validation (just check-terrateam-tags)

  All {redacted – number of projects} standalone projects are properly tagged.

  2. Stack tag assignment verification

  ┌─────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                  Check                  │                                                    Result                                                    │
  ├─────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Cluster projects missing from all stacks│ None — all {redacted – number of projects} cluster projects are covered                                      │
  ├─────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Cluster projects in multiple stacks     │ None — tag sets are disjoint                                                                                 │
  ├─────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Non-cluster projects in stacks          │ 10 projects (6 terraform-secrets, 1 opsgenie, 3 atlas) — all in cluster-foundation, expected/harmless per ADR│
  ├─────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Placeholder tags (not yet in use)       │ deploy, rds, service-identity — cluster-services stack is currently empty                                    │
  └─────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

  3. Config validation

  - yamllint: passed (zero warnings/errors)
  - just check: all checks passed (AWS profiles, terrateam tags, AWS provider tags)

  Everything looks good locally. Ready for step 4 (push branch, open PR, test Terrateam's stack ordering on a real PR) whenever you want to proceed.
```

_In prose_: consider using
[subagents](https://code.claude.com/docs/en/sub-agents) (i) to preserve your
[context window]({{< ref
"2025-10-17-mcp-model-context-protocol-considered-harmful" >}}), and (ii) to
speed up testing by running them in parallel.

One disadvantage: I'd avoid using subagents in this manner whenever the testing
procedures aren't clearly well-defined and scoped (for example, whenever they
are ambiguous or uncertain). Why? Because I'd rather have full control in these
complex scenarios, by having the ability to manually steer the LLM in real-time.
With subagents you have limited ability to do so.

Last but not least: subagents are not an exclusive feature of Claude Code:

- Pi has a couple of extensions that add subagents capabilities to it.
[Example](https://github.com/nicobailon/pi-subagents) (untested)
- And so does [OpenCode](https://opencode.ai/docs/agents/).
- I am a bit surprised to find out that Codex [does not](https://github.com/openai/codex/issues/2604) support them
yet. Or [does it](https://developers.openai.com/codex/multi-agent/)?

