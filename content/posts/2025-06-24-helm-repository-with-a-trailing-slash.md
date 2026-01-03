---
title: "Helm repository with a trailing slash"
date: 2025-06-24T11:32:50+02:00
tags:
  - dev
  - kubernetes
  - pre-commit
---

[A repository URL with a trailing slash, and the same URL without a trailing
slash, are treated as different
repos](https://github.com/argoproj/argo-cd/issues/9857). We found this out the
hard way:

```
Failed to load target state: failed to generate manifest for source 1 of 2: rpc error: code = Unknown desc = error building helm chart dependencies: failed to add helm repository https://chartmuseum.{corp intranet}/orgs/{corp}/: failed to add repository: failed to get command args to log: `helm repo add https:--chartmuseum.{corp intranet}-orgs-{corp}- https://chartmuseum.{corp intranet}/orgs/{corp}/` failed exit status 1: Error: looks like "https://chartmuseum.{corp intranet}/orgs/{corp}/" is not a valid chart repository or cannot be reached: failed to fetch https://chartmuseum.{corp intranet}/orgs/{corp}/index.yaml : 401 Unauthorized
```

Let's put aside the fact the error message REALLY likes to repeat the repo name.

This is a repository that we've already configured, with proper authentication
credentials. Why would it start to fail now, all of a sudden?

You already got spoiled in the post title. Given `Chart.yaml`:

```yaml
apiVersion: v2
name: corp-postgres-operator
description: Corp Postgres Operator
type: application
version: 1.1.13

dependencies:
  - name: postgres-operator
    repository: https://chartmuseum.{corp intranet}/orgs/archive
```

And also:

```yaml
apiVersion: v2
name: corp-postgres-operator
description: Corp Postgres Operator
type: application
version: 1.1.13

dependencies:
  - name: postgres-operator
    repository: https://chartmuseum.{corp intranet}/orgs/archive/
```

These two dependencies end up being treated differently by Argo, even though
they are effectively the same. It's an upstream bug.

To work around it, I decided to simply remove all trailing slashes from
helm repository dependencies. Canonicalize everything!

A git [pre-commit.com hook](https://pre-commit.com) is a good mechanism to do so:

```yaml
repos:
  repo: local
  hooks:
    - id: helm-repo-trailing-slash
      name: Helm repositories must not contain trailing slashes in Chart.yaml
      files: Chart.yaml$
      language: pygrep
      entry: '\s*repository: [\w:/.]+/$'
```

Run `pre-commit run -a helm-repo-trailing-slash`, fix all violations, and then
never think about this again.

Should the upstream bug ever be fixed, we can remove this workaround.
