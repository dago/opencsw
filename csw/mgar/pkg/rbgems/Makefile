# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

default:
	@echo "You are in the pkg/rbgems directory."

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

lcase = $(shell echo $(1) | tr '[A-Z]' '[a-z]' ) 

# You can use "gmake newpkg-ruby-gem".
newpkg-%: dir = $(subst ::,-,$*)
newpkg-%:
	@svn mkdir $(dir) $(dir)/tags $(dir)/branches $(dir)/trunk $(dir)/trunk/files
	@svn cp ../template/Makefile $(dir)/Makefile
	@if [ -d ../../gar/v2 ]; then \
	  ln -s ../../../../gar/v2 $(dir)/trunk/gar; \
	  cd $(dir)/trunk/gar; svn update; \
	else \
	  svn co https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2 $(dir)/trunk/gar; \
	fi
	@echo "gar https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2" | svn propset svn:externals -F /dev/fd/0 $(dir)/trunk
	@echo "work\n" | svn propset svn:ignore -F /dev/fd/0 $(dir)/trunk
	@(cd $(dir)/trunk/; gem fetch $*; gar/bin/gem2pkg *gem > Makefile; rm *gem)
	@( cd $(dir)/trunk; gmake fetch; gmake makesums; gmake garchive );
	@svn add $(dir)/trunk/Makefile $(dir)/trunk/checksums
	@echo "work\n" | svn propset svn:ignore -F /dev/fd/0 $(dir)/trunk
	@echo
	@echo "Your package is set up for editing at $(dir)/trunk"



