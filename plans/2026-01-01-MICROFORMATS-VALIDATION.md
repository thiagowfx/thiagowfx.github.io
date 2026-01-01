# Plan: Microformats Validation

## Overview
Document validation procedures for IndieWeb microformats (h-card, h-entry, h-feed, rel-me) to ensure proper implementation on perrotta.dev.

## Validation URLs

### 1. Microformats Parser
**URL:** https://pin13.net/mf2/

**Purpose:** Parse and display microformats found on a page

**Test URLs:**
- Homepage: `https://perrotta.dev` (should show h-card)
- Any post: `https://perrotta.dev/2025/11/no-adblocker-detected/` (should show h-entry)
- Post list: `https://perrotta.dev/posts/` (should show h-feed)

**Expected Results:**

#### h-card (homepage)
```json
{
  "type": ["h-card"],
  "properties": {
    "name": ["Thiago Perrotta"],
    "nickname": ["thiagowfx"],
    "url": ["https://perrotta.dev"],
    "email": ["<configured email>"],
    "photo": ["https://perrotta.dev/thiagowfx.webp"]
  }
}
```

#### h-entry (post)
```json
{
  "type": ["h-entry"],
  "properties": {
    "name": ["No adblocker detected"],
    "published": ["2025-11-23T00:23:26-03:00"],
    "url": ["https://perrotta.dev/2025/11/no-adblocker-detected/"],
    "content": [{
      "html": "<p>...",
      "value": "..."
    }],
    "author": [{
      "type": ["h-card"],
      "properties": {
        "name": ["Thiago Perrotta"],
        "url": ["https://perrotta.dev"]
      }
    }]
  }
}
```

#### h-feed (posts list)
```json
{
  "type": ["h-feed"],
  "properties": {
    "name": ["Posts"]
  },
  "children": [
    {
      "type": ["h-entry"],
      "properties": {
        "name": ["No adblocker detected"],
        "published": ["2025-11-23T00:23:26-03:00"],
        "url": ["https://perrotta.dev/2025/11/no-adblocker-detected/"]
      }
    }
    // ... more entries
  ]
}
```

---

### 2. IndieWebify.me - h-card Validation
**URL:** https://indiewebify.me/validate-hcard/

**Purpose:** Check for valid h-card on homepage

**Test:**
- Enter: `https://perrotta.dev`
- Click "Check"

**Expected Results:**
- ✅ h-card found
- Shows: name, nickname, photo, email, url properties
- No errors or warnings

---

### 3. IndieWebify.me - rel-me Validation
**URL:** https://indiewebify.me/validate-rel-me/?url=https%3A%2F%2Fperrotta.dev%2F

**Purpose:** Verify rel-me links for social media ownership

**Expected Results:**
- ✅ 4 rel-me links detected:
  - GitHub: https://github.com/thiagowfx
  - Goodreads: https://goodreads.com/user/show/7873832-thiago
  - LinkedIn: https://linkedin.com/in/thiagoperrotta
  - StackOverflow: https://stackoverflow.com/users/1745064/thiagowfx
- ✅ All links return 200 status
- ✅ Links point back to perrotta.dev with rel="me"

**How to verify ownership:**
1. Visit each social profile (GitHub, Goodreads, LinkedIn, StackOverflow)
2. Ensure your profile links to `https://perrotta.dev`
3. Use IndieWebify.me to verify bidirectional rel-me relationship

---

### 4. W3C HTML Validator
**URL:** https://validator.w3.org/

**Purpose:** Ensure microformat changes don't break HTML validity

**Test:**
- Enter: `https://perrotta.dev`
- Enter: Any post URL

**Expected Results:**
- No new errors introduced by microformat changes
- Valid HTML5 markup
- Proper nesting of h-card, h-entry, h-feed elements

---

## Manual Validation Checklist

