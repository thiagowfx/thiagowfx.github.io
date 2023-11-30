# Sitemap URL.
SITEMAP = https://thiagowfx.github.io/sitemap.xml

# Path to hugo binary.
HUGO := hugo
# Hugo port
PORT := 1313

# Abort if hugo is not installed.
ifeq (, $(shell which $(HUGO)))
  $(error "No hugo in $$PATH, install it first")
endif

all:
	$(HUGO) server --bind="0.0.0.0" --buildDrafts --port $(PORT) --watch

clean:
	# kill process listening on port, if any; fail gracefully
	-fuser -k $(PORT)/tcp
	$(RM) -r public/ resources/

ping:
	# Ping Google about changes in the sitemap
	curl -sS -o /dev/null "https://www.google.com/ping?sitemap=$(SITEMAP)"
	# Ping Bing (DuckDuckGo, etc) about changes in the sitemap
	curl -sS -o /dev/null "https://www.bing.com/ping?sitemap=$(SITEMAP)"

.PHONY: all clean ping
