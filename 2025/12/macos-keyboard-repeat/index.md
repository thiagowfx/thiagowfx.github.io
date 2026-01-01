
Run:

```shell
defaults write NSGlobalDomain InitialKeyRepeat -int 10
defaults write NSGlobalDomain KeyRepeat -int 1
```

...to configure the macOS keyboard repeat behavior for significantly faster
responsiveness.

- InitialKeyRepeat -int 10 — Sets the delay before a held key starts repeating
  (lower -> faster). Default is 15.
- KeyRepeat -int 1 — Sets the repeat rate once a key is held (lower -> faster).
  Default is 2.

Together, they make the keyboard feel snappier with minimal delay before repeat
and faster repetition speed.

Should have done that ages ago!

