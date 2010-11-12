# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

# This is needed by the pkg build approach with gar/ in each pkg build
# directory and is overriden by the "mgar" wrapper which pre-sets GARDIR
# with an absolute path. If we could determine the full path of
# _this_ file's directory, we could use it for both approaches and
# there would be no need to pre-set it for "mgar".
GARDIR ?= $(CURDIR)/gar

ifeq (,$(wildcard $(GARDIR)/categories/$(CATEGORIES)/category.mk))
  $(error The category '$(CATEGORIES)' is invalid. Valid categories are: $(patsubst $(GARDIR)/categories/%,%,$(wildcard $(GARDIR)/categories/*)))
endif

include $(GARDIR)/categories/$(CATEGORIES)/category.mk
