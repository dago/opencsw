# vim: ft=make ts=4 sw=4 noet
#
# This Makefile is the main entry point to GAR and is included by
# each package build description. As such, the file name 'category.mk'
# is slightly misleading and could be subject to future change.
#

# Determine this file's directory, i.e. the GAR base directory
GARDIR := $(dir $(lastword $(MAKEFILE_LIST)))

ifeq (,$(wildcard $(GARDIR)/categories/$(CATEGORIES)/category.mk))
  $(error The category '$(CATEGORIES)' is invalid. Valid categories are: $(patsubst $(GARDIR)/categories/%,%,$(wildcard $(GARDIR)/categories/*)))
endif

include $(GARDIR)/categories/$(CATEGORIES)/category.mk
