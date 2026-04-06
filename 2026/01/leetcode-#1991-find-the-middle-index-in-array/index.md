---
title: "LeetCode #1991: Find the Middle Index in Array"
url: https://perrotta.dev/2026/01/leetcode-%231991-find-the-middle-index-in-array/
last_updated: 2026-01-06
---


[LeetCode #1991: Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array):

```python
from itertools import accumulate

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        acc = list(accumulate(nums))

        for i, num in enumerate(nums):
            if (acc[i - 1] if i > 0 else 0) == (acc[-1] - acc[i]):
                return i

        return -1
```

