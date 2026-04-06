---
title: "sliding window"
url: https://perrotta.dev/2026/03/sliding-window/
last_updated: 2026-03-13
---


Sliding window template:

```python
def sliding_window(nums):
    left = 0
    state = ...          # dict, set, int — track window contents

    for right in range(len(nums)):
        # 1. expand — add nums[right] to state
        state.add(nums[right])

        # 2. shrink — while window is invalid (while, not if!)
        while invalid(state):
            state.remove(nums[left])
            left += 1

        # 3. update answer
        ans = max(ans, right - left + 1)

    return ans
```

