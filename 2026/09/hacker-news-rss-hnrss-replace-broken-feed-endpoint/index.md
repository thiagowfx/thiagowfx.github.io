---
title: "Hacker News RSS (hnrss): replace broken feed endpoint"
url: https://perrotta.dev/2026/09/hacker-news-rss-hnrss-replace-broken-feed-endpoint/
last_updated: 2026-09-02
---


[Previously]({{< ref "2022-02-17-praise-for-blog-aggregators" >}}).

**Problem statement**: my filtered Hacker News feed stopped working in
Miniflux because its HNRSS endpoint returned a bad gateway response.

This has been happening for a couple of weeks, to the point it became
unreliable.

The feed selected stories with more than 650 points:

```text
https://hnrss.org/newest?points=650
```

Miniflux reported the upstream failure without hiding it:

```text
The website is not available at the moment due to a bad gateway error.
The problem is not on Miniflux side. Please, try again later.
```

HNRSS is open source, and another public instance runs a
[fork](https://github.com/kakwa/hnrss-ai-filtering) against the same Hacker News
Algolia data. So I replaced the domain:

```diff
-https://hnrss.org/newest?points=650
+https://hnrss.kakwalab.ovh/newest?points=650
```

The replacement returned an XML feed with 20 items:

```shell
% curl -L --max-time 15 -sS \
    'https://hnrss.kakwalab.ovh/newest?points=650' \
    -o /tmp/hnrss.xml \
    -w '%{http_code} %{content_type} %{size_download} bytes\n'
200 application/xml; charset=utf-8 15929 bytes

% python3 -c 'import xml.etree.ElementTree as ET; \
r=ET.parse("/tmp/hnrss.xml").getroot(); \
i=r.findall("./channel/item"); print(len(i)); print(i[0].findtext("title"))'
20
Hang on to Your Firefox
```

