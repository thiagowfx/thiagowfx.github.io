---
title: "LeetCode #451: Sort Characters By Frequency"
url: https://perrotta.dev/2026/01/leetcode-%23451-sort-characters-by-frequency/
last_updated: 2026-01-06
---


[LeetCode #451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency):

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c * v for (c, v) in Counter(s).most_common()])
```

