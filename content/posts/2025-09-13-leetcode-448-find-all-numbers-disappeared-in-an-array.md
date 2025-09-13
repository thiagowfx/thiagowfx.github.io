---
title: "LeetCode #448: Find All Numbers Disappeared in an Array"
date: 2025-09-13T06:49:32+02:00
tags:
  - coding
---

[LeetCode #448: Find All Numbers Disappeared in an Array](/find-all-numbers-disappeared-in-an-array/):

Set difference!

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
```

We could also craft the logic above more imperatively, but it's not as elegant:

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        for num in nums:
            seen.add(num)

        ans = []
        for num in range(1, len(nums) + 1):
            if num not in seen:
                ans.append(num)

        return ans
```

Can we do it with O(1) memory?

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        # [4, 3, 2, 7, 8, 2, 3, 1] ->
        # [1, 2, 2, 3, 3, 4, 7, 8]
        last = 0
        for num in sorted(nums):
            ans += list(range(last + 1, num))
            last = num

        ans += list(range(last + 1, len(nums) + 1))

        return ans
```
