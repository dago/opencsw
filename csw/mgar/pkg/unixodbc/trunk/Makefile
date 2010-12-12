# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = unixodbc
VERSION = 2.3.0
CATEGORIES = lib

DESCRIPTION = ODBC drivers for Unix systems
define BLURB
endef
DL_NAME = unixODBC
MASTER_SITES = http://www.unixodbc.org/
DISTNAME = $(DL_NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += cswmigrateconf
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*).tar.gz
RUNTIME_DEP_PKGS_CSWunixodbc  = CSWiconv
RUNTIME_DEP_PKGS_CSWunixodbc += CSWreadline
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibtoolrt
sysconfdir = /etc$(prefix)
localstatedir = /var$(prefix)
CONFIGURE_ARGS = $(DIRPATHS) --enable-gui=no
BUILD64 = 1
SAMPLECONF = \/etc\/opt\/csw\/odbc(inst|).ini
MIGRATECONF = \/etc\/opt\/csw\/pkg\/$(NAME)\/cswmigrateconf
TEST_SCRIPTS =
LICENSE = COPYING

include gar/category.mk

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for f in odbc.ini odbcinst.ini; do \
		mv "$${f}" "$${f}.CSW"; \
	done)
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/pkg/$(NAME)
	ginstall -m 644 $(FILEDIR)/cswmigrateconf $(DESTDIR)$(sysconfdir)/pkg/$(NAME)
	@$(MAKECOOKIE)
