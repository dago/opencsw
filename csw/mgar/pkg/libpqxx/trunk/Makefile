# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libpqxx
VERSION = 5.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = C++ client API for PostgreSQL
define BLURB
endef

# Daily dev snapshots
MASTER_SITES = http://pqxx.org/~jtv/tmp/pqxx/snapshot/

# Official download site
# MASTER_SITES = http://pqxx.org/download/software/libpqxx/

DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS = CSWpostgresql-dev

PATCHFILES += 0001-Can-t-instantiate-a-const-iterator-from-non-const.patch
PATCHFILES += 0002-Don-t-test-for-reverse-iters-if-they-re-not-there.patch

# Tests require a running server, which we won't have.
SKIPTEST = 1

EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += --enable-static=no

PACKAGES += CSWlibpqxx5-0
CATALOGNAME_CSWlibpqxx5-0 = libpqxx5_0
PKGFILES_CSWlibpqxx5-0 += $(call baseisadirs,$(libdir),libpqxx-5\.0\.so(\.\d+)*)
SPKG_DESC_CSWlibpqxx5-0 += $(DESCRIPTION), libpqxx-5.0.so
RUNTIME_DEP_PKGS_CSWlibpqxx5-0 += CSWlibpq5
# This is a retarded way to name shared libraries. Some projects still do it.
CHECKPKG_OVERRIDES_CSWlibpqxx5-0 += soname-equals-filename|file=/opt/csw/lib/libpqxx-5.0.so
# The 'EXTRA_LINKER_FLAGS = -norunpath' bit doesn't work.
CHECKPKG_OVERRIDES_CSWlibpqxx5-0 += bad-rpath-entry

PACKAGES += CSWlibpqxx-dev
SPKG_DESC_CSWlibpqxx-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibpqxx-dev += CSWlibpqxx5-0
INCOMPATIBLE_PKGS_CSWlibpqxx-dev = CSWlibpqxx

include gar/category.mk
