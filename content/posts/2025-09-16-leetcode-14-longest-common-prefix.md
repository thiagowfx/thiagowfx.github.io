---
title: "LeetCode #14: Longest Common Prefix"
date: 2025-09-16T23:51:34+02:00
tags:
  - coding
rss: false
---

[LeetCode #14: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/):

Elegant:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(min(len(s) for s in strs)):
            # ('f', 'f', 'f') -> (True, True, True)
            if all(strs[0][i] == s[i] for s in strs[1:]):
                prefix += strs[0][i]
            else:
                break

        return prefix
```

Both `for s in strs[1:]` and `for s in strs` work, the latter is redundant.

Previously:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        min_length = min([len(str) for str in strs])

        for i in range(min_length):
            c = strs[0][i]
            the_end = False
            for str in strs[1:]:
                if str[i] != c:
                    the_end = True
                    break
            if the_end:
                break
            ans += c

        return ans
```

When you do `min()`, `max()`, `sum()`, etc: there's no need to create an
intermediate list. In other words, this simplification is more concise and
elegant:

```python
min_length = min([len(str) for str in strs]) # ->
min_length = min(len(str) for str in strs) # ->
```

`the_end` is a workaround to break from a nested loop, as there is no `goto` in
Python. And it is [considered
harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) anyway.
Another way is to throw an exception, but that's more cumbersome and error-prone
in the context of a coding interview.
