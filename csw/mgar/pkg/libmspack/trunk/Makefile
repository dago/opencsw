# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmspack
VERSION = 0.3alpha
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A library for Microsoft compression formats
define BLURB
endef

MASTER_SITES = http://www.cabextract.org.uk/libmspack/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-use-gcc-specific-flags.patch

VENDOR_URL = http://www.cabextract.org.uk/libmspack/

LICENSE = COPYING.LIB

PACKAGES += CSWlibmspack0
SPKG_DESC_CSWlibmspack0 = A library for Microsoft compression formats, libmspack.so.0
PKGFILES_CSWlibmspack0 += $(call pkgfiles_lib,libmspack.so.0)

PACKAGES += CSWlibmspack-dev
SPKG_DESC_CSWlibmspack-dev = Development files for libmspack.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmspack-dev += CSWlibmspack0

# For __FUNCTION__
EXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__

BUILD64 = 1

include gar/category.mk

