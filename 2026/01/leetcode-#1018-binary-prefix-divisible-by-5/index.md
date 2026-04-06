---
title: "LeetCode #1018: Binary Prefix Divisible By 5"
url: https://perrotta.dev/2026/01/leetcode-%231018-binary-prefix-divisible-by-5/
last_updated: 2026-01-06
---


[LeetCode #1018: Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5):

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []

        n = 0

        for i, num in enumerate(nums):
            n = n * 2 + num
            ans.append(n % 5 == 0)

        return ans
```

