# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libpqxx
VERSION = 4.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = C++ client API for PostgreSQL
define BLURB
endef

MASTER_SITES = http://pqxx.org/download/software/libpqxx/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS = CSWpostgresql-dev

PATCHFILES += 0001-Can-t-instantiate-a-const_reverse_iterator.patch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

