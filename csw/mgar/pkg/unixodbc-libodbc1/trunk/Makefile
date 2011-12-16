# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = unixodbc
VERSION = 2.3.0
CATEGORIES = lib

DESCRIPTION = ODBC drivers for Unix systems
define BLURB
endef

MASTER_SITES = http://www.unixodbc.org/

DISTNAME = unixODBC-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

PACKAGES += CSWunixodbc
SPKG_DESC_CSWunixodbc = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbcinst1
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbc1

PACKAGES += CSWunixodbc-dev
CATALOGNAME_CSWunixodbc-dev = unixodbc_dev
SPKG_DESC_CSWunixodbc-dev = Development files for libodbc*.so.1
PKGFILES_CSWunixodbc-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWunixodbc-dev += $(call baseisadirs,$(bindir),odbc_config)
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbc1
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbccr1
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbcinst1

PACKAGES += CSWlibodbc1
SPKG_DESC_CSWlibodbc1 = $(DESCRIPTION), libodbc.so.1
PKGFILES_CSWlibodbc1 += $(call pkgfiles_lib,libodbc.so.1)
PKGFILES_CSWlibodbc1 += $(sysconfdir)/.*
RUNTIME_DEP_PKGS_CSWlibodbc1 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibodbc1 += CSWlibiconv2

PACKAGES += CSWlibodbccr1
SPKG_DESC_CSWlibodbccr1 = $(DESCRIPTION), libodbccr.so.1
PKGFILES_CSWlibodbccr1 += $(call pkgfiles_lib,libodbccr.so.1)

PACKAGES += CSWlibodbcinst1
SPKG_DESC_CSWlibodbcinst1 = $(DESCRIPTION), libodbcinst.so.1
PKGFILES_CSWlibodbcinst1 += $(call pkgfiles_lib,libodbcinst.so.1)
RUNTIME_DEP_PKGS_CSWlibodbcinst1 += CSWlibltdl7

BUILD64 = 1
CONFIGURE_ARGS += $(DIRPATHS)

PRESERVECONF += $(sysconfdir)/odbc.ini
PRESERVECONF += $(sysconfdir)/odbcinst.ini

MIGRATE_FILES_CSWunixodbc += odbc.ini
MIGRATE_FILES_CSWunixodbc += odbcinst.ini
MIGRATE_FILES_CSWunixodbc += ODBCDataSources

include gar/category.mk
