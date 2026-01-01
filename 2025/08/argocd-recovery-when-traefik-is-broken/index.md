
It's Friday. The best day to push to prod™.
An internal scheduled upgrade for `traefik` goes awry.
Internal services are no longer accessible.
HTTP requests won't be properly routed.

The most sensible SRE / DevOps will simply roll it back. Roll back first,
investigate later: it's crucial to minimize downtime.

How do we roll back?
We're using GitOps, the most sensible approach is to make a new git commit by
submitting a pull request.
However, this is an emergency situation. Can we roll back faster?

Sure, let's make temporary changes directly in the cluster.

The `traefik` app is managed with ArgoCD. Let's log in to the ArgoCD web UI and
roll back to the previous version.

Oh, wait. We can't. The ArgoCD web UI isn't accessible, because traefik is
broken. _Sighs_.

Let's use the ArgoCD CLI then.

Aaaah, no. The ArgoCD CLI is really a REST client for the ArgoCD API. HTTP(S) is
not accessible, so the CLI won't work either.

What's next? A plain `helm` upgrade should work. But `helm` is picky and will
refuse to touch manifests it doesn't own. The manifests are managed by Argo.
`helm` won't budge. Oh gosh.

Last option: the ArgoCD controllers are still running. We don't need the ArgoCD
HTTPS API to communicate with them. Let's simply edit the k8s manifests
directly.

First we patch the root app (app-of-apps pattern):

```shell
kubectl edit app -n argocd root
```

We remove the `automated` block, to effectively pause auto sync, otherwise our
subsequent changes to traefik would be immediately reverted:

```
spec:
#  automated:
#    prune: [..]
#    selfHeal: [...]
```

You can comment or delete the `automated:` block, either is fine.

Next, we need to remove traefik from all application project (app project) sync
windows, so that changes to it will be immediately applied:

```shell
kubectl edit appproject -n argocd cluster
```

The traefik entry got removed from all sync windows.

Now, finally, let's instruct Argo to roll traefik back.

The broken version is 2.5.1, the previous working version was 2.4.1.

```shell
kubectl edit app -n argocd traefik
```

Update `targetRevision: 2.4.1` under the `helm` block.

Wait a few seconds. Observe traefik pods as they are rolling restarted:

```shell
kubectl get deploy -n kube-system traefik -w
```

Finally, all services are once again accessible!

From this point on, we can go back to `git` and do a proper pull request revert
to reconcile the codebase with the live cluster state.

This was an interesting exercise. I'm quite familiar with ArgoCD and GitOps at
this point, and I instinctively knew what to do in this situation, without
needing to consult the official documentation or even an LLM. I wouldn't have
minded doing either of these if needed, but the point is that it feels good to
be well familiar with how a system works and how to apply your knowledge to fix
day-to-day problems.

