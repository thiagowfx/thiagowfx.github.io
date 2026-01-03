---
title: "Helm: enforce the directory name matches the chart name"
date: 2024-11-12T11:13:06+01:00
tags:
  - bestof
  - dev
  - kubernetes
---

**Problem statement**: Given a helm chart called `foo`, enforce that its `Chart.yaml` file lives in a directory called `foo`[^1].

[^1]: _Why_? For ease of management, simplicity, consistency & uniformity.

## Background

In 2016, this [used to be](https://github.com/helm/helm/pull/818/) the default behavior in Helm:

> fix(helm): produce error if package name is inconsistent

In 2018, this enforcement was [removed](https://github.com/helm/helm/pull/4141):

> remove dirname constraint on helm package

We would like to reintroduce this requirement in our Helm charts codebase, as a best practice, to prevent chart name collisions.

What would be the most native way to accomplish that?

I would probably write a git pre-commit hook if there is no native way (e.g. via some `helm lint` flag).

## Solution

Use the following script with [pre-commit](https://pre-commit.com/):

```bash
#!/usr/bin/env bash
#
# Check that the directory name matches the chart name in Chart.yaml.
#
# Examples:
#   - foo/Chart.yaml with "name: hey-foo" fails the check.
#   - foo/Chart.yaml with "name: foo" passes the check.
#
# Usage: $0 [path/to/chart/Chart.yaml ...]

for chart in "$@"; do
	dirname="$(basename "$(dirname "$chart")")"

	# Remove trailing slash.
	dirname="${dirname%/}"

	# Fetch chart name from Chart.yaml.
	chart_name="$(yq e '.name' "$chart")"

	if [[ $dirname != "$chart_name" ]]; then
		echo "error: directory name '${dirname}' does not match chart name '${chart_name}'"
		exit 1
	fi
done
```

## Reference

I asked and self-answered this question on [Stack Overflow](https://stackoverflow.com/questions/79166730/how-to-enforce-that-the-directory-name-must-match-the-chart-name/79180650#79180650).
