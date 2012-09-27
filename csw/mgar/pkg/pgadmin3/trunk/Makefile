# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pgadmin3
VERSION = 1.16.0
CATEGORIES = apps
GARTYPE = v2
GARCOMPILER = SOS12U1
LICENSE = LICENSE

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = An administration and development platform for PostgreSQL
define BLURB
endef

SPKG_SOURCEURL = http://www.pgadmin.org/
MASTER_SITES = http://ftp.postgresql.org/pub/pgadmin3/release/v$(VERSION)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += changelog.CSW
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Ignore them for now
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/zh_TW/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/cs_CZ/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/zh_CN/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/sl_SI/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/es_ES/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/fi_FI/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/de_DE/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/en_US/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/fr_FR/hints/instrumentation.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/en_US/extend.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/local|root/opt/csw/share/pgadmin3/docs/en_US/pgagent-install.html
CHECKPKG_OVERRIDES_CSWpgadmin3 += file-with-bad-content|/usr/share|root/opt/csw/share/pgadmin3/docs/en_US/pgagent-install.html

RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpgadmin3 += CSWlibpq5

BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWpostgresql-dev
BUILD_DEP_PKGS += CSWwxwidgetsdevel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pgsql=$(prefix)
CONFIGURE_ARGS += --with-libxml2=$(prefix)
CONFIGURE_ARGS += --with-libxslt=$(prefix)

EXTRA_CXXFLAGS += -norunpath
include gar/category.mk
