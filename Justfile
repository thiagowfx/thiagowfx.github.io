#!/usr/bin/env just --justfile
# https://github.com/casey/just

editor := env_var_or_default("EDITOR", "vim")
port := env_var_or_default("PORT", "1313")

# Start a hugo server in watch mode
watch preview="true" *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ "{{ preview }}" = "true" ]; then
      open "http://localhost:{{ port }}/posts/" &
    fi

    hugo server --port {{ port }} --watch {{ args }}

# Build the blog as in production
build with-openring="false" *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ "{{ with-openring }}" = "true" ]; then
        ./ci/build_openring.sh
    fi
    hugo --environment production --gc {{ args }}

# Quick build for pre-commit (skips expensive template logic)
build-quick *args:
    hugo --environment quick {{ args }}

# Create a new blog post. Usage: `just new "my cool title"`
new title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/: /-/g' | tr ' ' '-')
    filepath="content/posts/`date "+%Y-%m-%d"`-${filename}.md"
    hugo new --kind blog "${filepath}" {{ args }}
    {{ editor }} "${filepath}"

alias blog := new

# Create a new coding post. Usage: `just code "leetcode #1"` or `just code "bytebytego #1"` or `just code "ByteByteGo: Triplet Sum"` or `just code "AoC 2024 Day 1"`.
code title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/#//g' -e 's/:/ /g' | tr -s ' ' | tr ' ' '-')
    filepath="content/posts/`date "+%Y-%m-%d"`-${filename}.md"

    hugo_title="{{ title }}"
    hugo_leetcode_slug=""
    hugo_bytebytego_slug=""
    hugo_aoc_slug=""
    if [[ "{{ title }}" == "LeetCode"* ]]; then
      # Handle "LeetCode #1: Problem", "LeetCode 1. Problem", and "LeetCode: Problem" formats
      # Normalize "LeetCode 1. Problem" to "LeetCode #1: Problem"
      if [[ "{{ title }}" =~ LeetCode[[:space:]]+([0-9]+)\. ]]; then
        problem_number="${BASH_REMATCH[1]}"
        problem_name=$(echo "{{ title }}" | sed -e 's/LeetCode [0-9]*\. //')
        hugo_title="LeetCode #${problem_number}: ${problem_name}"
      fi
      problem_name=$(echo "${hugo_title}" | sed -e 's/LeetCode \(#[0-9]*: \|[0-9]*\. \)\?//')
      hugo_leetcode_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    elif [[ "{{ title }}" == "ByteByteGo"* ]]; then
      # Handle both "ByteByteGo #1: Problem" and "ByteByteGo: Problem" formats
      problem_name=$(echo "{{ title }}" | sed -e 's/ByteByteGo \(#[0-9]*: \)\?//')
      hugo_bytebytego_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    elif [[ "{{ title }}" == "AoC"* ]] || [[ "{{ title }}" == "Advent"* ]]; then
      # Handle "AoC YYYY Day N" or "Advent of Code YYYY Day N" formats
      problem_name=$(echo "{{ title }}" | sed -e 's/\(AoC\|Advent of Code\) //')
      hugo_aoc_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    fi

    HUGO_TITLE="${hugo_title}" HUGO_LEETCODE_SLUG="${hugo_leetcode_slug}" HUGO_BYTEBYTEGO_SLUG="${hugo_bytebytego_slug}" HUGO_AOC_SLUG="${hugo_aoc_slug}" hugo new --kind coding "${filepath}" {{ args }}

    # Check for duplicate LeetCode posts before opening editor
    if [[ "{{ title }}" == "LeetCode"* ]]; then
        if ! ci/check_duplicate_leetcode_posts.py; then
            echo ""
            echo "❌ Duplicate LeetCode post detected! Please resolve the duplicate before editing."
            rm "${filepath}"
            exit 1
        fi
    fi

    {{ editor }} '+/^```/' "${filepath}"

alias coding := code

# Search for and edit a blog post. Usage: `just edit` or `just edit <term>`
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

alias search := edit

# Edit the most recent blog post
last:
    #!/usr/bin/env bash
    set -euo pipefail

    latest=$(ls -t content/posts/*.md 2>/dev/null | head -n 1 || true)
    if [ -z "$latest" ]; then
      echo "No posts found in content/posts/"
      exit 1
    fi
    {{ editor }} "$latest"

# Create a git commit without any substance
lazy *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -z "{{ args }}" ]; then
        msg="lazy commit"
    else
        msg="{{ args }}"
    fi
    git commit -m "$msg" -n && git pushm

# Delete hugo build artifacts
clean:
    rm -rf public/ resources/
    git clean -x -f -d

# Lint and validate with pre-commit hooks
lint *args:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -z "{{ args }}" ]; then
        pre-commit run --all-files
    else
        pre-commit run --files {{ args }}
    fi

# Ping search engines about changes in the sitemap
ping sitemap="https://perrotta.dev/sitemap.xml":
    curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
    curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"

# Update git submodules, pre-commit hooks and JSON schemas
update: update-git update-pre-commit update-json-schemas

# Update git submodules
update-git:
    git submodule update --remote --jobs "$(nproc)"

# Update pre-commit hooks
update-pre-commit:
    pre-commit autoupdate --freeze --jobs "$(nproc)" && pre-commit run --all-files

# Update JSON schemas
update-json-schemas:
    pre-commit run -a update-json-schemas --hook-stage manual
