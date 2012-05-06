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
PATCHFILES += 0002-If-reviter-is-unavailable-don-t-test-for-it.patch

CONFIGURE_ARGS = $(DIRPATHS)

# The tests require a running PostgreSQL server.
SKIPTEST = 1

include gar/category.mk

