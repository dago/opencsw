# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = schily
VERSION = 2011-08-29
CATEGORIES = lib
DESCRIPTION = Software by Joerg Shilling
define BLURB
endef
SPKG_SOURCEURL =
MASTER_SITES = ftp://ftp.berlios.de/pub/schily/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
BUILD_DEP_PKGS = CSWsmake
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =
INS_BASE = $(BUILD_PREFIX)
INS_RBASE = $(BUILD_PREFIX)
EXTRA_COMMON_EXPORTS = INS_BASE INS_RBASE
# Shared libraries don't work at the moment.
# LINKMODE = dynamic
# EXTRA_COMMON_EXPORTS += LINKMODE
BUILD_ARGS = INS_BASE=$(INS_BASE) INS_RBASE=$(INS_RBASE)

include gar/category.mk

build-custom:
	(cd $(WORKSRC) && smake $(BUILD_ARGS))
	@$(MAKECOOKIE)

install-custom:
	(cd $(WORKSRC) && smake $(BUILD_ARGS) install)
	@$(MAKECOOKIE)
