# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pgadmin3
GARVERSION = 1.10.0
CATEGORIES = apps
DESCRIPTION = An administration and development platform for PostgreSQL
define BLURB
endef
SPKG_SOURCEURL = http://www.pgadmin.org/
MASTER_SITES = http://wwwmaster.postgresql.org/redir/76/h/pgadmin3/release/v$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS += CSWpostgresql
REQUIRED_PKGS += CSWkrb5lib
REQUIRED_PKGS += CSWlibpq
REQUIRED_PKGS += CSWlibxml2
REQUIRED_PKGS += CSWlibxslt
REQUIRED_PKGS += CSWosslrt
REQUIRED_PKGS += CSWwxwidgetscommon
REQUIRED_PKGS += CSWwxwidgetsgtk2
REQUIRED_PKGS += CSWzlib
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWwxwidgetsdevel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
