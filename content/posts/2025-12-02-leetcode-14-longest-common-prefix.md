---
title: "LeetCode #14: Longest Common Prefix"
date: 2025-12-02T03:19:16-03:00
tags:
  - coding
rss: false
---

[LeetCode #14: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix):

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return strs[0][:i]

        return strs[0][:min_len]
```
