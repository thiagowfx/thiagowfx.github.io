---
title: "Tracking packages automatically in a single place"
date: 2022-04-23T18:03:52-04:00
tags:
  - dev
---

I was looking for a way to **track packages and parcels** (mail) for the most popular post and courier services e.g. DHL, UPS, Fedex, Canada Post, USPS, Correios, etc.


There were only two requirements:

1. _one place to rule them all_: whether an app, chatbot, self-hosted software, or website, all services should be available from a single UI endpoint, for **ease of management**
2. automatic / periodic updates: whether by polling, subscription or webhook, the service should autonomously retrieve parcel statuses; accessing each individual provider website should be a no-go

Ultimately I found two solutions that pleased me, both of which free:

1. [Shopify's Shop app](https://shop.app): **Pro**: Great and [KISS](https://en.wikipedia.org/wiki/KISS_principle) design, **Con**: Tracking; Fortune 500 company gathering analytics and data from my purchases. Although I do have a great amount of respect for Shopify generally, the less amount of tracking by Big Tech the better.

2. [Telegram's @Trackbot](https://trackbot.eu/en):

> TrackBot is a Telegram bot for tracking all your shipments. Free, forever. Automatic courier recognition. TrackBot automatically detects the courier of the shipment by using machine learning techniques, with an accuracy higher than 97%.

After using both of them for a while, **my preferred solution nowadays is the Telegram bot**. Its basic operations are (i) List all shipments and (ii) Add a new shipment. It is smart enough to detect the carrier by itself in most cases from the tracking code alone, however whenever it doesn't one can simply specify it manually. Whenever new updates to your existing shipments are detected, it sends you a message (notification) on Telegram.
