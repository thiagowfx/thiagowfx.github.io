
https://github.com/frnmst/md-toc:

> Automatically generate and add an accurate table of contents to markdown files.

Adopting it via [pre-commit](https://pre-commit.com) in a git repository is very
straightforward:

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/frnmst/md-toc
    rev: 4a8b796dbde00f71eb1a51b075462f825f872c34 # frozen: 9.0.0
    hooks:
      - id: md-toc
```

Next, update `README.md` to include `<!--TOC-->` where the table of contents
should be inserted.

Run `pre-commit run -a md-toc` once to generate and preview the results:

```markdown
<!--TOC-->

- [GitOps Pipeline for Terraform](#gitops-pipeline-for-terraform)
  - [CI status](#ci-status)
  - [Key Objectives](#key-objectives)
  - [The Workflow](#the-workflow)
  - [Core Features](#core-features)

<!--TOC-->
```

