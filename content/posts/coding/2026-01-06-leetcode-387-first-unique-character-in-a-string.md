---
title: "LeetCode #387: First Unique Character in a String"
date: 2026-01-06T20:59:58-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #387: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string):

```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1
```
