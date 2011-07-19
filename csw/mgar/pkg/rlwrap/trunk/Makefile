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

NAME = rlwrap
VERSION = 0.37
CATEGORIES = utils

DESCRIPTION = A readline wrapper
define BLURB
  rlwrap is a readline wrapper, a small utility that uses the GNU readline library to allow the editing of keyboard input for any other command. It maintains a separate input history for each command, and can TAB-expand words using all previously seen words and/or a user-specified file.
endef

PACKAGES = CSWrlwrap

RUNTIME_DEP_PKGS  = CSWlibreadline6

# We don't want to depend on OpenCSW perl
CHECKPKG_OVERRIDES_CSWrlwrap += missing-dependency|CSWperl

# Reference to default paths in documentation or sample files, can be safely ignored
CHECKPKG_OVERRIDES_CSWrlwrap += file-with-bad-content|/usr/share|root/opt/csw/share/rlwrap/filters/paint_prompt
CHECKPKG_OVERRIDES_CSWrlwrap += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rlwrap/NEWS


###### Upstream and opencsw files information #######

MASTER_SITES = http://utopia.knoware.nl/~hlub/uck/rlwrap/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(NAME)-$(VERSION).tar.gz
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
	        @ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(NAME)/changelog.CSW
	        @( for FILE in AUTHORS BUGS INSTALL NEWS README TODO; do \
	                 ginstall -D $(WORKSRC_FIRSTMOD)/$$FILE $(PKGROOT)$(docdir)/$(NAME)/`basename $$FILE`; \
	         done )

