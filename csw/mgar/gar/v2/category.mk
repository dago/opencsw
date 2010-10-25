# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

GARDIR ?= $(abspath gar)

ifeq (,$(wildcard $(GARDIR)/categories/$(CATEGORIES)/category.mk))
  $(error The category '$(CATEGORIES)' is invalid. Valid categories are: $(patsubst $(GARDIR)/categories/%,%,$(wildcard $(GARDIR)/categories/*)))
endif

include $(GARDIR)/categories/$(CATEGORIES)/category.mk
