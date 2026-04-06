---
title: "LeetCode #3667: Sort Array By Absolute Value"
url: https://perrotta.dev/2026/01/leetcode-%233667-sort-array-by-absolute-value/
last_updated: 2026-01-06
---


[LeetCode #3667: Sort Array By Absolute Value](https://leetcode.com/problems/sort-array-by-absolute-value):

```python
class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return list(sorted(nums, key=lambda x: abs(x)))
```

