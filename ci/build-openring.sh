#!/usr/bin/env bash
set -o pipefail

# Build OpenRing HTML from blogroll.yaml
# Generates 3 random recent articles from feeds

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_FILE="${REPO_ROOT}/layouts/partials/openring.html"
OPML_INPUT="${REPO_ROOT}/data/blogroll.yaml"

# Ensure openring is installed
if ! command -v openring &>/dev/null; then
    echo "Installing openring..."
    if ! go install git.sr.ht/~sircmpwn/openring@latest 2>&1; then
        echo "Failed to install openring"
        exit 1
    fi
fi

# Create a temporary template for openring (HTML template with {{.Articles}} loop)
TEMP_TEMPLATE=$(mktemp)
trap 'rm -f "$TEMP_TEMPLATE"' EXIT

cat > "$TEMP_TEMPLATE" << 'TEMPLATE'
<div style="border: 2px solid var(--border-color); border-radius: 0.5rem; padding: 1.5rem; margin: 2rem 0;">
  <h4 style="margin-top: 0;">Random blogs from my blogroll</h4>
  <section style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0;">
    {{ range .Articles }}
    <article style="flex: 1 1 250px; padding: 1rem; background: var(--code-bg); border-radius: 0.25rem; color: var(--text-color);">
      <h5 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--heading-color);">
        <a href="{{ .Link }}" target="_blank" rel="noopener">{{ .Title }}</a>
      </h5>
      <p style="margin: 0.5rem 0; font-size: 0.9rem;">{{ .Summary }}</p>
      <small style="color: var(--color-gray);">via <a href="{{ .SourceLink }}">{{ .SourceTitle }}</a> · {{ .Date.Format "Jan 2, 2006" }}</small>
    </article>
    {{ end }}
  </section>
  <p style="margin: 1rem 0 0 0; font-size: 0.9rem;"><a href="https://git.sr.ht/~sircmpwn/openring">Powered by OpenRing</a></p>
</div>
TEMPLATE

# Extract feed URLs from blogroll.yaml and sample random feeds
TEMP_OUT=$(mktemp)
trap 'rm -f "$TEMP_TEMPLATE" "$TEMP_OUT"' EXIT

# Parse YAML and extract feed URLs, exclude own blog, sample 5 random ones
echo "Sampling feeds from blogroll..."
FEEDS=$(grep -E '^\s+feed:' "$OPML_INPUT" | sed 's/.*feed:[[:space:]]*//' | sed 's/[[:space:]]*$//' | grep -v "perrotta.dev" | shuf | head -5 || true)

# Build openring command
OPENRING_ARGS="-n 3"  # Get 3 articles total
FEED_COUNT=0
while IFS= read -r feed; do
    [ -n "$feed" ] && OPENRING_ARGS="$OPENRING_ARGS -s '$feed'" && ((FEED_COUNT++))
done <<< "$FEEDS"
echo "Running openring with $FEED_COUNT feeds (timeout: 120s)..."

# Run with timeout (120s) and capture stderr
if timeout 120 bash -c "eval 'openring $OPENRING_ARGS' < '$TEMP_TEMPLATE'" > "$TEMP_OUT" 2>/tmp/openring.err; then
    # Check if output is not empty
    if [ -s "$TEMP_OUT" ]; then
        mkdir -p "$(dirname "$OUTPUT_FILE")"
        mv "$TEMP_OUT" "$OUTPUT_FILE"
        echo "✓ Generated OpenRing"
    else
        echo "⚠ OpenRing generated empty output"
        mkdir -p "$(dirname "$OUTPUT_FILE")"
        cat > "$OUTPUT_FILE" << 'STUB'
<!-- OpenRing: feeds returned no articles -->
STUB
    fi
else
    echo "⚠ OpenRing generation failed/timed out."
    if [ -f /tmp/openring.err ]; then
        echo "Error:"
        cat /tmp/openring.err
    fi
    mkdir -p "$(dirname "$OUTPUT_FILE")"
    cat > "$OUTPUT_FILE" << 'STUB'
<!-- OpenRing generation will be enabled on deploy -->
STUB
fi
