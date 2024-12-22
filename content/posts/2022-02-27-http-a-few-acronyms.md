---
title: "HTTP: a few acronyms"
date: 2022-02-27T21:48:03-05:00
tags:
  - dev
---

I keep forgetting these, so I wrote a small summary for my own reference.


## HSTS

[Wikipedia — HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security):

> HTTP Strict Transport Security (HSTS) is a policy mechanism that helps to
> protect websites against man-in-the-middle attacks such as protocol downgrade
> attacks and cookie hijacking. It allows web servers to declare that web
> browsers (or other complying user agents) should automatically interact with
> it using only HTTPS connections.

In layman's terms: _Force HTTPS on a given domain_.

[HSTS Preload List](https://hstspreload.org/):

> This form is used to submit domains for inclusion in Chrome's HTTP Strict
> Transport Security (HSTS) preload list. This is a list of sites that are
> hardcoded into Chrome as being HTTPS only.
>
> Most major browsers (Chrome, Firefox, Opera, Safari, IE 11 and Edge) also
> have HSTS preload lists based on the Chrome list. (See the HSTS compatibility
> matrix.)

If you add your website to that list, major browsers will honor it and only use
HTTPS for your domain.

Some [TLDs](https://en.wikipedia.org/wiki/Top-level_domain) enforce HTTPS
through HSTS, some popular ones are `.app` and `.dev`.
[Here](https://serverfault.com/q/1067229/180092) is a more comprehensive list.

`HSTS` is fire-and-forget, you'll usually only need to worry about it once,
when configuring a SSL certificate (HTTPS) for your domain or subdomains.


## CSP

[Wikipedia — CSP](https://en.wikipedia.org/wiki/Content_Security_Policy):

> Content Security Policy (CSP) is a computer security standard introduced to
> prevent cross-site scripting (XSS), clickjacking and other code injection
> attacks resulting from execution of malicious content in the trusted web page
> context.

[MDN — CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP):

> Content Security Policy (CSP) is an added layer of security that helps to
> detect and mitigate certain types of attacks, including Cross-Site Scripting
> (XSS) and data injection attacks. These attacks are used for everything from
> data theft, to site defacement, to malware distribution.

CSP can be configured in at least two distinct ways:

1. Web server: return the `Content-Security-Policy` HTTP header:

```
Content-Security-Policy: default-src 'self'; img-src https://*; child-src 'none';
```

2. HTML `<meta>` tag:

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';">
```

`CSP` is something to worry about at the application level. For example,
[miniflux](https://github.com/miniflux/v2/issues/748) to fetch resources
(fonts) from another domain (Google Fonts).


## CORS

[Wikipedia — CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing):

> Cross-origin resource sharing (CORS) is a mechanism that allows restricted
> resources on a web page to be requested from another domain outside the
> domain from which the first resource was served.

CORS can be configured via web server: return the `Access-Control-Allow-Origin` HTTP header:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Origin: http://example.com:8080
```

`CORS` is something to worry about at the application level. For example,
https://keep.google.com/ ⟷ https://google.com/ cookies.


## CSRF

[Wikipedia — CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery):

> Cross-site request forgery, also known as one-click attack or session riding
> and abbreviated as CSRF (sometimes pronounced sea-surf) or XSRF, is a type of
> malicious exploit of a website where unauthorized commands are submitted from
> a user that the web application trusts.

`CSRF` is something to be aware of and to watch out for.
[OWASP](https://owasp.org/www-community/attacks/csrf) has some additional
resources on it.
