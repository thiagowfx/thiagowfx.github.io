
**Context**: Helm charts use `.Values.{foo}` in `templates/` for templating from
`values.yaml`.

**Goal**: Return all unique values used in `templates/`. The intention for it is
to add them all as defaults to `values.yaml`.

First attempt:

```shell
$ ack '\.Values\.'
```

One could proceed manually from here, but this is not very ergonomic in big helm
charts.

A better (and more precise) attempt is:

```shell
$ ack '\.Values[\.\w+]+'
```

This will match `.Values.config.foo`, in addition to `.Values.foo`.

To return only the matched strings, add `-o`:

```shell
$ ack -o '\.Values[\.\w+]+'
```

Here is a real example:

```shell
$ ack -o '\.Values[\.\w+]+'
[...]
values.yaml
349:29:.Values.global.prometheus_scrape_interval
863:29:.Values.global.prometheus_scrape_interval
903:20:.Values.global.global_grafana_ingest_url
```

To return only the values, add `-h` (it will hide the filenames):

```shell
$ ack -o -h '\.Values[\.\w+]+'
[...]
.Values.global.prometheus_scrape_interval
.Values.global.prometheus_scrape_interval
.Values.global.global_grafana_ingest_url
```

Now all that is left to do is to pipe it to `sort -u`.

```shell
$ ack -o -h '\.Values[\.\w+]+' | sort -u
[...]
.Values.global.prometheus_scrape_interval
.Values.global.global_grafana_ingest_url
```

It turns out that `grep` also has a `-o` flag with a similar behavior.

