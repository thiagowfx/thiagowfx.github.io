---
title: "LeetCode #501: Find Mode in Binary Search Tree"
date: 2025-12-31T18:24:32-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #501: Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree):

Recursive DFS with a Counter:

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

Iterative DFS:

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

            stack = [node]

            while stack:
                node = stack.pop()
                counter[node.val] += 1

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        dfs(root)

        max_mode = max(counter.values())
        return [k for (k, v) in counter.items() if v == max_mode]
```

BFS:

```python
from collections import Counter, deque

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

            queue = deque([node])

            while queue:
                node = queue.popleft()
                counter[node.val] += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        dfs(root)

        max_mode = max(counter.values())
        return [k for (k, v) in counter.items() if v == max_mode]
```
