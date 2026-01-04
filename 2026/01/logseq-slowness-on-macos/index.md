
Last week LogSeq was super slow on my Mac, it was pretty much unusable. I had to
manually kill its process multiple times as it kept freezing.

Eventually I figured out [the issue](https://discuss.logseq.com/t/my-logseq-become-too-slow-recently/31985/4):

> Then iCloud is the cause for the slowness. This is a known issue and is the
> reason why the developers have built Logseq Sync. Other options for syncing
> that don't impact performance are Git and SyncThing.

I would like to keep using iCloud at this time as it's (i) free and (ii)
convenient to access from iOS.

The following mitigation seemed to work:

- Locate the LogSeq directory in iCloud (`~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents`)
- Right click the directory in Finder
- Click ['Keep Downloaded'](https://discussions.apple.com/thread/256113094?sortBy=rank)

> Keep Downloaded means the file stays on the device, and even if space is
> needed the file will not be removed [...]

