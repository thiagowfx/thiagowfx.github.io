---
title: "LeetCode #93: Restore IP Addresses"
date: 2025-12-24T03:50:57-03:00
categories:
  - coding
---

[LeetCode #93: Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses):

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(s: str, t: List[str]):
            if not s:
                if t and len(t) == 4:
                    ans.append('.'.join(t))
                    return
                else:
                    return

            if len(t) >= 4:
                return

            def is_valid(chunk):
                return chunk and (chunk == "0" or (not chunk.startswith('0') and 0 <= int(chunk) <= 255))

            for i in [1, 2, 3]:
                if i > len(s):
                    break
                chunk = s[:i]
                if is_valid(chunk):
                    backtrack(s[i:], t + [s[:i]])

        backtrack(s, [])

        return ans
```
