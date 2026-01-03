---
title: "LeetCode #5: Longest Palindromic String"
date: 2025-12-02T01:28:06-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #5: Longest Palindromic String](https://leetcode.com/problems/longest-palindromic-string):

Top-down DP, memory limit exceeded:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        @lru_cache(maxsize=None)
        def is_palindrome(i, j):
            assert i >= 0
            assert j < len(s)

            if i >= j:  # out of bounds
                return True

            if s[i] != s[j]:
                return False

            return is_palindrome(i + 1, j - 1)

        if len(s) > 0:
            ans = s[0]

        for i in range(len(s)):
            for j in range(i + 1, len(s)):  # both inclusive
                if is_palindrome(i, j):
                    curr_len = j - i + 1
                    if curr_len > len(ans):
                        ans = s[i:j + 1]

        return ans
```

Bottom-up DP, space efficient:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # size 1
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        # size 2
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i-1][i] = True
                ans = s[i - 1 : i + 1]

        # size >= 3 : size = diff + 1
        for diff in range(2, n):
            for i in range(diff, n):
                # compare i vs (i - diff)
                j = i - diff
                if s[i] == s[j] and dp[j + 1][i - 1]:
                    dp[j][i] = True
                    ans = s[j: j + diff +  1]

        return ans
```
