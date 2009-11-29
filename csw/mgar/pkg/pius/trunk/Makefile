# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pius
GARVERSION = 2.0.3
CATEGORIES = apps
DESCRIPTION = A tool for signing and email all UIDs on a set of PGP keys.
define BLURB
endef
SPKG_SOURCEURL = http://www.phildev.net/pius/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = pgpius
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
REQUIRED_PKGS = CSWpython
ARCHALL = 1
PREREQUISITE_PKGS = $(REQUIRED_PKGS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = pius
TEST_SCRIPTS =

include gar/category.mk

install-pius:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/pius $(DESTDIR)$(bindir)
	ginstall -m 755 -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(datadir)/doc/$(GARNAME)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