### Homepage (h-card)
- [ ] Hidden h-card present in `<body>`
- [ ] Contains p-name (author full name)
- [ ] Contains p-nickname (thiagowfx)
- [ ] Contains u-url (site URL)
- [ ] Contains u-email (email address)
- [ ] Contains u-photo (profile image)
- [ ] All values are dynamic (from config, not hardcoded)

### Single Post (h-entry)
- [ ] Wrapped in `<article class="h-entry">`
- [ ] Title has `class="p-name"`
- [ ] Date/time has `class="dt-published"`
- [ ] Datetime format: `YYYY-MM-DDTHH:mm:ss-07:00` (timezone-aware)
- [ ] Content wrapped in `<div class="e-content">`
- [ ] Hidden `u-url` link with permalink
- [ ] Hidden `u-author h-card` link pointing to homepage
- [ ] All author values are dynamic

### Post List (h-feed)
- [ ] Content wrapped in `<div class="h-feed">`
- [ ] Feed title has `class="p-name"`
- [ ] Main content wrapped in `<div class="e-content">`
- [ ] Each list item has `class="h-entry"`
- [ ] Each post link has `class="u-url"`
- [ ] Each post title wrapped in `<span class="p-name">`
- [ ] Each date has `class="dt-published"`

### Social Links (rel-me)
- [ ] GitHub link has `rel="me noopener"`
- [ ] Goodreads link has `rel="me noopener"`
- [ ] LinkedIn link has `rel="me noopener"`
- [ ] StackOverflow link has `rel="me noopener"`
- [ ] Email link has `rel="noopener"` (no "me")
- [ ] RSS link has `rel="noopener"` (no "me")

---

## Common Issues and Solutions

### Issue: Microformats parser finds nothing
**Solution:**
- Check that h-card is in `<body>`, not `<head>`
- Verify class names are correct: h-card, h-entry, h-feed
- Ensure no JavaScript interference (should be static HTML)

### Issue: rel-me validation fails
**Solution:**
- Verify social profiles link back to perrotta.dev
- Check that rel="me" is present on social links
- Ensure rel="me" only on external links (not internal)
- Wait a few minutes if changes were just deployed

### Issue: Datetime format incorrect
**Solution:**
- Use Hugo's `2006-01-02T15:04:05-07:00` format string
- Verify timezone offset is preserved (not UTC)
- Check that pubdate attribute is present

### Issue: Author information missing in posts
**Solution:**
- Ensure u-author h-card link points to homepage
- Verify homepage has valid h-card
- Check that u-author link is inside h-entry

---

## Next Steps After Validation

If all validations pass:

1. **Enable WebMentions** (existing plan: `2026-01-01-webmention-support.md`)
   - Add webmention endpoint to `<head>`
   - Implement webmention display
   - Set up Brid.gy for social media mentions

2. **Add MicroPub** (optional)
   - Allow posting from IndieWeb clients
   - Implement Micropub endpoint
   - Test with clients like Quill

3. **Register with IndieWeb Directory**
   - Submit site to https://indieweb.org/webring
   - Add to https://indiebloggers.org
   - Join https://xn--sr8hvo.ws (indieweb.org social)

---

## Maintenance

### When to re-validate:
- After changing author config (name, email, nickname)
- After modifying layout templates
- After adding/removing social links
- After Hugo updates that might affect datetime formatting
- Before submitting to IndieWeb directories

### Monitoring:
- Periodically check https://indiewebify.me/validate-rel-me/?url=https%3A%2F%2Fperrotta.dev%2F
- Watch for broken social links (404 errors)
- Ensure new posts have proper h-entry structure

---

## Resources

- **IndieWeb Microformats:** https://microformats.org/wiki/IndieWeb
- **h-card specification:** https://microformats.org/wiki/h-card
- **h-entry specification:** https://microformats.org/wiki/h-entry
- **h-feed specification:** https://microformats.org/wiki/h-feed
- **rel-me spec:** https://microformats.org/wiki/rel-me
- **IndieWebify:** https://indiewebify.me/
- **WebMention.io:** https://webmention.io/
