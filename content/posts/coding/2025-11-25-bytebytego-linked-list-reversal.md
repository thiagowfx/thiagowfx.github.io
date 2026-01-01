---
title: "ByteByteGo: Linked List Reversal"
date: 2025-11-25T21:18:56-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Linked List Reversal](https://bytebytego.com/exercises/coding-patterns/linked-lists/linked-list-reversal):

## Recursive

```python
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    new_head = linked_list_reversal(head.next)

    head.next.next = head
    head.next = None

    return new_head
```

## Iterative

```python
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    prev = None

    while head is not None:
        next_node = head.next

        head.next = prev

        prev = head
        head = next_node

    return prev
```
