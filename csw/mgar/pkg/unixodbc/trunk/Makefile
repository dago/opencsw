# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = unixodbc
GARVERSION = 2.2.14
CATEGORIES = lib

DESCRIPTION = ODBC drivers for Unix systems
define BLURB
endef
DL_NAME = unixODBC
MASTER_SITES = http://www.unixodbc.org/
DISTFILES  = $(DL_NAME)-$(GARVERSION).tar.gz
DISTFILES += cswmigrateconf
WORKSRC = $(WORKDIR)/$(DL_NAME)-$(GARVERSION)
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS  = CSWiconv
REQUIRED_PKGS += CSWreadline
sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS) --enable-gui=no
BUILD64 = 1
SAMPLECONF = \/etc\/opt\/csw\/odbc(inst|).ini
MIGRATECONF = \/etc\/opt\/csw\/pkg\/$(GARNAME)\/cswmigrateconf
TEST_SCRIPTS =

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for f in odbc.ini odbcinst.ini; do \
		mv "$${f}" "$${f}.CSW"; \
	done)
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/pkg/$(GARNAME)
	ginstall -m 644 $(FILEDIR)/cswmigrateconf $(DESTDIR)$(sysconfdir)/pkg/$(GARNAME)
	@$(MAKECOOKIE)

include gar/category.mk
