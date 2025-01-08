---
title: "bash: distinguish between script invocation versus source"
date: 2025-01-07T22:08:20-03:00
tags:
  - dev
---

**Problem statement**: Given a `main.sh`[^1] bash script that does a bunch of
variable `export`s:

```shell
# [...]
export AWS_ACCESS_KEY_ID=$(echo "$credentials" | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "$credentials" | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "$credentials" | jq -r '.Credentials.SessionToken')
```

...we want to source it so that these exported variables become available in the
current shell context[^2]:

```shell
$ source ./main.sh
```

...at the same time, we want to prevent users from invoking it:

```shell
$ ./main.sh
```

...because, otherwise, the variables wouldn't be exported.

How can we distinguish between these two forms in `bash`?

The following snippet works in this scenario:

```shell
if [[ "$0" == "${BASH_SOURCE[0]}" ]]; then
    echo "error: do not invoke this script directly; instead, run \`source $0\`"
    exit 1
fi
```

The general scenario is:

```shell
if [[ "$0" == "${BASH_SOURCE[0]}" ]]; then
    echo "The script was invoked with ./main.sh"
else
    echo "The script was invoked with source main.sh"
fi
```

## LLM moment

I got it from ChatGPT + personal amends. If you're curious, this is the original
snippet obtained with the first prompt:

```
#!/bin/bash

if [[ $0 = "$BASH_SOURCE" ]]; then
    echo "The script was invoked with ./main.sh"
else
    echo "The script was invoked with source main.sh"
fi
```

Out of curiosity, I asked:

> improve this script

To which I got:

```
#!/bin/bash

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "The script was invoked with ./main.sh"
else
    echo "The script was invoked with source main.sh or . main.sh"
fi
```

...which is similar to my final version. Not bad! That said, you would hope
that, in 2025, this "improve this script" chain-of-thought prompt reasoning
would be part of the model out-of-the-box, oneshot. _Oh, well._


[^1]: It's for [this script]({{< ref "2024-12-17-skopeo-operate-container-images-and-registries" >}}).

[^2]: In this context the `./` is optional and was added only for clarity.
