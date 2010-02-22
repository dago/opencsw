# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 6092 2009-08-23 21:50:45Z skayser $
#
# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

default:
	@echo "You are in the pkg/x11/lib directory."

%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || exit 2; \
	done

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
	done

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@(echo "GARNAME = $*";                                     \
	echo "GARVERSION = 1.0";                                        \
	echo "CATEGORIES = category";                                   \
	echo "";                                                        \
	echo "DESCRIPTION = Brief description";                         \
	echo "define BLURB";                                            \
	echo "  Long description";                                      \
	echo "endef";                                                   \
	echo "";                                                        \
	echo "MASTER_SITES = ";                                         \
	echo "DISTFILES  = $$(GARNAME)-$$(GARVERSION).tar.gz";          \
	echo "";                                                        								\
	echo "# We define upstream file regex so we can be notifed of new upstream software release";  	\
	echo "UFILES_REGEX = $$(GARNAME)-(\d+(?:\.\d+)*).tar.gz";										\
	echo "";                                                        								\
	echo "# If the url used to check for software update is different of MASTER_SITES, then ";   	\
	echo "# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES"; 	\
	echo "# UPSTREAM_MASTER_SITES = ";                                         						\
	echo "";                                                        \
	echo "CONFIGURE_ARGS = $$(DIRPATHS)";                           \
	echo "";                                                        \
	echo "include gar/category.mk";                                 \
	) > $*/trunk/Makefile
	@touch $*/trunk/checksums
	@svn add $*/trunk/Makefile $*/trunk/checksums
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo "gar https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2" | svn propset svn:externals -F /dev/fd/0 $*/trunk
	@if [ -d ../../gar/v2 ]; then \
	  ln -s ../../../../gar/v2 $*/trunk/gar; \
	else \
	  svn co https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2 $*/trunk/gar; \
	fi
	@echo
	@echo "Your package is set up for editing at $*/trunk"

