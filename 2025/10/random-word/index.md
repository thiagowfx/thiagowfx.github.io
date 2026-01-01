
**Problem statement**: get a random word via shell scripting. Assume a typical
Unix / POSIX environment is available.

There are various ways to do so.

## Dictionary shuffle

Pick a random word from the system dictionary:

```shell
% shuf -n 1 /usr/share/dict/words
acrochordon
```

`-n` controls how many words to pick.

Or use `sort -R`:

```shell
% sort -R /usr/share/dict/words | head -n 1
transcurrently
```

`-R` is `--random-sort`. I am amazed that this option even exists.

## Gibberish

Use `/dev/urandom`:

```shell
% tr -dc 'a-z' < /dev/urandom | head -c 8
zsdckwbs%
```

Use OpenSSL:

```shell
% openssl rand -base64 12 | tr -dc 'a-z' | head -c 8
hfwkwqmt%
```

