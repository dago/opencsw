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
WORKSRC = $(WORKDIR)/$(DL_NAME)-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES = none cswcpsampleconf

REQUIRED_PKGS  = CSWiconv
REQUIRED_PKGS += CSWreadline
REQUIRED_PKGS += CSWcswclassutils

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)  --enable-gui=no
BUILD64 = 1

PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/etc\/opt\/csw\/.*\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
    { print }'


TEST_SCRIPTS =

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for f in ODBCDataSources odbc.ini odbcinst.ini; do \
		mv "$${f}" "$${f}.CSW"; \
	done)
	@$(MAKECOOKIE)


include gar/category.mk
