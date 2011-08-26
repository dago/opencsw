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
VERSION = 1.2.46
CATEGORIES = lib
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
RUNTIME_DEP_PKGS_CSWlibpng-dev += CSWlibpng3
RUNTIME_DEP_PKGS_CSWlibpng-dev += CSWlibpng12-0

PACKAGES += CSWlibpng3
CATALOGNAME_CSWlibpng3 = libpng3
PKGFILES_CSWlibpng3 += $(call baseisadirs,$(libdir),libpng\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibpng3 += $(DESCRIPTION), libpng.so.3
RUNTIME_DEP_PKGS_CSWlibpng += CSWlibpng3
OBSOLETED_BY_CSWlibpng3 += CSWpng
RUNTIME_DEP_PKGS_CSWlibpng3 += CSWlibz1

PACKAGES += CSWlibpng12-0
CATALOGNAME_CSWlibpng12-0 = libpng12_0
PKGFILES_CSWlibpng12-0 += $(call baseisadirs,$(libdir),libpng12\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpng12-0 += $(DESCRIPTION), libpng12.so.0
RUNTIME_DEP_PKGS_CSWlibpng += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibpng12-0 += CSWlibz1
OBSOLETED_BY_CSWlibpng12-0 += CSWpng

BUILD64 = 1

include gar/category.mk
