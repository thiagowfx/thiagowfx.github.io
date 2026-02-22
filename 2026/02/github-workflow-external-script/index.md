
**Problem statement**: execute a `.js` script in a GitHub workflow. The script
must be stored in a separate file (than the workflow) in the same git
repository.

Why store the file separately?

- Inlining a big script is ugly and very non-elegant
- No syntax highlighting when updating the script → error-prone
- Risk of messing up with string interpolation or escapign characters →
  error-prone
- Limited ability to use formatters and linters in inlined scripts

The following approach, taken from a real example, works well:

```shell
% tree {repo root}/.github/
.github/
├── scripts
│   └── drift-summary.js
└── workflows
    ├── drift-summary.yml
    [...]
```

```yaml
name: 'Drift Summary'

on:
  schedule:
    - cron: '0 9 * * MON-FRI'
  workflow_dispatch:

permissions:
  issues: write

jobs:
  summarize:
    name: 'Update drift summary issue'
    runs-on: ubuntu-latest
    steps:
      - name: 'Checkout repository'
        uses: actions/checkout@1af3b93b6815bc44a9784bd300feb67ff0d1eeb3 # v6.0.0
        with:
          persist-credentials: false

      - name: 'Aggregate drift and update summary'
        uses: actions/github-script@f28e40c7f34bde8b3046d885e986cb6290c5673b # v7
        with:
          script: |
            const script = require('./.github/scripts/drift-summary.js');
            await script({ github, context });
```

Use [`github-script`](https://github.com/actions/github-script) + [`require`](
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

