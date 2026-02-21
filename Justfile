#!/usr/bin/env just --justfile
# https://github.com/casey/just
# Justfile for perrotta.dev blog - Hugo-based site with custom build pipeline

editor := env_var_or_default("EDITOR", "vim")
port := env_var_or_default("PORT", "1313")

[doc('Start a hugo dev server with live reload')]
[group('server')]
watch preview="true" *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ "{{ preview }}" = "true" ]; then
      open "http://localhost:{{ port }}/posts/" &
    fi

    hugo server --port {{ port }} --watch --navigateToChanged {{ args }}

[doc('Precompute post relationships (backlinks, related, previously, graph)')]
[group('build')]
precompute:
    python3 ci/precompute_links.py

[doc('Build the blog for production')]
[group('build')]
build with-openring="false" *args: precompute
    #!/usr/bin/env bash
    set -euo pipefail

    if [ "{{ with-openring }}" = "true" ]; then
        ./ci/build_openring.sh
    fi
    hugo --environment production --gc {{ args }}

[doc('Quick build for pre-commit (skips expensive template logic)')]
[group('build')]
build-quick *args:
    hugo --environment quick {{ args }}

[doc('Create a new blog post - Usage: `just new "my cool title"`')]
[group('create')]
new *args:
    #!/usr/bin/env bash
    set -euo pipefail

    title="{{ args }}"
    if [[ -z "${title}" ]]; then
        echo "error: title is required. Usage: just new \"my cool title\"" >&2
        exit 1
    fi
    filename=$(echo "${title}" | tr '[:upper:]' '[:lower:]' | sed -e 's/[,:/]/-/g' | tr -s ' ' | tr ' ' '-')
    filepath="content/posts/$(date "+%Y-%m-%d")-${filename}.md"
    hugo new --kind blog "${filepath}"
    {{ editor }} "${filepath}"

alias blog := new

[doc('Create a new coding/problem post - Examples: `just code "leetcode #1"` or `just code "ByteByteGo: Triplet Sum"` or `just code "AoC 2024 Day 1"`')]
[group('create')]
code *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ args }}" | sed -e 's/#//g' -e 's/\.//g' -e 's/,//g' | tr '[:upper:]' '[:lower:]' | sed -e 's/:/ /g' | tr -s ' ' | tr ' ' '-')
    filepath="content/posts/coding/`date "+%Y-%m-%d"`-${filename}.md"

    hugo_title="{{ args }}"
    hugo_leetcode_slug=""
    hugo_bytebytego_slug=""
    hugo_aoc_slug=""
    hugo_tags=""
    if [[ "{{ args }}" == "LeetCode"* ]]; then
      # Handle "LeetCode #1: Problem", "LeetCode 1. Problem", and "LeetCode: Problem" formats
      # Normalize "LeetCode 1. Problem" to "LeetCode #1: Problem"
      if [[ "{{ args }}" =~ LeetCode[[:space:]]+([0-9]+)\. ]]; then
        problem_number="${BASH_REMATCH[1]}"
        problem_name=$(echo "{{ args }}" | sed -e 's/LeetCode [0-9]*\. //')
        hugo_title="LeetCode #${problem_number}: ${problem_name}"
      fi
      problem_name=$(echo "${hugo_title}" | sed -e 's/LeetCode \(#[0-9]*: \|[0-9]*\. \)\?//')
      hugo_leetcode_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
      hugo_tags="leetcode"
    elif [[ "{{ args }}" == "ByteByteGo"* ]]; then
      # Handle both "ByteByteGo #1: Problem" and "ByteByteGo: Problem" formats
      problem_name=$(echo "{{ args }}" | sed -e 's/ByteByteGo \(#[0-9]*: \)\?//')
      hugo_bytebytego_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
      hugo_tags="bytebytego"
    elif [[ "{{ args }}" == "AoC"* ]] || [[ "{{ args }}" == "Advent"* ]]; then
      # Handle "AoC YYYY Day N" or "Advent of Code YYYY Day N" formats
      problem_name=$(echo "{{ args }}" | sed -e 's/\(AoC\|Advent of Code\) //')
      hugo_aoc_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
      hugo_tags="advent-of-code"
    fi

    HUGO_TITLE="${hugo_title}" HUGO_LEETCODE_SLUG="${hugo_leetcode_slug}" HUGO_BYTEBYTEGO_SLUG="${hugo_bytebytego_slug}" HUGO_AOC_SLUG="${hugo_aoc_slug}" HUGO_TAGS="${hugo_tags}" hugo new --kind coding "${filepath}"

    # Check for duplicate posts before opening editor
    if [[ "{{ args }}" == "LeetCode"* ]] || [[ "{{ args }}" == "ByteByteGo"* ]]; then
        if ! ci/check_duplicate_coding_posts.py; then
            echo ""
            echo "❌ Duplicate post detected! Please resolve the duplicate before editing."
            rm "${filepath}"
            exit 1
        fi
    fi

    {{ editor }} '+/^```/' "${filepath}"

alias coding := code

