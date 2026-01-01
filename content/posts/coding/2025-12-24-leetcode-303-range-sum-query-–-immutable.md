---
title: "LeetCode #303: Range Sum Query – Immutable"
date: 2025-12-24T17:10:09-03:00
rss: false
categories:
  - coding
---

[LeetCode #303: Range Sum Query – Immutable](https://leetcode.com/problems/range-sum-query-immutable):

```python
class NumArray:
    def __init__(self, nums: List[int]):
        w = 0
        self.acc = []

        for num in nums:
            w += num
            self.acc.append(w)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] -(self.acc[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

Or optimized with stdlib:

```python
import itertools

class NumArray:
    def __init__(self, nums: List[int]):
        self.acc = list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] -(self.acc[left - 1] if left > 0 else 0)
```
