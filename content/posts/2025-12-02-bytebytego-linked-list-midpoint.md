---
title: "ByteByteGo: Linked List Midpoint"
date: 2025-12-02T16:10:08-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Linked List Midpoint](https://bytebytego.com/exercises/coding-patterns/bytebytego:-linked-list-midpoint):

Slow and fast pointers.

```python
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_midpoint(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```
