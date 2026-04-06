---
title: "LeetCode #274: H-Index"
url: https://perrotta.dev/2025/12/leetcode-%23274-h-index/
last_updated: 2026-01-03
---


[LeetCode #274: H-Index](https://leetcode.com/problems/h-index):

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h = 0

        while h < len(citations):
            if h < citations[h]:
                h += 1
            else:
                break

        return h
```

