
It turns out the
[built-in](https://github.com/argoproj/gitops-engine/blob/master/pkg/health/health_statefulset.go)
health check for
[StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
in ArgoCD is not comprehensive enough.

It covers
[`RollingUpdate`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#update-strategies)
well enough, but `OnDelete` is incomplete.

More specifically:

**Observed**: whenever you push an update to an STS whose `.spec.updateStrategy`
is `OnDelete`, its health status stays as `Healthy`.

**Expected**: there should be an indication that the STS pods are not
up-to-date, and hence need to be restarted to incorporate the latest changes.

There is [an open bug](https://github.com/argoproj/argo-cd/issues/6527):
`Statefulset healthcheck does not work #6527` for it.

I managed to work around it by defining my own health check. This is an use case
where Gen AI is helpful, though it does not shine. I could not have Gen AI
produce a fully working health check for this scenario. Instead, I used it to
bootstrap a basic example, then had to tweak it until it worked. This has been
tested multiple times, I am reasonably confident it works well (some edge cases
could be missing though).

```lua
health_status = {}

if obj.status == nil then
  health_status.status = "Progressing"
  health_status.message = "Waiting for status to be reported"
  return health_status
end

local strategy = obj.spec.updateStrategy and obj.spec.updateStrategy.type or "RollingUpdate"
local spec_replicas = obj.spec.replicas or 1
local ready_replicas = obj.status.readyReplicas or 0
local updated_replicas = obj.status.updatedReplicas or 0
local status_replicas = obj.status.replicas or 0
local current_revision = obj.status.currentRevision or ""
local update_revision = obj.status.updateRevision or ""

if strategy == "OnDelete" then
  if ready_replicas == status_replicas and updated_replicas == spec_replicas then
    health_status.status = "Healthy"
    health_status.message = "All replicas are ready and updated (OnDelete strategy)"
  elseif updated_replicas == 0 then
    health_status.status = "Degraded"
    health_status.message = "No replicas have been updated (OnDelete strategy): 0/" .. spec_replicas .. " updated. Still running an old revision!"
  else
    health_status.status = "Progressing"
    health_status.message = "Progressing (OnDelete): " .. ready_replicas .. "/" .. status_replicas .. " ready, " .. updated_replicas .. "/" .. spec_replicas .. " updated"
  end
else
  if ready_replicas == status_replicas and updated_replicas == spec_replicas then
    if current_revision ~= update_revision then
      health_status.status = "Progressing"
      health_status.message = "Waiting for rollout to complete: revision mismatch (" .. current_revision .. " ≠ " .. update_revision .. ")"
    else
      health_status.status = "Healthy"
      health_status.message = "All replicas updated, ready, and revisions match"
    end
  else
    health_status.status = "Progressing"
    health_status.message = "RollingUpdate progressing: " .. ready_replicas .. "/" .. status_replicas .. " ready, " .. updated_replicas .. "/" .. spec_replicas .. " updated"
  end
end
return health_status
```

It is necessary to distinguish between `OnDelete` and `RollingUpdate`.

`OnDelete` should not use `currentRevision` / `update_revision`, as these values
don't mean anything for that update strategy. This can be observed
[upstream](https://github.com/argoproj/gitops-engine/blob/f8f1b61ba3fd5fcb647563db3106977e1364de31/pkg/health/health_statefulset.go#L63)
as well.

It is easy to write / tweak the health check when you look at the live STS
resource / manifest in the cluster. `obj` refers to the STS manifest (`kubectl
get sts -o yaml`). The most relevant field is `status:`.

If you deploy ArgoCD via its helm chart, add that check for `argocd-cm`. The
`values.yaml` file:

```yaml
argo-cd:
  configs:
    cm:
      resource.customizations.health.apps_StatefulSet: |
        health_status = {}
        [...]
```

This custom health check was partly inspired by a Prometheus alert we have:

```yaml
alert: StatefulSetUpdateNotRolledOut
expr: max without (revision) (kube_statefulset_status_current_revision unless kube_statefulset_status_update_revision) * (kube_statefulset_replicas != kube_statefulset_status_replicas_updated)
```

How long will it take until LLMs ~~steal~~ adopt this novel solution from me?

