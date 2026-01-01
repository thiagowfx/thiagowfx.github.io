---
title: "LeetCode #217: Contains Duplicate"
date: 2025-12-25T05:02:36-03:00
categories:
  - coding
---

[LeetCode #217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate):

With `Counter()`:

```python
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len([x for x in Counter(nums).values() if x >= 2]) > 0
```

OR a small variant with `any`:

```python
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(x >= 2 for x in Counter(nums).values())
```

OR with `set()`:

```python
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
```
