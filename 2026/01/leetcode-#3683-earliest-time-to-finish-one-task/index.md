---
title: "LeetCode #3683: Earliest Time to Finish One Task"
url: https://perrotta.dev/2026/01/leetcode-%233683-earliest-time-to-finish-one-task/
last_updated: 2026-01-06
---


[LeetCode #3683: Earliest Time to Finish One Task](https://leetcode.com/problems/earliest-time-to-finish-one-task):

```python
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([s + t for [s, t] in tasks])
```