[doc('Create a new commentary/reply post - Usage: `just commentary https://example.com "optional title"`')]
[group('create')]
commentary url *args:
    #!/usr/bin/env bash
    set -euo pipefail

    # Extract title from remaining args, or fetch from URL, or use domain as fallback
    title="{{ args }}"
    if [ -z "$title" ]; then
        # Try to fetch the page title from the URL
        fetched_title=$(curl -sL "{{ url }}" | htmlq 'title' --text | head -1 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
        if [ -n "$fetched_title" ]; then
            # Convert to lowercase (only first letter uppercase is handled by keeping first char and lowercasing rest)
            title=$(echo "$fetched_title" | sed 's/./\L&/g; s/^./\U&/')
        else
            # Fallback to URL domain
            title=$(echo "{{ url }}" | sed -E 's|https?://([^/]+).*|\1|' | tr '[:upper:]' '[:lower:]')
        fi
    fi

    filename=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed -e 's/[,:/]/-/g' | tr -s ' ' | tr ' ' '-')
    filepath="content/posts/`date "+%Y-%m-%d"`-${filename}.md"

    HUGO_TITLE="Reply to: ${title}" HUGO_EXTERNAL_LINK="{{ url }}" hugo new --kind commentary "${filepath}"
    {{ editor }} "${filepath}"

    # Rename file based on the actual title from frontmatter (strip "Reply to: " prefix for filename)
    actual_title=$(sed -n 's/^title: "\(.*\)"$/\1/p' "${filepath}" | head -1)
    if [ -n "$actual_title" ]; then
        # Remove "Reply to: " prefix for the filename
        filename_title=$(echo "$actual_title" | sed -e 's/^Reply to: //')
        new_filename=$(echo "$filename_title" | tr '[:upper:]' '[:lower:]' | sed -e 's/[,:/]/-/g' | tr -s ' ' | tr ' ' '-')
        new_filepath="content/posts/$(date "+%Y-%m-%d")-${new_filename}.md"
        if [ "${filepath}" != "${new_filepath}" ]; then
            mv "${filepath}" "${new_filepath}"
            echo "Renamed to: ${new_filepath}"
        fi
    fi

alias comment := commentary

[doc('Search for and edit a blog post - Usage: `just edit` or `just edit <term>`')]
[group('manage')]
edit *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if command -v fd >/dev/null 2>&1; then
        finder="fd --extension md . content/posts"
    else
        finder="find content/posts -name *.md"
    fi

    if [ -z "{{ args }}" ]; then
        file=$($finder | fzf || true)
    else
        file=$($finder | fzf --query "{{ args }}" --select-1 || true)
    fi

    if [ -n "$file" ]; then
        {{ editor }} "$file"
    fi

[doc('Search for blog posts by name - Usage: `just search` or `just search <term>`')]
[group('manage')]
search *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if command -v fd >/dev/null 2>&1; then
        finder="fd --extension md -0 --exclude _index.md . content/posts"
    else
        finder="find content/posts -name *.md -not -name _index.md -print0"
    fi

    sort_by_date() { sed 's|.*\(/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]\)|\1\t&|' | sort | cut -f2-; }

    if [ -z "{{ args }}" ]; then
        $finder | tr '\0' '\n' | sort_by_date
    else
        $finder | tr '\0' '\n' | grep -i "{{ args }}" | sort_by_date || echo "No posts found matching '{{ args }}'"
    fi

alias list := search

[doc('Edit the most recent blog post')]
[group('manage')]
last:
    #!/usr/bin/env bash
    set -euo pipefail

    if command -v fd >/dev/null 2>&1; then
        latest=$(fd -e md . content/posts -0 | xargs -0 ls -dt 2>/dev/null | head -n 1 || true)
    else
        latest=$(find content/posts -name "*.md" -type f -exec ls -t {} + 2>/dev/null | head -n 1 || true)
    fi
    if [ -z "$latest" ]; then
      echo "No posts found in content/posts/"
      exit 1
    fi
    {{ editor }} "$latest"

[doc('Create a lazy git commit and push')]
[group('publish')]
lazy *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -z "{{ args }}" ]; then
        msg="lazy commit"
    else
        msg="{{ args }}"
    fi
    git commit -m "$msg" -n && git pushm

[doc('List all available Hugo tags')]
[group('utils')]
list-tags:
    @fd -e md . content/posts -x awk '/^tags:/{f=1;next} f && /^  - /{print substr($0,5)} f && /^[^ ]/{f=0}' | sort -u

[doc('Delete hugo build artifacts')]
[group('utils')]
clean:
    rm -rf public/ resources/
    git clean -x -f -d

[doc('Lint and validate with prek hooks')]
[group('utils')]
lint *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -z "{{ args }}" ]; then
        prek run --all-files
    else
        prek run --files {{ args }}
    fi

[doc('Ping search engines about sitemap changes')]
[group('publish')]
ping sitemap="https://perrotta.dev/sitemap.xml":
    curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
    curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"

[doc('Update git submodules, prek hooks, JSON schemas, and vendored dependencies')]
[group('utils')]
update: update-git update-prek update-json-schemas update-vendor

[doc('Update git submodules')]
[group('utils')]
update-git:
    git submodule update --remote --jobs "$(nproc)"

[doc('Update prek hooks')]
[group('utils')]
update-prek:
    prek auto-update --freeze --jobs "$(nproc)" && prek run --all-files

[doc('Update JSON schemas')]
[group('utils')]
update-json-schemas:
    prek run -a update-json-schemas --hook-stage manual

[doc('Update vendored dependencies (d3.js)')]
[group('utils')]
update-vendor:
    curl -sL "https://d3js.org/d3.v7.min.js" -o static/vendor/d3.v7.min.js
