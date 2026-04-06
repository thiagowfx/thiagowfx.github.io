---
title: "LeetCode #1636: Sort Array by Increasing Frequency"
url: https://perrotta.dev/2026/01/leetcode-%231636-sort-array-by-increasing-frequency/
last_updated: 2026-01-06
---


[LeetCode #1636: Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency):

```python
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []

        counter = Counter(nums)

        ## 3 3 4 4 2 1 -> 4 4 3 3 2 1

        chunk = []
        prev_count = None

        ## [3, 3]

        for (num, count) in counter.most_common()[::-1]:
            if count != prev_count:
                prev_count = count
                ans.extend(list(sorted(chunk, reverse=True)))
                chunk = []

            chunk.extend([num] * count)

        if chunk:
            ans.extend(list(sorted(chunk, reverse=True)))

        return ans
```

