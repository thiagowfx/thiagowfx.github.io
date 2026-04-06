---
title: "LeetCode #1876: Substrings of Size Three with Distinct Characters"
url: https://perrotta.dev/2026/01/leetcode-%231876-substrings-of-size-three-with-distinct-characters/
last_updated: 2026-01-06
---


[LeetCode #1876: Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters):

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def good(s):
            return len(s) == 3 and s[0] != s[1] and s[1] != s[2] and s[2] != s[0]

        ans = 0

        for i in range(0, len(s) - 2):
            ans += good(s[i:i + 3])

        return ans
```

