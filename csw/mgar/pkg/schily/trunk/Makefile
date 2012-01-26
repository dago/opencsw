# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = schily
VERSION = 2011-08-29
CATEGORIES = lib
GARTYPE = v2
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
BUILD_ARGS  = INS_BASE=$(INS_BASE)
BUILD_ARGS += INS_RBASE=$(INS_RBASE)
BUILD_ARGS += LINKMODE=dynamic

include gar/category.mk

PATH := /usr/ccs/bin:/usr/bin:/opt/csw/bin

build-custom:
	(cd $(WORKSRC) && /usr/bin/env -i PATH=$(PATH) /opt/csw/bin/smake $(BUILD_ARGS))
	@$(MAKECOOKIE)

install-custom:
	(cd $(WORKSRC) && /usr/bin/env -i PATH=$(PATH) /opt/csw/bin/smake $(BUILD_ARGS) install)
	@$(MAKECOOKIE)
