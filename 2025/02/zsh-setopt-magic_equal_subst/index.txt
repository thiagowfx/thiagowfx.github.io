
**Problem statement**: Write the following command line in `zsh`:

```shell
% terraform plan -var-file=../../../config/global-dns-changer-
```

Now press `<TAB>`.

**Expected**: Filename expansion.

**Observed**:

```
No matches for: `filename' or `file'
```

Ugh. How about some magic 🪄?

```shell
setopt magic_equal_subst
```

Now:

```shell
% terraform plan -var-file=../../../config/global-dns-changer-<TAB>
completing file
global-dns-changer-{foo}.tfvars  global-dns-changer-{bar}.tfvars
```

Yay!

There's a workaround if you don't want to set the aforementioned option. Just
remove the `=` character:

```shell
% terraform plan -var-file ../../../config/global-dns-changer-<TAB>
completing file
global-dns-changer-{foo}.tfvars  global-dns-changer-{bar}.tfvars
```

I find it's more convenient to have this option work in both situations though.

(via [Reddit](https://www.reddit.com/r/zsh/comments/10o018l/glob_expansion_and_tab_completion_after_the_sign/))

