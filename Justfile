# https://github.com/casey/just

set dotenv-load

watch:
	hugo server --buildDrafts --port ${PORT:-1313} --watch

build:
	hugo --environment production --gc --minify

# Create a new post. Usage: `just new "advent of code day 8"`
new post:
	hugo new content/posts/`date "+%Y-%m-%d"`-{{ kebabcase(post) }}.md

clean:
	rm -rf public/ resources/

update:
	git submodule update --remote

# Ping Google and Bing about changes in the sitemap
ping sitemap="https://perrotta.dev/sitemap.xml":
	curl -sS -o /dev/null "https://www.google.com/ping?sitemap={{ sitemap }}"
	curl -sS -o /dev/null "https://www.bing.com/ping?sitemap={{ sitemap }}"
