---
title: "LeetCode #217: Contains Duplicate"
date: 2025-12-25T05:02:36-03:00
tags:
  - coding
rss: false
---

[LeetCode #217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate):

```python
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len([x for x in Counter(nums).values() if x >= 2]) > 0
```

OR:

```python
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(x >= 2 for x in Counter(nums).values())
```
