---
title: "LeetCode #2154: Keep Multiplying Found Values by Two"
url: https://perrotta.dev/2026/01/leetcode-%232154-keep-multiplying-found-values-by-two/
last_updated: 2026-01-06
---


[LeetCode #2154: Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two):

```python
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)

        while True:
            if original in s:
                original <<= 1
            else:
                break

        return original
```

