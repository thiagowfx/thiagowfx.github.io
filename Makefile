# Homepage URL.
BASE_URL ?= $(shell hostname)

# Path to hugo binary.
HUGO := hugo

# Listens on port 1313 by default.
PORT := 1313

# Abort if hugo is not installed.
ifeq (, $(shell which $(HUGO)))
  $(error "No hugo in $$PATH, install it first")
endif

dev:
	$(HUGO) server --baseUrl="$(BASE_URL)" --bind="0.0.0.0" --buildDrafts --port $(PORT) --watch

clean:
	-fuser -k $(PORT)/tcp
	$(RM) -r public/ resources/

pull:
	git submodule update --init --remote

.PHONY: dev clean pull
