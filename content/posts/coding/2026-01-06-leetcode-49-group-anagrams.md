---
title: "LeetCode #49: Group Anagrams"
date: 2026-01-06T23:55:13-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #49: Group Anagrams](https://leetcode.com/problems/group-anagrams):

```python
from collections import defaultdict
from collections.abc import Hashable

def is_hashable(obj) -> bool:
    return isinstance(obj, Hashable)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            cs = ''.join(sorted(s)) # canonical
            seen[cs].append(s)

        return list(seen.values())
```
