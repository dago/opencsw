
stoptheunwary:
	$(error "*** You are in the GAR directory and probably didn't mean to call make")

FILTER_DIRS = CVS/ bin/ meta/
# top-level Makefile for the entire tree.
%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $@ || exit 2; \
	done

unbuilt:
	@(gfind . -mindepth 3 -maxdepth 3 -name work | cut -d/ -f 3; gfind . -mindepth 2 -maxdepth 2 | cut -d/ -f3) | sort | uniq -u

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@echo "$@ started at $$(date)" >> $(BUILDLOG)
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $@ || echo "	make $@ in category $$i failed" >> $(BUILDLOG); \
	done
	@echo "$@ completed at $$(date)" >> $(BUILDLOG)

pkgdesc = `/bin/perl -ne '/DESCRIPTION\s+=\s+(.+)$$/ && print $$1' $(1)/Makefile`

# Rebuild the package database
rebuildpkgdb:
	@echo " ==> Rebuilding package database"
	-@rm -f pkg.db
	@bin/build_pkgdb > pkg.db

cvsdesc:
	@for package in $(shell gfind . -type d -mindepth 2 -maxdepth 2 -not -name 'CVS' -a -not -name '00CPAN_Module_Template' | gsed -e 's/^\.\///') ; do \
		printf "%-36s%s\n" sunx/$$package "$(call pkgdesc,$$package)" ; \
	done

GARDIR=$(CURDIR)
include gar.mk

pkgclean:
	@if test -d "$(DESTBUILD)" ; then \
		echo " ==> Removing $(DESTBUILD)" ; \
		rm -rf $(DESTBUILD) ; \
	fi
	@if test -d "$(SPKG_SPOOLDIR)" ; then \
		echo " ==> Removing $(SPKG_SPOOLDIR)" ; \
		rm -rf $(SPKG_SPOOLDIR) ; \
	fi

.PHONY: unbuilt
