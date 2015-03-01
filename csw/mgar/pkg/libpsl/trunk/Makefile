# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libpsl
VERSION = 0.7.1
GARTYPE = v2

DESCRIPTION = Provides functions to check domains against the Mozilla Public Suffix List

MASTER_SITES += https://github.com/rockdaboot/libpsl/releases/download/$(DISTNAME)/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibpsl0
SPKG_DESC_CSWlibpsl0 = Public Suffix List library, libpsl.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpsl0 += CSWlibicuuc54

PACKAGES += CSWlibpsl-dev
SPKG_DESC_CSWlibpsl-dev = Development files for libpsl.so.0
PKGFILES_CSWlibpsl-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpsl-dev += $(bindir)/.*
RUNTIME_DEP_PKGS_CSWlibpsl-dev += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibpsl-dev += CSWlibpsl0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

# This is needed for sha1sum
BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk
