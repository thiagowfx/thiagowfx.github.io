---
title: "pre-commit: additional dependencies in golang"
date: 2024-11-21T12:36:35+01:00
tags:
  - dev
---

When working with [pre-commit.com](https://pre-commit.com/) and specifying
`language: golang` for a given hook, you may want to install dependencies as
part of the hook bootstrapping process.


Recently I needed to do so for [yq](https://github.com/mikefarah/yq)[^1]:

The `.pre-commit-config.yaml` looked like this:

```yaml
repos:
  - repo: local
    hooks:
      - id: helm-dirname-must-match-chart-name
        name: Helm chart directory name must match the chart name
        files: /Chart\.(yml|yaml)$
        entry: ci/helm_check_match_dirname_chart_name.sh
        language: golang
        additional_dependencies:
          - https://github.com/mikefarah/yq
```

Context for the hook and the script: https://stackoverflow.com/q/79166730/1745064.

It didn't work. It's necessary to drop the `https://` prefix.

```yaml
repos:
  - repo: local
    hooks:
      - id: helm-dirname-must-match-chart-name
        name: Helm chart directory name must match the chart name
        files: /Chart\.(yml|yaml)$
        entry: ci/helm_check_match_dirname_chart_name.sh
        language: golang
        additional_dependencies:
          - github.com/mikefarah/yq
```

That didn't work either. Then I realized I needed to specify an exact
version[^2]:

```yaml
repos:
  - repo: local
    hooks:
      - id: helm-dirname-must-match-chart-name
        name: Helm chart directory name must match the chart name
        files: /Chart\.(yml|yaml)$
        entry: ci/helm_check_match_dirname_chart_name.sh
        language: golang
        additional_dependencies:
          - github.com/mikefarah/yq@v4.44.3
```

It also didn't work! There was an error message about the need to specify `/v4`
in the path for whatever reason:

```yaml
repos:
  - repo: local
    hooks:
      - id: helm-dirname-must-match-chart-name
        name: Helm chart directory name must match the chart name
        files: /Chart\.(yml|yaml)$
        entry: ci/helm_check_match_dirname_chart_name.sh
        language: golang
        additional_dependencies:
          - github.com/mikefarah/yq/v4@v4.44.3
```

That worked! Test it:

```shell
pre-commit run --all-files helm-dirname-must-match-chart-name [--verbose]
```

[^1]: `yq` is like `jq` for YAML instead of JSON.

[^2]: `@latest` would also work. However, for the sake of reproducibility,
    pinning is more reliable.
