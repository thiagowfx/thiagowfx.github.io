---
title: "LeetCode #355: Design Twitter"
date: 2026-04-06T00:54:49+02:00
tags:
  - dev
  - leetcode
categories:
  - coding
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
