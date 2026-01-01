
[RFC 6901: JSON Pointers](https://www.rfc-editor.org/rfc/rfc6901):

> JSON Pointer defines a string syntax for identifying a specific value within a
> JavaScript Object Notation (JSON) document.

I wanted to point out to a key named `metadata -> annotations ->
argocd.argoproj.io/tracking-id`, wherein the arrows represent nesting.

There's a problem: the slash (`/`) cannot be used as is, it needs to be escaped.
And I always seem to forget how to escape it[^1].

**[Cheatsheet](https://www.rfc-editor.org/rfc/rfc6901#section-3)**:

- `~` -> `~0`
- `/` -> `~1`

Real-world usage, from [ArgoCD ignore differences](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/):

```
spec:
  ignoreDifferences:
    [...]
    # Workaround for a sync loop in External Secrets: https://github.com/argoproj/argo-cd/issues/18980
    - kind: Secret
      namespace: argocd
      jsonPointers:
        - /metadata/annotations/argocd.argoproj.io~1tracking-id
```

[^1]: No, it's not with a backslash (`\/`). That I can remember!

