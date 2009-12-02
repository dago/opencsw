#####################################################################
# OpenCSW build recipe for rlwrap
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

GARNAME = rlwrap
GARVERSION = 0.33
CATEGORIES = utils

DESCRIPTION = A readline wrapper
define BLURB
  rlwrap is a readline wrapper, a small utility that uses the GNU readline library to allow the editing of keyboard input for any other command. It maintains a separate input history for each command, and can TAB-expand words using all previously seen words and/or a user-specified file.
endef

PACKAGES = CSWrlwrap

REQUIRED_PKGS  = CSWreadline 

###### Upstream and opencsw files information #######

MASTER_SITES = http://utopia.knoware.nl/~hlub/uck/rlwrap/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += changelog.CSW

# replace setenv with putenv
#PATCHFILES += putenv.patch

##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# the putenv patch modify configure.ac so we must re-generate configure
pre-configure:
		cd $(WORKSRC) && autoconf

post-merge:
	        @ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(GARNAME)/changelog.CSW
	        @( for FILE in AUTHORS BUGS INSTALL NEWS README TODO; do \
	                 ginstall -D $(WORKSRC_FIRSTMOD)/$$FILE $(PKGROOT)$(docdir)/$(GARNAME)/`basename $$FILE`; \
	         done )

