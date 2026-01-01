
[Yahoo! Pipes](https://en.wikipedia.org/wiki/Yahoo!_Pipes) is not around
anymore, however there is a modern replacement for it: https://www.pipes.digital/.

It was on Hacker News recently: https://news.ycombinator.com/item?id=40841980

Here is a practical use case for it: to filter out unwanted episodes from
podcast RSS feeds.

I follow [Jovem Nerd - Nerdcasts](https://jovemnerd.com.br/podcasts/nerdcast).
They are a Brazilian podcast.

However, in the recent years, they added a lot of other (unrelated) podcasts
from their network to the main NerdCast feed, effectively polluting it. The
cleaner and elegant action to do would have been to publish individual RSS feeds
for each of their podcast series, and perhaps an additional one to contain all
of them, for those who would like to subscribe to everything. But that's not
what they do.

This is an effective marketing strategy for them, because the smaller podcast
series benefit from the exposure in the main feed. At the same time, this is
hostile to listeners, as we end up receiving bundling of episodes we are not
looking for.

Enter the new Pipes.

With it I can build the following pipeline:

- fetch the nerdcast feed: https://api.jovemnerd.com.br/feed-nerdcast/
- filter only the items that contain "NerdCast" in `item.title`
- publish a new feed

The end result ("NerdCast ONLY"):

- Preview: https://www.pipes.digital/feedpreview/VqaEW4qJ
- Raw feed: https://www.pipes.digital/feed/VqaEW4qJ?

You are welcome.

Documentation: https://www.pipes.digital/docs

