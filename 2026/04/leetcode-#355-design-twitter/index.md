---
title: "LeetCode #355: Design Twitter"
url: https://perrotta.dev/2026/04/leetcode-%23355-design-twitter/
last_updated: 2026-04-06
---


[LeetCode #355: Design Twitter](https://leetcode.com/problems/design-twitter):

My original solution:

```python
from collections import defaultdict
from itertools import chain

class Twitter:

    def __init__(self):
        # [userId] -> {userId, ...}
        self.f = defaultdict(set)

        self.tweets = defaultdict(list)

        self.ts = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.ts, tweetId))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_with_ts = []

        ## for followee in list(self.f[userId]) + [userId]:
        for followee in chain(self.f[userId], [userId]):
            tweets_with_ts.extend(self.tweets[followee][::-1])

        # [(1, 3), (0, 5)]
        tweets_with_ts.sort(reverse=True)

        tweets = [id for (_, id) in tweets_with_ts]

        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

With `deque` (slow):

```python
from collections import defaultdict, deque
from itertools import chain

class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for (user, tweetId) in self.tweets if user == userId or user in self.f[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

With heap:

```python
from collections import defaultdict, deque
from itertools import chain
import heapq

class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        self.tweets = defaultdict(list)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.ts, tweetId))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heap = []

        for followee in chain(self.f[userId], [userId]):
            heap.extend(self.tweets[followee])

        heapq.heapify(heap)

        for _ in range(min(10, len(heap))):
            tweets.append(heapq.heappop(heap)[1])

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

