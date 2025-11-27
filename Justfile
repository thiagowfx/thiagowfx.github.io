#!/usr/bin/env just --justfile
# https://github.com/casey/just

editor := env_var_or_default("EDITOR", "vim")
port := env_var_or_default("PORT", "1313")

# Start a hugo server in watch mode
watch preview="true" *args:
    #!/usr/bin/env bash
    set -euo pipefail

    additional_flags=""
    if [ "{{ preview }}" = "true" ]; then
      additional_flags="--openBrowser --navigateToChanged"
    fi
    hugo server --baseURL "http://localhost:{{ port }}" --buildDrafts --port {{ port }} --watch $additional_flags {{ args }}

# Build the blog as in production
build *args:
    hugo --environment production --gc --minify {{ args }}

# Create a new blog post. Usage: `just new "my cool title"`
new title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/: /-/g' | tr ' ' '-')
    filepath="content/posts/`date "+%Y-%m-%d"`-${filename}.md"
    hugo new --kind blog "${filepath}" {{ args }}
    {{ editor }} "${filepath}"

alias blog := new

# Create a new coding post. Usage: `just code "leetcode #1"` or `just code "bytebytego #1"` or `just code "ByteByteGo: Triplet Sum"`.
code title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/#//g' -e 's/:/ /g' | tr -s ' ' | tr ' ' '-')
    filepath="content/posts/`date "+%Y-%m-%d"`-${filename}.md"

    hugo_title="{{ title }}"
    hugo_leetcode_slug=""
    hugo_bytebytego_slug=""
    if [[ "{{ title }}" == "LeetCode"* ]]; then
      # Handle both "LeetCode #1: Problem" and "LeetCode: Problem" formats
      problem_name=$(echo "{{ title }}" | sed -e 's/LeetCode \(#[0-9]*: \)\?//')
      hugo_leetcode_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    elif [[ "{{ title }}" == "ByteByteGo"* ]]; then
      # Handle both "ByteByteGo #1: Problem" and "ByteByteGo: Problem" formats
      problem_name=$(echo "{{ title }}" | sed -e 's/ByteByteGo \(#[0-9]*: \)\?//')
      hugo_bytebytego_slug=$(echo "${problem_name}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    fi

    HUGO_TITLE="${hugo_title}" HUGO_LEETCODE_SLUG="${hugo_leetcode_slug}" HUGO_BYTEBYTEGO_SLUG="${hugo_bytebytego_slug}" hugo new --kind coding "${filepath}" {{ args }}
    {{ editor }} "${filepath}"

alias coding := code

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
    git commit -m "lazy commit" -n {{ args }}

# Delete hugo build artifacts
clean:
    rm -rf public/ resources/
    git clean -x -f -d

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
