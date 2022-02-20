---
{{- $today := now.Format "2006-01-02"}}
title: "{{ replace .Name $today "" | humanize }}"
date: {{ .Date }}
tags:
draft: true
showtoc: true
---

<!--more-->
