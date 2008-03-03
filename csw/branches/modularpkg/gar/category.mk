# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

ifeq (,$(CATEGORIES))
  $(error Please set CATEGORIES to one of $(wildcard categories/*))
endif

include gar/categories/$(CATEGORIES)/category.mk

#%:
#	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
#		$(MAKE) -C $$i $* ; \
#	done
#
#paranoid-%:
#	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
#		$(MAKE) -C $$i $* || exit 2; \
#	done
#
#export BUILDLOG ?= $(shell pwd)/buildlog.txt
#
#report-%:
#	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
#		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
#	done
