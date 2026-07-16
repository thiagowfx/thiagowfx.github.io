---
title: "safari: (permanently) allow pop-ups for a domain"
url: https://perrotta.dev/2026/07/safari-permanently-allow-pop-ups-for-a-domain/
last_updated: 2026-07-16
---


**Problem statement**: a site / domain needs pop-ups for OAuth / logins, but I
don't want to disable Safari's pop-up blocker globally just to appease a couple
of domains.

Safari lets one scope the exception on a per-site basis. The domain has to be
open in a tab first, so that its entry shows up in the list:

- Open the site in a new tab.
- Click **Safari → Settings → Websites → Pop-up Windows** (left sidebar).
- Find the domain under "Currently Open Websites" and set it to **Allow**.

The blocker stays on everywhere else, as it should be.

The default at the bottom ("When visiting other websites") is the global toggle;
leave it on **Block and Notify** so only the sites I've whitelisted get through.

That per-site list is the same panel that governs camera, microphone,
location, and auto-play permissions.

