---
title: "LeetCode #905: Sort Array By Parity"
date: 2025-12-30T19:29:46-03:00
tags:
  - coding
rss: false
---

[LeetCode #905: Sort Array By Parity](https://leetcode.com/problems/leetcode-#905:-sort-array-by-parity):

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 == 1]
```

Or with `sort`:

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x & 1)
```

Or:

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x & 1)
        return nums
```
