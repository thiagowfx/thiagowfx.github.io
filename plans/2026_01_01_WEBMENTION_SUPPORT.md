# WebMention Support Implementation Plan

## Current State Assessment

Your blog currently:
- Uses Hugo with a custom fork of bearblog theme
- Has IndieWeb badge but no WebMention implementation
- Uses static generation with no server-side processing
- Has good structure with partials and custom layouts
- Uses IndieWeb principles (personal domain, badges, etc.)

## Implementation Approach: Client-Side with webmention.io

**Rationale:** Chosen over GitHub Actions approach because:
- Minimal complexity (~30 min setup vs 2-3 hours)
- No additional infrastructure/workflows needed
- Fits your "simple is better" philosophy (512kb club member)
- Can migrate to server-side later if needed
- webmention.js is well-maintained and privacy-respecting

## Detailed Implementation Steps

### 1. Sign up for webmention.io
- Create account at https://webmention.io/
- Verify ownership of `perrotta.dev`
- Note your webmention endpoint URL

### 2. Add WebMention endpoint to HTML head
**File:** `layouts/_default/baseof.html` (after line 29)

Add:
```html
<link rel="webmention" href="https://webmention.io/perrotta.dev/webmention" />
```

### 3. Download and add webmentions.js
**Action:** Download latest version from https://github.com/PlaidWeb/webmention.js
**Location:** `static/js/webmention.min.js`

### 4. Include webmentions.js in head
**File:** `layouts/_default/baseof.html` (after line 31)

Add:
```html
<script src="{{ "js/webmention.min.js" | absURL }}" async></script>
```

### 5. Add WebMention display container to single posts
**File:** `layouts/_default/single.html` (after line 113, before the end)

Add:
```html
<section class="webmentions-section">
  <div id="webmentions"></div>
</section>
```

### 6. Add CSS styling for WebMentions
**File:** `layouts/partials/style.html` (append at end)

Add:
```css
.webmentions-section {
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px dashed var(--border-color);
}

#webmentions {
  margin-top: 1rem;
}

#webmentions .webmention {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background-color: var(--code-bg);
  border-radius: 8px;
  border-left: 3px solid var(--link-color);
}

#webmentions .webmention-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

#webmentions .webmention-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

#webmentions .webmention-name {
  font-weight: 600;
  text-decoration: none;
  color: var(--link-color);
}

#webmentions .webmention-name:hover {
  text-decoration: underline;
}

#webmentions .webmention-content {
  font-size: 0.95em;
  line-height: 1.5;
  color: var(--text-color);
}

#webmentions .webmention-source {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.85em;
  color: var(--color-gray);
}

#webmentions .webmention-source a {
  color: var(--color-gray);
}

#webmentions .webmention-source a:hover {
  color: var(--link-color);
}

#webmentions .webmention-date {
  font-style: italic;
}

#webmentions .webmention-type {
  display: inline-block;
  padding: 2px 8px;
  margin-right: 0.5rem;
  border-radius: 4px;
  font-size: 0.75em;
  font-weight: 600;
  text-transform: uppercase;
}

#webmentions .webmention-type-reply {
  background-color: #e3f2fd;
  color: #1565c0;
}

#webmentions .webmention-type-like {
  background-color: #fce4ec;
  color: #c2185b;
}

#webmentions .webmention-type-repost {
  background-color: #e8f5e9;
  color: #2e7d32;
}

@media (max-width: 600px) {
  #webmentions .webmention {
    padding: 0.75rem;
  }

  #webmentions .webmention-avatar {
    width: 40px;
    height: 40px;
  }
}
```

### 7. Configure webmention.js behavior
**File:** Add to baseof.html script section (after line 449)

Add initialization:
```javascript
window.webmentionJS = {
  wordcount: true,
  showAvatars: true,
  showRelativeTime: true
};
```

### 8. Add h-entry microformats (optional but recommended)
**File:** `layouts/_default/single.html` (wrap content in h-entry)

Modify the `<content>` section to add microformats:
```html
<div class="h-entry">
  <h2 class="p-name">{{ .Title }}</h2>
  <time class="dt-published" datetime='{{ .Date.Format "2006-01-02T15:04:05Z07:00" }}'>{{ .Date.Format (default "02 Jan, 2006" .Site.Params.dateFormat) }}</time>
  <content class="e-content"> {{ .Content }} </content>
</div>
```

### 9. Test implementation
- Run `just watch false` to test locally
- Visit a blog post and inspect head for webmention link
- Check browser console for webmention.js loading
- Test with webmention.rocks test suite
- Send a test webmention to verify endpoint works

### 10. Set up Brid.gy for social media mentions
- Visit https://brid.gy/
- Connect your Mastodon/Twitter accounts
- Configure to send webmentions for likes/reposts
- This enables showing social media reactions as webmentions

## Files to Modify

1. `layouts/_default/baseof.html` - Add endpoint link, script include, JS config
2. `layouts/_default/single.html` - Add webmention container, optional h-entry microformats
3. `layouts/partials/style.html` - Add webmention styling
4. `static/js/webmention.min.js` - Add new file (download webmention.js)

## Testing Checklist

- [ ] webmention.io account created and verified
- [ ] Endpoint link appears in HTML head
- [ ] webmention.js loads without errors
- [ ] Webmention container renders on blog posts
- [ ] Styling matches blog theme
- [ ] Test webmention received and displayed
- [ ] mobile responsiveness tested
- [ ] accessibility tested (keyboard nav, screen reader)

## Rollback Plan

If issues arise:
1. Remove webmention endpoint link from baseof.html
2. Remove webmention.js script from baseof.html
3. Remove webmention container from single.html
4. Remove webmention CSS from style.html
5. Delete static/js/webmention.min.js
6. Commit reversal

## Future Enhancements (Optional)

- Add mention counter to post list
- Implement moderation via webmention.io settings
- Add ability to filter by mention type (reply, like, repost)
- Export webmentions to data files for server-side rendering
- Add webmention verification during builds

## Questions Before Implementation

1. **Domain verification:** Do you have access to add DNS records or upload verification files for webmention.io?

2. **Social media:** Do you want to enable Brid.gy integration to show Mastodon/Twitter likes and reposts as webmentions?

3. **Mention types:** Are you interested in showing all mention types (replies, likes, reposts), or just replies/comments?

4. **Styling preferences:** Any specific styling preferences for the webmention section, or should I match your existing theme?

5. **Mobile consideration:** Should webmentions be collapsible on mobile to save space?
