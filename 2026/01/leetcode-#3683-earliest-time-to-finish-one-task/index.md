
[LeetCode #3683: Earliest Time to Finish One Task](https://leetcode.com/problems/earliest-time-to-finish-one-task):

```python
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([s + t for [s, t] in tasks])
```

