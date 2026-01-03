---
title: "SAML Chrome Panel"
date: 2025-03-12T00:51:05+01:00
tags:
  - dev
  - security
---

[SAML Chrome Panel](https://chromewebstore.google.com/detail/saml-chrome-panel/paijfdbeoenhembfhkhllainmocckace):

> Extends the (Chrome) Developer Tools, adding support for SAML Requests and
> Responses to be displayed in the Developer Tools window

> This is an Open Source SAML debugger for Chrome. It operates as another panel
> in the Chrome Developer Tools section, which monitors the traffic in the
> current active tab. This panel is trying to replicate what the Firefox version
> of SAML Tracer does as there wasn't a good enough one (or any) for Chrome at
> the time of writing this.

> It is designed to display all network traffic, along with the request and
> response data. If there is a SAML request or response, then it will grab the
> message, format it nicely and show it to you in another tab.

Upstream: https://github.com/milton-lai/saml-chrome-panel

This Chrome extension has proven useful to me at least twice.

Recently I was integrating [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)
and [MongoDB Atlas](https://www.mongodb.com/atlas) with
[Okta](https://www.okta.com/). You can do it via SAML or via OIDC.

There's always a chance of having one tiny configuration mistake, perhaps a
typo or a missing field. I found:

- ArgoCD: a typo in the callback URL (`foo-foo` instead of `foo`)
- MongoDB Atlas: an `acsError` in the response
  ([example](https://www.mongodb.com/community/forums/t/mongodb-atlas-okta-integration-login-error/230897),
  [example](https://www.mongodb.com/community/forums/t/sso-issue-with-idp-azure-entraid-okta-mongodb-saml/278500)):
  https://cloud.mongodb.com/okta/hooks/acsError: it was a certificate error.
  Instead of copying and pasting the certificate content (`------ BEGIN
  CERTIFICATE ------`), upload the file directly. The
  [documentation](https://www.mongodb.com/docs/cloud-manager/security/federated-auth-okta/)
  (item `1.h.`) notes so. Convert it to `.pem` prior to uploading it.
