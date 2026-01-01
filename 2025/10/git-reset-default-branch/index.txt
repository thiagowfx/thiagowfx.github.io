
**Problem statement**: Given an existing repository whose default branch is
`master`, make it become "fresh" (=fully reset it), as if it had just been
created.

```shell
# backup the current default branch, just in case
git branch backup-old-master
git push origin backup-old-master

# create an orphan branch
git checkout --orphan temp

# remove everything – use one or some of the following, accordingly
git reset --hard
rm {all files}
git rm {all files}

# create an initial commit – c.f. https://perrotta.dev/2025/02/git-blank-commit/
git blank

# delete the old default branch
git branch -D master

# rename temp to master, pick one of the following
git rb master        # this is my alias for "rename branch"
git branch -m master # the native way

# override the current master
git push --force origin master
```

