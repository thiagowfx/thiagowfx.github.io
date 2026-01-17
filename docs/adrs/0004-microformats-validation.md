# ADR-0004: Microformats Validation

## Status

Proposed

## Date

2026-01-01

## Context

The blog implements IndieWeb microformats (h-card, h-entry, h-feed, rel-me) but
lacks documented validation procedures to ensure correctness. Microformats
enable machine-readable author data, post metadata, and social link ownership.

## Decision

Establish validation procedures using these tools:

### Validation URLs

1. **Microformats Parser** (https://pin13.net/mf2/)
   - Test homepage for h-card
   - Test posts for h-entry
   - Test post list for h-feed

2. **IndieWebify.me** (https://indiewebify.me/)
   - h-card validation: `/validate-hcard/`
   - rel-me validation: `/validate-rel-me/`

3. **W3C HTML Validator** (https://validator.w3.org/)
   - Ensure microformat changes don't break HTML validity

### Expected Properties

- **h-card**: name, nickname, url, email, photo
- **h-entry**: name, published, url, content, author
- **h-feed**: name, children (h-entry items)
- **rel-me**: GitHub, Goodreads, LinkedIn, StackOverflow

### Re-validate When

- Changing author config (name, email, nickname)
- Modifying layout templates
- Adding/removing social links
- Before submitting to IndieWeb directories

## Consequences

**Easier:**

- Confidence that microformats work correctly
- Prerequisite for WebMention support
- Eligibility for IndieWeb directories and webring

**Harder:**

- Manual validation steps required after template changes
