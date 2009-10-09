# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

ifeq (,$(CATEGORIES))
  $(error Please set CATEGORIES to one of $(wildcard categories/*))
endif

include gar/categories/$(CATEGORIES)/category.mk
