# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

ifeq (,$(wildcard gar/categories/$(CATEGORIES)/category.mk))
  $(error The category '$(CATEGORIES)' is invalid. Valid categories are $(patsubst gar/categories/%,%,$(wildcard gar/categories/*)))
endif

include gar/categories/$(CATEGORIES)/category.mk
