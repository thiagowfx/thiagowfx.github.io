---
title: "LeetCode #11: Container With Most Water"
date: 2025-12-02T03:13:17-03:00
tags:
  - coding
rss: false
---

[LeetCode #11: Container With Most Water](https://leetcode.com/problems/container-with-most-water):

Two pointers inwards:

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
```
