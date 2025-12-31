---
title: "LeetCode #501: Find Mode in Binary Search Tree"
date: 2025-12-31T18:24:32-03:00
tags:
  - coding
rss: false
---

[LeetCode #501: Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree):

```python
from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        
        def dfs(node):
            if not node:
                return

            counter[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_mode = max(counter.values())
        return [k for (k, v) in counter.items() if v == max_mode]
```
