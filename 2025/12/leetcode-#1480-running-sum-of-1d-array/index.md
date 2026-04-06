---
title: "LeetCode #1480: Running Sum of 1d Array"
url: https://perrotta.dev/2025/12/leetcode-%231480-running-sum-of-1d-array/
last_updated: 2026-01-03
---


[LeetCode #1480: Running Sum of 1d Array](https://leetcode.com/problems/leetcode-#1480:-running-sum-of-1d-array):

```python
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
```

Primitives:

```python
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []

        acc = 0
        for num in nums:
            acc += num
            ans.append(acc)

        return ans
```

