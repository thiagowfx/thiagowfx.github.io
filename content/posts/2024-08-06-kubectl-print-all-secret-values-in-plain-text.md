---
title: "kubectl: print all secret values in plain text"
date: 2024-08-06T13:37:31+02:00
tags:
  - dev
---

**Problem statement**: Given a [kubernetes
secret](https://kubernetes.io/docs/concepts/configuration/secret/) with more
than one key-value pair, print **all** of them in plain text (i.e.
base64-decoded in this context).

**Edit(2024-08-08)**: It turns out I made a mistake. The effect of the post
below is akin to `kubectl get [...] -o yaml`. I'll keep the post for
bookkeeping purposes anyway.

Basically, something like:

```shell
kubectl cat secret -n infra-services my-cool-secret
```

Except that there is no `kubectl cat`, what a shame. It would be really great if
we had it, for consistency with `systemctl cat`. Oh well.

There is `kubectl edit` though – amen, just like `systemctl edit`. This will
open your `$EDITOR`. It's often inconvenient to copy text to the clipboard from
your terminal-based editor though, due to intricacies of different terminals,
shells, terminal multiplexers, and OSC-52, therefore I don't deem this as an
acceptable solution.

There is a simple trick though:

```shell
EDITOR=cat kubectl edit secret -n infra-services my-cool-secret
```

...which works exactly as you would expect `kubectl cat` to behave. It displays
a warning at the end:

```
Edit cancelled, no changes made.
```

...however it can be duly ignored.

If we didn't have this trick, we could have:

- written a bloated tool in golang to pipe to e.g. https://github.com/ashleyschuett/kubernetes-secret-decode ([via](https://itnext.io/secrets-in-plain-text-13a98f54ef97))
- used the `kubectl edit` trick above, with a decent terminal and OSC-52 setup
- used `jq` with its `map` and `base64d` constructs (c.f. [Stack
  Overflow](https://stackoverflow.com/questions/50286066/kubernetes-kubectl-print-all-secrets))
- used `kubectl describe` with `-o jsonpath`, specifying every single field, one
  by one (super tedious) c.f. [this previous post]({{< ref "2024-07-09-kubectl-get-secret-with-jsonpath-add-newline" >}})
