# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pgadmin3
VERSION = 1.10.0
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = An administration and development platform for PostgreSQL
define BLURB
endef
SPKG_SOURCEURL = http://www.pgadmin.org/
MASTER_SITES = http://wwwmaster.postgresql.org/redir/76/h/pgadmin3/release/v$(VERSION)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
RUNTIME_DEP_PKGS += CSWpostgresql
RUNTIME_DEP_PKGS += CSWkrb5lib
RUNTIME_DEP_PKGS += CSWlibpq
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWlibxslt
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWwxwidgetscommon
RUNTIME_DEP_PKGS += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS += CSWzlib
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWwxwidgetsdevel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
