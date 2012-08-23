# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

MY_SVN_DIR=$(shell svn info | awk -F: '$$1=="URL"{print $$2":"$$3}' )


FILTER_DIRS = CVS/

default:
	@echo "You are in the pkg/lang-python directory."

scm-update-packages:
	@echo "Updating packages..."
	@svn up --ignore-externals

scm-help:
	@cat ../../gar/v2/scm-help

%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || exit 2; \
	done

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
	done

pkglist:
	@for i in $(filter-out $(FILTER_DIRS),$(foreach D,. $(SUBDIRS),$(wildcard $D/*/))) ; do \
		$(MAKE) -s -C $$i/trunk pkglist ; \
	done

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@svn cp ../template/Makefile $*/Makefile
	@python -c 'from mako.template import Template; \
		v = { "name": "$*", "version": "x.y" }; \
		t = Template(filename="newpkg-Makefile"); \
		print t.render(**v)' > $*/trunk/Makefile
	@touch $*/trunk/checksums
	@svn add $*/trunk/Makefile $*/trunk/checksums
	@svn ps svn:keywords Id $*/trunk/Makefile
	@echo "work\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo
	@echo "Your package is set up for editing at $*/trunk"


TEMPLATES/createpkg:
	@echo Checking out TEMPLATES directory...
	svn --ignore-externals co $(MY_SVN_DIR)/TEMPLATES


createpkg-%: TEMPLATES/createpkg
	@TEMPLATES/createpkg/copy_template $*
	
