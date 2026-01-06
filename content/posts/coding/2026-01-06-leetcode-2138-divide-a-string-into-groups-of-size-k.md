---
title: "LeetCode #2138: Divide a String Into Groups of Size k"
date: 2026-01-06T17:03:54-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2138: Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k):

```python
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        for i in range(0, len(s), k):
            if len(s) - i >= k:
                ans.append(s[i:i + k])

        if len(s) % k > 0:
            r = (k - (len(s) % k))
            ans.append(s[-(len(s)  % k):] + fill * r)

        return ans
```
