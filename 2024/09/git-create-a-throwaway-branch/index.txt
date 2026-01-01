
Let's say you want to submit a quick, perhaps even trivial, one-off pull request
(PR).

One step you can do to minimize the number of decisions[^1] to make is to have
a git alias that creates a branch with an arbitrary name.

```
% cat ~/.gitconfig
# ...
[alias]
nbt = !git nb \"thiagowfx/$(shuf -n1 /usr/share/dict/words | tr \"[:upper:]\" \"[:lower:]\")\"
```

Running `git nbt`[^2] will create a branch such as `thiagowfx/foo`.

The `{username}/` prefix is to make it easier to attribute your branches to
yourself, which can be handy when working collaboratively with other engineers
in a team.

The word after the slash is sourced from dictionary words on your system.

[^1]: See https://en.wikipedia.org/wiki/Decision_fatigue, https://en.wikipedia.org/wiki/The_Paradox_of_Choice.

[^2]: `nbt` stands for "new branch throwaway".

