---
title: "LeetCode #442: Find All Duplicates in an Array"
url: https://perrotta.dev/2026/01/leetcode-%23442-find-all-duplicates-in-an-array/
last_updated: 2026-01-06
---


[LeetCode #442: Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array):

Easy with Counter:

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for (num, count) in Counter(nums).most_common() if count == 2]
```

