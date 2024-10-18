# Sitemap URL
SITEMAP = https://www.perrotta.dev/sitemap.xml

# Hugo port
PORT := 1313

# Abort if hugo is not installed.
ifeq (, $(shell which hugo))
  $(error "No hugo in $$PATH, install it first")
endif

all:
	hugo server --bind="0.0.0.0" --buildDrafts --port $(PORT) --watch

build:
	hugo --environment production --gc --minify

clean:
	$(RM) -r public/ resources/

ping:
	# Ping Google about changes in the sitemap
	curl -sS -o /dev/null "https://www.google.com/ping?sitemap=$(SITEMAP)"
	# Ping Bing (DuckDuckGo, etc) about changes in the sitemap
	curl -sS -o /dev/null "https://www.bing.com/ping?sitemap=$(SITEMAP)"

.PHONY: all build clean ping
