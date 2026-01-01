
[zoxide](https://github.com/ajeetdsouza/zoxide):

> It remembers which directories you use most frequently, so you can "jump" to them in just a few keystrokes.

For example:

- `z perrotta.dev` jumps to `~/Workspace/perrotta.dev/`
- `z dotfiles` jumps to `~/.dotfiles`

I had one issue. Given these two directories:

- `~/corp/gitops`
- `~/corp/gitops-china`

`z gitops` was selecting the `gitops-china` directory, which I barely use.

In order to remove it from the frequently accessed directories list, do:

```shell
zoxide remove ~/corp/gitops-china
```

Now `z gitops` jumps to `~/corp/gitops`, as I originally intend most of the
time.

