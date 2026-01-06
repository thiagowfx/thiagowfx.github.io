---
title: "LeetCode #3662: Filter Characters by Frequency"
date: 2026-01-06T20:28:28-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #3662: Filter Characters by Frequency](https://leetcode.com/problems/filter-characters-by-frequency):

```python
from collections import Counter

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        ans = []

        counter = Counter(s)

        for c in s:
            if counter[c] < k:
                ans.append(c)

        return ''.join(ans)
```
