---
title: "LeetCode #24: Swap Nodes in Pairs"
date: 2025-12-31T03:25:59-03:00
rss: false
categories:
  - coding
---

[LeetCode #24: Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs):

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head
        second = head.next
        third = head.next.next

        first.next = self.swapPairs(third)
        second.next = first

        return second
```
