---
title: "LeetCode #268: Missing Number"
url: https://perrotta.dev/2025/12/leetcode-%23268-missing-number/
last_updated: 2026-01-03
---


[LeetCode #268: Missing Number](https://leetcode.com/problems/missing-number):

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i

        return len(nums)
```

Without `sort`:

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        return total - sum(nums)
```

