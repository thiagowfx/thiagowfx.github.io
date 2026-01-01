---
title: "LeetCode #1346: Check If N and Its Double Exist"
date: 2025-12-30T10:22:45-03:00
categories:
  - coding
---

[LeetCode #1346: Check If N and Its Double Exist](https://leetcode.com/problems/leetcode-#1346:-check-if-n-and-its-double-exist):

```python
from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = Counter(arr)
        for num in arr:
            if num == 0:
                if seen[0] > 1:
                    return True
            elif 2 * num in seen.keys():
                return True
        return False
```

Simpler:

```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen:
                return True
            if num % 2 == 0 and num // 2 in seen:
                return True

            seen.add(num)

        return False
```
