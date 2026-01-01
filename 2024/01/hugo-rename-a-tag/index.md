
This blog is rendered by the means of a static site generator (SSG) called
[Hugo](https://gohugo.io/). Each blog post has a set of one or more tags
associated to it. The more posts I create, the more consolidated the tags become.

Sometimes I need to rename tags after-the-fact to better reflect the underlying
posts they represent.

This is how I typically do it. Start from the root of the git repository, then do:

```shell
% for file in content/posts/**/*.md; do gsed -i -e 's/- german/- deutsch/g' "$file"; done
```

The example above renames `german` -> `deutsch`.

This isn't the most robust way to do so, but it's the quickest one. For extra robustness, I'd do:

```shell
% fd -t f -e md -e gsed -i -x 's/- german/- deutsch/g'
```

...however it's always easier to remember the for loop syntax than the `fd`
one.

## Why `fd` instead of a `for` loop?

`fd(1)` is more elegant than shell wildcards. Although, in practice, both ways
are equivalent and should yield no difference.

## Why `gsed` instead of `sed`?

I am on macOS. The GNU version of `sed` does not create backup files, which is what I want in most cases. There's no need for backups because everything is checked into git already; if I make a mistake, I can always `git reset --hard` or `git checkout`. The BSD version of `sed` will leave this mess behind:

```shell
% fd -t f -e md -x /usr/bin/sed -i -e 's/- german/- deutsch/g'
% git st
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   2022-02-27-linux-us-international-keyboard-layout.md
	modified:   2022-04-03-translating-german-to-english.md
	modified:   2024-01-29-anki-find-all-notes-with-an-empty-field.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	2014-01-07-testando-uma-iso-no-linux-sem-o-virtualbox.md-e
	2014-04-18-mini-recovery-tipico-via-usb.md-e
	2014-05-01-instalando-o-gentoo-a-partir-do-arch.md-e
	2014-09-28-my-first-ebuild.md-e
	2015-01-07-the-eudyptula-challenge.md-e
[...]
```

There are even more of these `*-e` files, and they are super annoying. It's easy to get rid of them:

```shell
% rm **/*-e
```

...but why bother, if we can just stick to the more familiar GNU `sed` anyway?

## Caveats

Finally, note the caveat: this find and replace is naive and could end up replacing false positives! Nonetheless, I'm still a big fan of this approach, because it's the quickest one. As my blog is checked into `git` anyway, I can always easily review the changes before committing them:

```shell
% git diff
```

If there are too many diffs, then prefer an incremental approach:

```shell
% git add -p
```

Happy tag renaming! Well, this only happens every once in a while anyway.

