# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = unixodbc
GARVERSION = 2.2.14
CATEGORIES = lib

DESCRIPTION = ODBC drivers for Unix systems
define BLURB
  It does stuff with things
endef
DL_NAME = unixODBC
MASTER_SITES = http://www.unixodbc.org/
DISTFILES  = $(DL_NAME)-$(GARVERSION).tar.gz
# The configuration migratin is pending decision.
# DISTFILES += CSWunixodbc.postinstall
WORKSRC = $(WORKDIR)/$(DL_NAME)-$(GARVERSION)
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS  = CSWiconv
REQUIRED_PKGS += CSWreadline
sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS) --enable-gui=no
BUILD64 = 1
SAMPLECONF = /\/etc\/opt\/csw\/.*\.CSW
TEST_SCRIPTS =

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for f in ODBCDataSources odbc.ini odbcinst.ini; do \
		mv "$${f}" "$${f}.CSW"; \
	done)
	@$(MAKECOOKIE)

include gar/category.mk
