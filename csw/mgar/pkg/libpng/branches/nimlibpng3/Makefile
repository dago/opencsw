# Copyright 2009 OpenNIMOSS
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# ! The transitional package NIMOSSpng must also pull in libpng.so.3 and
#   libpng12.so.0
# * Would be good to also provide ISAs:
#   sparcv8plus+vis
#   sparcv8plus+vis2
#   pentium_pro

NAME = libpng
VERSION = 1.2.50
CATEGORIES = lib
GARTYPE = bts

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

PACKAGES = NIMOSSlibpng-dev
SPKG_DESC_NIMOSSlibpng-dev = $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_NIMOSSlibpng-dev += NIMOSSlibpng3
RUNTIME_DEP_PKGS_NIMOSSlibpng-dev += NIMOSSlibpng12-0

PACKAGES += NIMOSSlibpng3
CATALOGNAME_NIMOSSlibpng3 = libpng3
PKGFILES_NIMOSSlibpng3 += $(call baseisadirs,$(libdir),libpng\.so\.3(\.\d+)*)
SPKG_DESC_NIMOSSlibpng3 += $(DESCRIPTION), libpng.so.3
RUNTIME_DEP_PKGS_NIMOSSlibpng += NIMOSSlibpng3
OBSOLETED_BY_NIMOSSlibpng3 += NIMOSSpng
RUNTIME_DEP_PKGS_NIMOSSlibpng3 += NIMOSSlibz1

PACKAGES += NIMOSSlibpng12-0
CATALOGNAME_NIMOSSlibpng12-0 = libpng12_0
PKGFILES_NIMOSSlibpng12-0 += $(call baseisadirs,$(libdir),libpng12\.so\.0(\.\d+)*)
SPKG_DESC_NIMOSSlibpng12-0 += $(DESCRIPTION), libpng12.so.0
RUNTIME_DEP_PKGS_NIMOSSlibpng += NIMOSSlibpng12-0
RUNTIME_DEP_PKGS_NIMOSSlibpng12-0 += NIMOSSlibz1
OBSOLETED_BY_NIMOSSlibpng12-0 += NIMOSSpng

BUILD64 = 1

include gar/category.mk
