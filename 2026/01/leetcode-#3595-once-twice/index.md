---
title: "LeetCode #3595: Once Twice"
url: https://perrotta.dev/2026/01/leetcode-%233595-once-twice/
last_updated: 2026-01-06
---


[LeetCode #3595: Once Twice](https://leetcode.com/problems/once-twice):

Counter:

```python
from collections import Counter

class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        return [num for (num, _) in Counter(nums).most_common()[::-1][:2]]
```

