---
title: "LeetCode #3662: Filter Characters by Frequency"
url: https://perrotta.dev/2026/01/leetcode-%233662-filter-characters-by-frequency/
last_updated: 2026-01-06
---


[LeetCode #3662: Filter Characters by Frequency](https://leetcode.com/problems/filter-characters-by-frequency):

```python
from collections import Counter

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        ans = []

        counter = Counter(s)

        for c in s:
            if counter[c] < k:
                ans.append(c)

        return ''.join(ans)
```

