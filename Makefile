HUGO = hugo

# Listens on port 1313 by default
PORT = 1313

# Abort if hugo is not installed.
ifeq (, $(shell which $(HUGO)))
  $(error "No hugo in $$PATH, install it first")
endif

dev:
	$(HUGO) server --buildDrafts --port $(PORT) --watch

clean:
	fuser -k $(PORT)/tcp

.PHONY: dev clean
