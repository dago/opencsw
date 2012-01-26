# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = nxcl
VERSION = 0.9
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A library for the Free NX client
define BLURB
  A library for NX clients.
endef

DL_NAME = freenx-client
WORKSRC = $(WORKDIR)/$(DL_NAME)-$(VERSION)/nxcl

docdir = $(datadir)/doc

PATCHFILES = doc-$(VERSION).patch

MASTER_SITES = http://download.berlios.de/freenx/
DISTFILES  = $(DL_NAME)-$(VERSION).tar.bz2
DISTFILES += $(PATCHFILES)


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS  = CSWautoconf CSWautomake CSWlibtool
BUILD_DEP_PKGS += CSWdoxygen CSWspeex

CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)
TEST_SCRIPTS =

pre-configure-modulated:
	(cd $(WORKSRC); autoreconf -fi)
	@$(MAKECOOKIE)

include gar/category.mk
