
When trying to optimize docker images in terms of size, the workflow is as
follows:

## Terminal 1

```shell
% docker build -f Dockerfile . -t argocd-download-tools
```

...possibly paired up with `entr` or `fswatch` depending on your eagerness for
automatic builds.

## Terminal 2

```shell
% docker image inspect argocd-download-tools | jq -r '.[0].Size' | numfmt --to=iec
134M
```

...possibly prepended with `watch`.

I wasn't aware of [`numfmt`](https://man.archlinux.org/man/numfmt.1):

> numfmt — Convert numbers from/to human-readable strings

...instead of displaying plain bytes, it converts numbers to human-readable
strings (à la `df -h` or `free -h`).

Regarding the [units](https://en.wikipedia.org/wiki/Binary_prefix): they don't
matter much, because we are only interested in an approximation, no need to
shave bytes off here. `SI` has 1k = 1000, whereas `IEC` has 1Ki = 1024.

