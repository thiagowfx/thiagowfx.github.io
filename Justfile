#!/usr/bin/env just --justfile
# https://github.com/casey/just

set dotenv-load

# Start a hugo server in watch mode
watch preview="true":
	#!/usr/bin/env bash
	additional_flags=()
	if [ "{{preview}}" = "true" ]; then
		additional_flags+=("--openBrowser" "--navigateToChanged")
	fi
	hugo server --buildDrafts --port ${PORT:-1313} --watch "${additional_flags[@]}"

# Build the blog as in production
build:
	hugo --environment production --gc --minify

# Create a new post. Usage: `just new "advent of code day 8"`
new title:
	hugo new content/posts/`date "+%Y-%m-%d"`-{{ kebabcase(title) }}.md

# Delete hugo build artifacts
clean:
	rm -rf public/ resources/

# Update git submodules
update:
	git submodule update --remote
	pre-commit autoupdate

# Ping Google and Bing about changes in the sitemap
ping sitemap="https://perrotta.dev/sitemap.xml":
	curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
	curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"
