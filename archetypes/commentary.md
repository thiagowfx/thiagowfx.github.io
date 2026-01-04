---
title: "Reply to: {{ replace .Name (now.Format "2006-01-02") "" | humanize }}"
date: {{ .Date }}
categories:
  - commentary
tags: []
external_link: "{{ getenv "HUGO_EXTERNAL_LINK" }}"
---
