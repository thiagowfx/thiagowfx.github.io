---
title: "jq: remove quotes from output"
url: https://perrotta.dev/2024/11/jq-remove-quotes-from-output/
last_updated: 2024-12-20
---


Given:

```
% aws eks --profile global --region us-east-1 list-clusters
{
    "clusters": [
        "aws-us-east-1-global-0"
    ]
}
```

Query:

```
% aws eks --profile global --region us-east-1 list-clusters | jq '.clusters'
[
  "aws-us-east-1-global-0"
]
```

Further:

```
% aws eks --profile global --region us-east-1 list-clusters | jq '.clusters[0]'
"aws-us-east-1-global-0"
```

What if we wanted to remove the quotes? Add `-r` (`--raw-output`):

```
% aws eks --profile global --region us-east-1 list-clusters | jq -r '.clusters[0]'
aws-us-east-1-global-0
```

