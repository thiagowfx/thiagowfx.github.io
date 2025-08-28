#!/usr/bin/env just --justfile
# https://github.com/casey/just

# Start a hugo server in watch mode
watch preview="true" *args:
    #!/usr/bin/env bash
    set -euo pipefail

    additional_flags=()
    if [ "{{ preview }}" = "true" ]; then
    	additional_flags+=("--openBrowser" "--navigateToChanged")
    fi
    hugo server --buildDrafts --port ${PORT:-1313} --watch "${additional_flags[@]}" {{ args }}

# Build the blog as in production
build *args:
    hugo --environment production --gc --minify {{ args }}

# Create a new post. Usage: `just new "advent of code day 8"`
new title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/: /-/g' | tr ' ' '-')
    hugo new content/posts/`date "+%Y-%m-%d"`-${filename}.md {{ args }}

# Create a new coding post. Usage: `just code "leetcode #1"`.
code title *args:
    #!/usr/bin/env bash
    set -euo pipefail

    filename=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | sed -e 's/: /-/g' | tr ' ' '-')
    hugo new --kind coding content/posts/`date "+%Y-%m-%d"`-${filename}.md {{ args }}

# Delete hugo build artifacts
clean:
    rm -rf public/ resources/

# Ping search engines about changes in the sitemap
ping sitemap="https://perrotta.dev/sitemap.xml":
    curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
    curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"

# Update git submodules and pre-commit hooks
update: update-git update-pre-commit

# Update git submodules
update-git:
    git submodule update --remote --jobs "$(nproc)"

# Update pre-commit hooks
update-pre-commit:
    pre-commit autoupdate --freeze --jobs "$(nproc)" && pre-commit run --all-files
