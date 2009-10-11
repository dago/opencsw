#####################################################################
# OpenCSW build recipe for bash
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

GARNAME = bash
GARVERSION = 4.0.33
CATEGORIES = devel

DESCRIPTION = A sh-compatible command language interpreter
define BLURB
  GNU Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh). Bash is intended to be a conforming implementation of the IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).
endef

BASH_VERSION = $(shell echo $(GARVERSION)c | cut -d. -f1-2)
BASH_PATCHLEVEL = $(shell echo -n $(GARVERSION) | cut -d. -f3)

PACKAGES = CSWbash

REQUIRED_PKGS = CSWggettextrt
REQUIRED_PKGS += CSWiconv

SPKG_CLASSES = none build

###### Upstream and opencsw files information #######

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = bash-(\d+\.\d+).tar.gz $(PATCHFILE_PREFIX)-(\d+)

# Patches download location
MASTER_SITES = $(GNU_MIRROR)/bash-$(BASH_VERSION)-patches/
# Main archive location
MASTER_SITES += $(GNU_MIRROR)
DISTNAME = $(GARNAME)-$(BASH_VERSION)
DISTFILES  = $(GARNAME)-$(BASH_VERSION).tar.gz
DISTFILES += CSWbash.prototype
DISTFILES += changelog.CSW

# build action script to modify /etc/shells at package installation and removal time
DISTFILES += shells

PATCHFILE_PREFIX = bash$(subst .,,$(BASH_VERSION))
PATCHDIRLEVEL = 0
# we generate the list of patches from the PATCHLEVEL
PATCHFILES = $(shell LEVEL=1; \
	        PREFIX_0="00"; \
	     	while [ $$LEVEL -le $(BASH_PATCHLEVEL)  ]; do \
			echo $(PATCHFILE_PREFIX)-$$PREFIX_0$$LEVEL; \
			LEVEL=`expr $$LEVEL + 1`; \
			if [ $$LEVEL -ge 10 ]; then \
				PREFIX_0="0"; \
			fi; \
		done )

#
# opencsw bash use /etc/bash.bashrc and /etc/bash.bash_logout files
PATCHFILES += use_system_bashrc_and_logout.patch


##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# We touch these file to avoid aclocal/autoconf
# configure to be run again
pre-configure:
	touch $(WORKSRC)/aclocal.m4
	touch $(WORKSRC)/configure
	touch $(WORKSRC)/config.status


post-merge:
	@( for FILE in README RBASH NEWS NOTES POSIX AUTHORS doc/FAQ doc/INTRO; do \
		 ginstall -D $(WORKSRC_FIRSTMOD)/$$FILE $(PKGROOT)$(docdir)/$(GARNAME)/`basename $$FILE`; \
	done )
	ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKDIR_FIRSTMOD)/shells $(PKGROOT)/etc/shells
