---
title: "ByteByteGo: Longest Palindrome in a String"
date: 2025-11-30T22:16:55-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Longest Palindrome in a String](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/longest-palindrome-in-a-string):

```python
def longest_palindrome_in_a_string(s: str) -> str:
    from functools import lru_cache

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
