
Lately I've been employing (with great success) the following pattern in order
to test whether changes to helm charts are harmless (and expected):

```shell
cd path/to/my/helm/chart
git checkout origin/master  # or main
helm template -f values.yaml . > golden
git switch --create thiagowfx/my-feature-branch
# develop, develop, develop
helm template -f values.yaml . > candidate
diff candidate golden  # or icdiff
```

The `diff` output will reliably demonstrate whether your changes are WAI.

**Note**: If needed, pass `--release-name {foo}` to `helm template`.

This pattern is comparable to running a golden `helm install` followed by a
[`helm-diff`](https://github.com/databus23/helm-diff) (`helm diff upgrade`)
candidate in the cluster.

