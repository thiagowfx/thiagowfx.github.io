HUGO = hugo

# Abort if hugo is not installed.
ifeq (, $(shell which $(HUGO)))
  $(error "No hugo in $$PATH, install it first")
endif

dev:
	# Listens on port 1313 by default
	$(HUGO) server --buildDrafts --watch

clean:
	fuser -k 1313/tcp

.PHONY: dev clean
