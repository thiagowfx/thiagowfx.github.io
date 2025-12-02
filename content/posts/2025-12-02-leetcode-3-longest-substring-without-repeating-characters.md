---
title: "LeetCode #3: Longest Substring Without Repeating Characters"
date: 2025-12-02T01:13:12-03:00
tags:
  - coding
rss: false
---

[LeetCode #3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters):

A `set` is enough but we could also employ a `Counter` or a `dict`.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = set()
        left = right = 0

        ans = 0

        while right < len(s):
            while s[right] in v:
                v.remove(s[left])
                left += 1
            v.add(s[right])

            ans = max(ans, right - left + 1)
            right += 1

        return ans
```
