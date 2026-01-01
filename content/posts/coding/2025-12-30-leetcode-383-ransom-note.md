---
title: "LeetCode #383: Ransom Note"
date: 2025-12-30T05:19:04-03:00
rss: false
categories:
  - coding
---

[LeetCode #383: Ransom Note](https://leetcode.com/problems/leetcode-#383:-ransom-note):

So elegant!

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)
```

A bit more manual:

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)

        for letter in ransomNote:
            if c[letter] <= 0:
                return False
            c[letter] -= 1

        return True
```

No `Counter`?

```python
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = defaultdict(int)
        for letter in magazine:
            c[letter] += 1

        for letter in ransomNote:
            if c[letter] <= 0:
                return False
            c[letter] -= 1

        return True
```

No `defaultdict`?

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = {}
        for letter in magazine:
            if letter in c:
                c[letter] += 1
            else:
                c[letter] = 1

        for letter in ransomNote:
            if c.get(letter, 0) <= 0:
                return False
            c[letter] -= 1

        return True
```

Or with `setdefault`:

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = {}
        for letter in magazine:
            c[letter] = c.setdefault(letter, 0) + 1

        for letter in ransomNote:
            if c.get(letter, 0) <= 0:
                return False
            c[letter] -= 1

        return True
```
