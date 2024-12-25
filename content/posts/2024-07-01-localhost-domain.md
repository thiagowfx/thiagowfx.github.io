---
title: "Localhost domain"
date: 2024-07-01T11:34:34+02:00
tags:
  - dev
  - linux
---

If you find yourself in a situation wherein http://localhost:1313 has issues,
you can use a domain that redirects to localhost. For example:

- http://localdev.me:1313/
- http://demo.localdev.me:1313/


> When I'm doing local development, I sometimes need a domain name that routes
> back to localhost. I've long run into cases where I need subdomains and ended
> up modifying my local hosts file. I've used this for a variety of situations
> going back for a long time. From Kubernetes ingress work to web development.

> `localdev.me` DNS is served through amazon. The domain name and any subdomains
> point to `127.0.0.1`.

> The next time you need a custom domain or subdomain for local development,
> instead of hancking your hosts file you might consider localdev.me.

Source: https://codeengineered.com/blog/2022/localdev-me/
