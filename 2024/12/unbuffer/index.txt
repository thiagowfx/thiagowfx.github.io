
The `unbuffer` binary comes from the [expect](https://www.nist.gov/services-resources/software/expect) package.
I didn't realize until now that it is hosted in NIST.gov!

There are two scenarios in which I find `unbuffer` quite helpful:

1) flush stdout line output immediately, in programs such as `tail` or `python`.
Julia Evans noted this
[in a blog post](https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/#solution-5-use-unbuffer):

```shell
% tail -f /some/log/file | unbuffer grep thing1 | grep thing2
```

Without `unbuffer` there's no guarantee `tail` would print its stdout output in
real time.

2) force stdout to write to a TTY (or to pretend that it will write to a TTY):

```shell
% unbuffer ls --color=auto | less -R
```

In this example, `less` will properly recognize and display color output from
`ls`.

