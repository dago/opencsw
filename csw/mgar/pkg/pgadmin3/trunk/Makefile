# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pgadmin3
VERSION = 1.18.1
GARTYPE = v2COMPILER = SOS12U1
LICENSE = LICENSE

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = An administration and development platform for PostgreSQL
define BLURB
endef

SPKG_SOURCEURL = http://www.pgadmin.org/
MASTER_SITES = http://ftp.postgresql.org/pub/pgadmin3/release/v$(VERSION)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += changelog.CSW
UFILES_REGEX = $(NAME)-(\d+(?RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWwxwidgetsCSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpgadRUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibz1dmin3 += CSWlibpq5

BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWpostgresql-dev
BUILD_DEP_PK-dev CSWwxwidgetsdevel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pgsql=$(prefix)
CONFIGURE_ARGS += --with-libxml2=$(prefix)
CONFIGURE_ARGS += --with-libxslt=$(prefix)

EXTRA_CXXFLAGS += -norunpath
includ