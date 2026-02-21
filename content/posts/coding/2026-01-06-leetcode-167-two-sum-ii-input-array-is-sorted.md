---
title: "LeetCode #167: Two Sum II - Input Array Is Sorted"
date: 2026-01-06T14:51:55-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #167: Two Sum II — Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii---input-array-is-sorted):

Classic, linear:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        assert False
```

Binary search, optimistic:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            ## 1 2 3 4 5
            ## l   m   r
            mid = left + (right - left) // 2

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                if numbers[left] + numbers[mid] > target:
                    right = mid - 1
                else:
                    right -= 1
            else: ## numbers[left] + numbers[right] < target:
                if numbers[mid] + numbers[right] < target:
                    left = mid + 1
                else:
                    left += 1

        assert False
```
