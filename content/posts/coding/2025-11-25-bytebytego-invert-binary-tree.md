---
title: "ByteByteGo: Invert Binary Tree"
date: 2025-11-25T00:36:17-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Invert Binary Tree](https://bytebytego.com/exercises/coding-patterns/trees/invert-binary-tree):

```python
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def invert_binary_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
```

The following **DOES NOT** work:

```python
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def invert_binary_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.left = invert_binary_tree(root.right)
    root.right = invert_binary_tree(root.left)

    return root
```

The swap must happen simultaneously. The following works:

```python
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def invert_binary_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)

    return root
```
