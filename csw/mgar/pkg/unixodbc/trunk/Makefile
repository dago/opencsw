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
RUNTIME_DEP_PKGS_CSWunixodbc += CSWiconv
RUNTIME_DEP_PKGS_CSWunixodbc += CSWreadline
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbcinst1
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbc1
sysconfdir = /etc$(prefix)
localstatedir = /var$(prefix)
CONFIGURE_ARGS = $(DIRPATHS) --enable-gui=no
BUILD64 = 1
SAMPLECONF = \/etc\/opt\/csw\/odbc(inst|).ini
MIGRATECONF = \/etc\/opt\/csw\/pkg\/$(NAME)\/cswmigrateconf
TEST_SCRIPTS =
LICENSE = COPYING

PACKAGES += CSWunixodbc
SPKG_DESC_CSWunixodbc = $(DESCRIPTION)

PACKAGES += CSWunixodbc-dev
CATALOGNAME_CSWunixodbc-dev = unixodbc_dev
SPKG_DESC_CSWunixodbc-dev = $(DESCRIPTION), development files
PKGFILES_CSWunixodbc-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbc1
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbccr1
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbcinst1

PACKAGES += CSWlibodbc1
SPKG_DESC_CSWlibodbc1 = $(DESCRIPTION), libodbc.so.1
PKGFILES_CSWlibodbc1 = .*libodbc\.so\.1.*
RUNTIME_DEP_PKGS_CSWlibodbc1 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibodbc1 += CSWiconv

PACKAGES += CSWlibodbccr1
SPKG_DESC_CSWlibodbccr1 = $(DESCRIPTION), libodbccr.so.1
PKGFILES_CSWlibodbccr1 = .*libodbccr\.so\.1.*

PACKAGES += CSWlibodbcinst1
SPKG_DESC_CSWlibodbcinst1 = $(DESCRIPTION), libodbcinst.so.1
PKGFILES_CSWlibodbcinst1 = .*libodbcinst\.so\.1.*
RUNTIME_DEP_PKGS_CSWlibodbcinst1 += CSWlibltdl7

include gar/category.mk

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for f in odbc.ini odbcinst.ini; do \
		mv "$${f}" "$${f}.CSW"; \
	done)
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/pkg/$(NAME)
	ginstall -m 644 $(FILEDIR)/cswmigrateconf $(DESTDIR)$(sysconfdir)/pkg/$(NAME)
	@$(MAKECOOKIE)
