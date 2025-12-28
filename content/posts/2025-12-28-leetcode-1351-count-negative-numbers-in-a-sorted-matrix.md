---
title: "LeetCode #1351: Count Negative Numbers in a Sorted Matrix"
date: 2025-12-28T03:23:02-03:00
tags:
  - coding
rss: false
---

[LeetCode #1351: Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix):

Brute force, O(n^2):

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    ans += 1

        return ans
```

Horizontal binary search:

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            left = 0
            right = len(grid[i]) - 1

            while left < right:
                mid = (left + right) // 2

                if grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid

            if grid[i][left] < 0:
                ans += len(grid[i]) - left

        return ans
```

Same, with `bisect`:

```python
import bisect

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            p = bisect.bisect_left(list(reversed(grid[i])), 0)
            ans += p

        return ans
```

**Note**: `bisect_left` on `0`.
