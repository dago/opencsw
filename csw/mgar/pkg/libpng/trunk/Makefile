# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# ! The transitional package CSWpng must also pull in libpng.so.3 and
#   libpng12.so.0
# * Would be good to also provide ISAs:
#   sparcv8plus+vis
#   sparcv8plus+vis2
#   pentium_pro

NAME = libpng
VERSION = 1.5.4
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = The official library for Portable Network Graphics format (PNG)
define BLURB
endef
VENDOR_URL = http://www.libpng.org/pub/png/libpng.html
MASTER_SITES = $(SF_MIRROR)
MASTER_SITES += ftp://ftp.simplesystems.org/pub/libpng/png/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_BUILD_ISAS = sparcv8plus+vis
EXTRA_BUILD_ISAS += sparcv8plus+vis2
EXTRA_BUILD_ISAS += pentium_pro

PACKAGES = CSWlibpng-dev
SPKG_DESC_CSWlibpng-dev = $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibpng-dev += CSWlibpng15-15

PACKAGES += CSWlibpng15-15
CATALOGNAME_CSWlibpng15-15 = libpng15_15
PKGFILES_CSWlibpng15-15 += $(call baseisadirs,$(libdir),libpng15\.so\.15(\.\d+)*)
SPKG_DESC_CSWlibpng15-15 += $(DESCRIPTION), libpng15.so.15
RUNTIME_DEP_PKGS_CSWlibpng += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpng15-15 += CSWlibz1

# The CSWpng package must also pull in libpng.so.3 and libpng12.so.0
OBSOLETED_BY_CSWlibpng15-15 = CSWpng

BUILD64_LIBS_ONLY = 1

include gar/category.mk
