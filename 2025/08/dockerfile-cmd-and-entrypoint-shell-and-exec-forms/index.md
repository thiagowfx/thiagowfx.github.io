
Today I filed a github issue against the
[`dockerfmt`](https://github.com/reteps/dockerfmt/) project, which I copy
verbatim here given its surprising behavior.

## [reteps/dockerfmt#33](https://github.com/reteps/dockerfmt/issues/33)

Consider this sample `Dockerfile` (abridged version of a real-world scenario):

```
ENTRYPOINT sleep infinity
CMD sleep infinity
```

Let's run `dockerfmt` (v0.3.7) in it:

```
% dockerfmt Dockerfile
ENTRYPOINT ["sleep", "infinity"]
CMD ["sleep", "infinity"]
```

At first glance, everything looks OK. The problem is that this transformation is not a no-op.

Looking at the docs:

- https://docs.docker.com/reference/dockerfile/#cmd
- https://docs.docker.com/reference/dockerfile/#shell-and-exec-form

> If CMD is used to provide default arguments for the ENTRYPOINT instruction, both the CMD and ENTRYPOINT instructions should be specified in the [exec form](https://docs.docker.com/reference/dockerfile/#exec-form).

The difference is:

- the original code yields `sleep infinity` (correct!)
- the transformed code yields `sleep infinity sleep infinity`, which is an error (sleep: `no such argument sleep`)

One could argue that the original code is odd – the following would be conceptually simpler, and more idiomatic:

```
ENTRYPOINT ["sleep"]
CMD ["infinity"]
```

Or even:

```
ENTRYPOINT ["sleep", "infinity"]
```

Nonetheless, IMHO `dockerfmt` should not change the behavior in this case.

## Notes

[`shell` and `exec`
forms](https://docs.docker.com/reference/dockerfile/#shell-and-exec-form) have
distinct forms:

- `INSTRUCTION ["executable", "param1", "param2"]` (exec form)
- `INSTRUCTION command param1 param2` (shell form)

> The exec form makes it possible to avoid shell string munging, and to invoke
> commands using a specific command shell, or any other executable. It uses a
> JSON array syntax, where each element in the array is a command, flag, or
> argument.

> The shell form is more relaxed, and emphasizes ease of use, flexibility, and
> readability. The shell form automatically uses a command shell, whereas the
> exec form does not.

`dockerfmt`
[prefers](https://github.com/reteps/dockerfmt/blob/290b5f78fbf3134024eb3366880754beee5dbe69/lib/format.go#L483)
the exec form, for whatever reason.

There's even a [code
comment](https://github.com/reteps/dockerfmt/blob/290b5f78fbf3134024eb3366880754beee5dbe69/lib/format.go#L480):

> `// this can technically change behavior. https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact`

Surprise surprise! The issue I reported is precisely due to a change of
behavior.

