---
title: "LeetCode #136: Single Number"
url: https://perrotta.dev/2026/01/leetcode-%23136-single-number/
last_updated: 2026-01-06
---


[LeetCode #136: Single Number](https://leetcode.com/problems/single-number):

XOR everything:

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
```

Or with `reduce`:

```python
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
```

