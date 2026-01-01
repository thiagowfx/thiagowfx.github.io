---
title: "LeetCode #203: Remove Linked List Elements"
date: 2025-12-31T01:31:29-03:00
rss: false
categories:
  - coding
---

[LeetCode #203: Remove Linked List Elements](https://leetcode.com/problems/leetcode-#203:-remove-linked-list-elements):

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        pointer = head
        while pointer and pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return head
```
