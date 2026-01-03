---
title: "LeetCode #139: Word Break"
date: 2025-09-16T01:08:11+02:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #139: Word Break](https://leetcode.com/problems/word-break/):

```python
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        @cache
        def solve(i):
            """Solvable for i..n-1"""
            assert i >= 0

            if i >= n:
                return True

            for word in wordDict:
                if s[i:].startswith(word):
                    if solve(i + len(word)):
                        return True

            return False

        return solve(0)
```

It is tempting to add the following condition:

```python
if s == "":
    return True
```

...but there's no need as it is a no-op; relying on the index is enough.

It is also tempting to convert `wordDict` into a set, but it does not provide
any value.
