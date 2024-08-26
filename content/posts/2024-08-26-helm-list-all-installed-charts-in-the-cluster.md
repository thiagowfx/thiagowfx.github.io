---
title: "Helm: list all installed charts in the cluster"
date: 2024-08-26T17:57:07+02:00
tags:
  - dev
  - devops
---

In theory this ought to be really easy:

```
$ helm ls -h
[...]
  -a, --all                  show all releases without any filter applied
  -A, --all-namespaces       list releases across all namespaces
```

<!--more-->

So...one of these should work, right?

```
helm ls -a
helm ls -A
```

I have a `sms-service` running in the cluster in the `default` namespace. If I
`grep` any of the previous commands to `sms`, it does not show up though.

Then...maybe `helm ls -a -A`? Nope.

Here's what works:

```
$ helm ls -a --max 9999 | grep sms
sms-service                  	default  	356     	2024-08-26 14:09:50.705277885 +0000 UTC	deployed	sms-v0.1.0
```

Kinda ridiculous, eh?

```
 -m, --max int              maximum number of releases to fetch (default 256)
```

From https://helm.sh/docs/helm/helm_list/:

> By default, up to 256 items may be returned. To limit this, use the '--max'
> flag. Setting '--max' to 0 will not return all results. Rather, it will return
> the server's default, which may be much higher than 256. Pairing the '--max'
> flag with the '--offset' flag allows you to page through results.

Happy helming.
