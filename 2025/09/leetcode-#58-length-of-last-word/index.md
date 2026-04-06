---
title: "LeetCode #58: Length of Last Word"
url: https://perrotta.dev/2025/09/leetcode-%2358-length-of-last-word/
last_updated: 2026-01-03
---


[LeetCode #58: Length of Last Word](https://leetcode.com/problems/length-of-last-word/):

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```

`.split()` acts on whitespace by default. It is equivalent to `.split(' ')`.

Previously:

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
```

It turns out `.strip()` is not really necessary.

