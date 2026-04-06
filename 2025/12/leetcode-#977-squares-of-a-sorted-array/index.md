---
title: "LeetCode #977: Squares of a Sorted Array"
url: https://perrotta.dev/2025/12/leetcode-%23977-squares-of-a-sorted-array/
last_updated: 2026-01-03
---


[LeetCode #977: Squares of a Sorted Array](https://leetcode.com/problems/leetcode-#977:-squares-of-a-sorted-array):

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(sorted(num ** 2 for num in nums))
```

