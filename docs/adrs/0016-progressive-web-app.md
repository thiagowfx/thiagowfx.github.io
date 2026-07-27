# ADR-0016: Progressive Web App

## Status

Abandoned

## Date

2026-07-27

## Context

The `pwa` branch explored making perrotta.dev installable and partially available
offline. The experiment added:

- A web app manifest and 192 px/512 px icons
- A service worker registered by the base layout
- Pre-caching for the homepage and an offline fallback page
- Network-first caching for successfully visited pages
- Cache-isolation and service-worker regression tests

The implementation did not download the full blog for offline reading. Only the
homepage, fallback page, and pages visited while online would be available without
a network connection.

## Decision

Do not adopt the Progressive Web App experiment.

For a static blog, home-screen installation, a branded offline fallback, and
offline revisits of previously viewed pages provide little practical value. Full
offline reading would require downloading and updating the entire post archive,
which would add more storage, synchronization, versioning, and invalidation
complexity.

The service worker also introduces persistent browser state and cache behavior
that must be tested and maintained across deployments. That cost outweighs the
limited benefit for this site.

## Consequences

- `master` remains a conventional website without a web app manifest or service
  worker.
- Readers need a network connection unless their browser's normal HTTP cache
  happens to satisfy a request.
- No service-worker cache lifecycle or offline-content synchronization needs to be
  maintained.
- The implementation remains unmerged, and the `pwa` branch may be deleted.
- Reconsider only if offline access or installability becomes an explicit user
  requirement.
