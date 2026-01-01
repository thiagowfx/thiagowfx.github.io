
Our installation of `traefik` via `helm` got stuck today in such a way that its
pods did not terminate, even with successive `kubectl delete`.

`--force` did not work either :mildshock:

`--grace-period=0` (alongside `--force`) did the trick:

```shell
kubectl delete pod traefik-{...} --grace-period=0 --force --namespace kube-system
```

**Source**: https://stackoverflow.com/questions/35453792/pods-stuck-in-terminating-status

