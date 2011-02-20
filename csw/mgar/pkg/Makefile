# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

# This contains all directories containing packages
SUBDIRS = cpan xfce


MY_SVN_DIR=$(shell svn info | awk -F: '$$1=="URL"{print $$2":"$$3}' )


FILTER_DIRS = CVS/

default:
	@echo "You are in the pkg/ directory."

scm-update-packages:
	@echo "Updating packages..."
	@svn up --ignore-externals

scm-help:
	@cat ../gar/v2/scm-help

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

# When the complete package tree is checked out there would be literally hundreds
# of instances of GAR as they are referenced as external references. Alternatively
# you can check out the tree with
#   svn co --ignore-externals https://.../pkg
# and then run
#   gmake garlinks
# to generate symbolic links instead of externally checked out dirs

# Lines returned by 'svn propget -R' look like this:
#
# gar/trunk - gar https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2
# gar-v1 https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v1
# gar-v2 https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2
# 
# ...

garlinks:
	@(svn propget svn:externals -R | perl -ane 'next if( /^$$/ ); if( $$F[1] eq "-" ) { ($$path,$$sep,$$dir,$$link)=@F; } else { ($$dir,$$link) = @F; } ($$upsteps=$$path)=~s![^/]+!..!g;(($$linkdest=$$link))=~ s!https://gar.svn.(?:sourceforge|sf).net/svnroot/gar/csw/mgar!$$upsteps!;unlink("$$path/$$dir"); print "Linking $$path/$$dir to ../$$linkdest", symlink("../$$linkdest","$$path/$$dir") ? "" : " failed", "\n";')

pkglist:
	@for i in $(filter-out $(FILTER_DIRS),$(foreach D,. $(SUBDIRS),$(wildcard $D/*/))) ; do \
		$(MAKE) -s -C $$i/trunk pkglist ; \
	done

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@svn cp template/Makefile $*/Makefile
	@(echo '# $$Id$$';   								\
	echo "NAME = $*";                                     								\
	echo "VERSION = 1.0";                                        								\
	echo "CATEGORIES = category";                                   								\
	echo "";                                                        								\
	echo "DESCRIPTION = Brief description";                         								\
	echo "define BLURB";                                            								\
	echo "  Long description";                                      								\
	echo "endef";                                                   								\
	echo "";                                                        								\
	echo "MASTER_SITES = ";                                         								\
	echo "DISTFILES  = $$(DISTNAME).tar.gz";          								\
	echo "";                                                        								\
	echo "# File name regex to get notifications about upstream software releases"; \
	echo "# NOTE: Use this only if the automatic regex creation"; \
	echo "#       does not work for your package";	\
	echo "# UFILES_REGEX = $$(NAME)-(\d+(?:\.\d+)*).tar.gz";										\
	echo "";                                                        								\
	echo "# If the url used to check for software update is different of MASTER_SITES, then ";   	\
	echo "# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES"; 	\
	echo "# UPSTREAM_MASTER_SITES = ";                                         						\
	echo "";                                                        								\
	echo "CONFIGURE_ARGS = $$(DIRPATHS)";                          									\
	echo "";                                                        								\
	echo "include gar/category.mk";                                 								\
	) > $*/trunk/Makefile
	@touch $*/trunk/checksums
	@svn add $*/trunk/Makefile $*/trunk/checksums
	@svn ps svn:keywords Id $*/trunk/Makefile
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo "gar https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2" | svn propset svn:externals -F /dev/fd/0 $*/trunk
	@if [ -d ../gar/v2 ]; then \
	  ln -s ../../../gar/v2 $*/trunk/gar; \
	else \
	  svn co https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2 $*/trunk/gar; \
	fi
	@echo
	@echo "Your package is set up for editing at $*/trunk"


TEMPLATES/createpkg:
	@echo Checking out TEMPLATES directory...
	svn --ignore-externals co $(MY_SVN_DIR)/TEMPLATES


createpkg-%: TEMPLATES/createpkg
	@TEMPLATES/createpkg/copy_template $*
	
