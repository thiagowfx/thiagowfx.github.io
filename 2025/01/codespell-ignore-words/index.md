
When using [codespell](https://github.com/codespell-project/codespell) to spell
check a git repository, sometimes you may run into false positive words.

There are two ways to whitelist them.

The first one is via command-line arguments:

```shell
codespell -L=ist -L=regio
```

or

```shell
codespell -L=ist,regio
```

The second one is with a dedicated `.ignore-words.txt` file:

```shell
% cat .ignore-words.txt
# keep-sorted start
ist
regio
# keep-sorted end
% codespell -I .ignore-words.txt
```

