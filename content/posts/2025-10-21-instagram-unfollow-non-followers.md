---
title: "Instagram: unfollow non-followers"
date: 2025-10-21T00:13:11+02:00
tags:
  - dev
  - meta
  - privacy
  - serenity
  - socialmedia
---

Sometimes connections simply fade away. Life happens. Privacy prevails. Then why
don't people remove them both ways (follower + following)? If you don't want to
stay connected with someone any longer, it is good courtesy to do so
symmetrically. If you just unfollow someone, without removing them from your
follower list, then you tacitly demonstrate that you care to a great extent
about invisible internet karma points /shrug.

Instagram doesn't make it easy to find those who do not follow you back.
However, it is possible to obtain this information with a little bit of
scripting.

- Go to [Go to Instagram → Settings → Privacy and security → Download your
information](https://www.instagram.com/download/request/).
- Choose JSON (not HTML).
- Select "Connections" only and, for the period, choose from the beginning of time[^1].
- Confirm the prompt.
- Instagram will email you a ZIP file. That should take a couple of minutes.
- Download the ZIP (`instagram-{username}-YYYY-MM-DD-{id}.zip`) and unpack it.
  Structure:

```shell
% tree connections
connections
└── followers_and_following
    ├── blocked_profiles.json
    ├── close_friends.json
    ├── follow_requests_you've_received.json
    ├── followers_1.json
    ├── following.json
    ├── hide_story_from.json
    ├── pending_follow_requests.json
    ├── profiles_you've_favorited.json
    ├── recent_follow_requests.json
    ├── recently_unfollowed_profiles.json
    └── removed_suggestions.json
```

(Yes, one of these files has a `'` in the name. It was not a typo.)

We're interested in `followers_N.json` and `following.json`.

From this point on, vibe code and chill. A single, well-crafted prompted is
enough. For example:

```
You are a world-class software developer.

I exported all my Instagram data.

Write a python script to parse all people I follow that do not follow me back.

Output username + profile URLs in each line.
```

I am a fan of this one-shot prompt structure / style[^2]:

- you are a superb ${FOO}
- this is some context for you
- do this for me
- output in the desired format

The resulting script:

```python
#!/usr/bin/env python3

import json
import csv
from pathlib import Path

# Base path where your JSON files are
base = Path("connections/followers_and_following")

def extract_usernames(file_path):
    """Extract Instagram usernames from a followers/following JSON file."""
    with open(file_path) as f:
        data = json.load(f)

    # Handle both old and new formats
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list):
                data = v
                break

    if not isinstance(data, list):
        raise ValueError(f"Unexpected format in {file_path}")

    usernames = set()
    for item in data:
        try:
            entry = item.get("string_list_data", [])[0]
            username = (
                entry.get("value")
                or entry.get("href", "").rstrip("/").split("/")[-1]
                or entry.get("username")
            )
            if username:
                usernames.add(username)
        except Exception:
            continue

    return usernames


# --- Load followers (handles multiple files) ---
followers = set()
for path in base.glob("followers_*.json"):
    followers |= extract_usernames(path)

# --- Load following ---
following = extract_usernames(base / "following.json")

# --- Compute differences ---
not_following_back = sorted(following - followers)
you_dont_follow_back = sorted(followers - following)
mutuals = sorted(followers & following)

def write_csv(filename, users):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "profile_url"])
        for user in users:
            writer.writerow([user, f"https://www.instagram.com/{user}/"])
    print(f"✅ Saved {len(users)} entries to {filename}")

# --- Write results ---
write_csv("not_following_back.csv", not_following_back)
write_csv("you_dont_follow_back.csv", you_dont_follow_back)
write_csv("mutuals.csv", mutuals)
```

The script was tested in a real account, and I'm pleased to state that it works
as intended.

If you use it for the sake of unfollowing people[^3] then it's advisable not to
automate the unfollowing process, as Instagram could potentially block you.
Instead, do it manually.

May the reduced noise increase your serenity.

[^1]: Or else it won't work.
[^2]: I am not here to claim what prompt is the best. Just keep it simple and
    carry on.
[^3]: Why would you run it otherwise?
