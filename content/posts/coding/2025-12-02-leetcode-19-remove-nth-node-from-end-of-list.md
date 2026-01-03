---
title: "LeetCode #19: Remove Nth Node From End of List"
date: 2025-12-02T03:50:43-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #19: Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list):

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        pivot = head
        back = head

        for _ in range(n):
            if pivot:
                pivot = pivot.next

        if not pivot:
            head = head.next
            return head

        while pivot.next:
            pivot = pivot.next
            back = back.next

        if back.next:
            back.next = back.next.next

        return head
```
