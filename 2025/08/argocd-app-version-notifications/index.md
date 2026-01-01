
**Problem statement**: when using [ArgoCD
notifications](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/),
starting off from their
[catalog](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/catalog/),
print the app chart version in addition to existing information.

More specifically, currently, a Slack notification message from Argo looks like
the following:

```
Cluster 37: Application heart-of-gold is unhealthy.
```

We want to improve it to:

```
Cluster 37: Application heart-of-gold (~1.18.3) is unhealthy.
```

The following diff (under a `template` block) accomplishes that:

```diff
-          {{if eq .serviceType "slack"}}:interrobang:{{end}} Cluster <{{.context.argocdUrl}}|*{{.context.clusterId}}*>: Application <{{.context.argocdUrl}}/applications/{{.app.metadata.name}}|`{{.app.metadata.name}}`> _sync_ by {{.app.status.operationState.operation.initiatedBy.username | default "_automation_" }} is _unknown_.
+          {{if eq .serviceType "slack"}}:interrobang:{{end}} Cluster <{{.context.argocdUrl}}|*{{.context.clusterId}}*>: Application <{{.context.argocdUrl}}/applications/{{.app.metadata.name}}|`{{.app.metadata.name}}`>{{if .app.spec.source.targetRevision}} ({{.app.spec.source.targetRevision}}){{else}}{{range .app.spec.sources}}{{if .targetRevision}} ({{.targetRevision}}){{break}}{{end}}{{end}}{{end}} _sync_ by {{.app.status.operationState.operation.initiatedBy.username | default "_automation_" }} is _unknown_.
```

Diving into it with pretty-printing[^1]:

```go-template
{{if .app.spec.source.targetRevision}}
  ({{.app.spec.source.targetRevision}})
{{else}}
  {{range .app.spec.sources}}
    {{if .targetRevision}}
      ({{.targetRevision}})
      {{break}}
    {{end}}
  {{end}}
{{end}}
```

If there's a single source in the helm chart, we extract its `targetRevision`.

Otherwise, when using a [multi-source
app](https://argo-cd.readthedocs.io/en/latest/user-guide/multiple_sources/), we
extract the first available `targetRevision`.

[^1]: These are
    [golang](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/GoTemplate/)
    [templates](https://pkg.go.dev/text/template).

