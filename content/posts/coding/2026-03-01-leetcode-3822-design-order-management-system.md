---
title: "LeetCode #3822: Design Order Management System"
date: 2026-03-01T18:21:49+01:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #3822: Design Order Management System](https://leetcode.com/problems/design-order-management-system):

```python
from dataclasses import dataclass

@dataclass
class Entry():
    orderType: OrderType
    price: int

class OrderManagementSystem:

    def __init__(self):
        self.orders = {}

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        assert orderType in ["buy", "sell"], f"invalid orderType: {orderType}"

        self.orders[orderId] = Entry(orderType, price)


    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        assert orderId in self.orders

        orderType = self.orders[orderId].orderType
        self.orders[orderId] = Entry(orderType, newPrice)


    def cancelOrder(self, orderId: int) -> None:
        assert orderId in self.orders

        del self.orders[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return [orderId for (orderId, entry) in self.orders.items() if entry.orderType == orderType and entry.price == price]


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)
```
