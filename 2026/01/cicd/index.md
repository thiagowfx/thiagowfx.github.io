
**CI/CD**: continuous integration / continuous delivery.

What do we care about?

- **Velocity / Speed**: If it takes too long, it adds friction.
- **Correctness / Safety / Reliability**: Reduce the blast radius. The pipeline
  should be readily available.

Architecture (CI):

- **Pre-submit checks**: At Google, TAP Presubmit. In the open, pre-commit.com.
  There's also husky (nodejs centric). And you could always use plain old
  vanilla `.git/hooks`.
- **Post-submit checks**: At Google, TAP PostSubmit. In the open, nightly cron
  jobs (e.g. with github workflows). There needs to be a notification mechanism.
  Email, slack, a CD dashboard.
- Test coverage report
- Formatters, linters, style guide
- Analyzers (static & dynamic)

Architecture (CD):

- Canary (mitigate risks) – guinea pigs. Smoke testing.
- Gradual rollouts – replace little by little -> rolling update.
- Blue-green deployments – maintain two sets of deployments, switch them
  dynamically. Zero-downtime, instant rollback, isolation for testing.
- Feature flags – dynamically toggle code paths on-demand (e.g. launchdarkly.com).

Testing pipeline – Pyramid of testing:

- Small, frequent, fast.
- Big, occasional, slow.
- Unit tests (single module) -> integration tests (various modules) ->
  end-to-end tests (various parts of the system) -> smoke tests (sanity check).
- Mocks, fakes, stubs.
- RpcReplay (Tin)
- Non-determinism: e.g. time, snynchronization, network, load, race conditions.
- Run tests locally vs in CI. Run tests hermetically, in an isolated fashion.
  Chrome for Testing.
- Multiple live environments: dev -> staging -> preprod -> prod, or daily-7,
  daily-6, ..., daily-1. Simpler: staging vs prod. Prod should be
  access-restricted / gated. Minimize permissions. Principle of least privilege.

Infrastructure as Code (IaC): the best ever!!

- Ansible, Chef, Puppet, SaltStack, Pyinfra.
- Terraform, OpenTofu and friends: Pulumi (programming languages instead of HCL
  e.g. python, typescript), Terraform CDK.
- Crossplane (Kubernetes IaC).
- Declarative vs Imperative.
- Idempotency.
- In general, make updates via git / gitops, and let the harness apply changes
  to the cloud infra. Avoid modifying live servers directly (live patching),
  unless during emergencies (oncall -> breakglass mechanisms).
- YAML, HCL, JSON. Gluing configuration languages all over the place.

Migrations of new DB schema without downtime?

- Decouple the migration from the code deployment
- Make the DB support both schemas (when possible), add new columns
- Deploy the new code (binary change)
- Deprecate the old schema / column
- Once all replicas are updated, remove the old schema / column
- Backwards compatibility for the win!

Slow build times?

- Caching (download of dependencies, generated artifacts, generated layers e.g.
  docker images)
- Parallelism – split + kick off multiple builds / tests (e.g. pytest supports
  this)
- Incremental builds – e.g. ccache, bazel/blaze, only build the parts of the
  graph that have changed
- Only build/test/run modified files -> detect via simple patterns, wildcards

When chaos ensues, what do you do?

Roll back immediately! Fix issues later. Do a postmortem analysis later. Easier
when you have cheap and/or automated rollbacks.

GitOps: ArgoCD, FluxCD. Operator. Agent continually polls, instead of CI pushing
changes. CI does not need access to prod.

Hermetic / reproducible builds. Code signing. SBOM.

DORA metrics / product health: deployment frequency, lead time for changes,
change failure rate, time to restore service.

How to secure CI/CD? Signed commits. Dependency pinning. Dependency cooldowns.
Dependency scanning (some tools available for that). Beware of supply-chain
attacks! Don't store secrets in the repo. Instead, use an external secrets
manager like AWS's, HashiCorp Vault, etc.

Flaky tests? Quarantine. Disable. Investigate off-line. Do not ever block the
pipeline! Risks losing confidence there.

Monorepo or various repos? Various repos: harder to maintain consistency,
enforce patterns. Monorepo: LSCs (large-scale changes). CODEOWNERS.

Security principles?

- Confidentiality (pssssh!!)
- Integrity (hashes)
- Availability (99.999%...)
- Authentication (it's me!)
- Authorization (yes, we can!)
- Non-repudiation (can't deny it!)
- Least privilege. Avoid: security through obscurity.

A kubernetes operator is a specialized controller that aims to reconcile state +
extends the base API with its own CRDs (e.g. external secrets, argocd,
prometheus stack). Watch CRDs, implement lifecycle tasks.

Do not forget hooks! Even Claude Code has them.

A Software Bill of Materials is a structured list that enumerates every
component, library, and dependency that makes up a software product. It provides
provenance and version information for each item, enabling stakeholders to
assess security, licensing, and supply‑chain risks.

