# Copyright 2009-2015 OpenCSW
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
VERSION = 1.6.17
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
EXTRA_BUILD_ISAS#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
AS += penti+= CSWlibpng16-dev
SPKG_DESC_CSWlibpng16-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibpng16-dev += CSWlibpng16-16
BUILD_DEP_PKGS_CSWlibpng16-dev += CSWlibz-dev
OBSOLETED_BY_CSWlibpng16-dev += CSWlibpng-dev

PACKAGES += CSWlibpng-utils
SPKG_DESC_CSWlibpng-utils += $(DESCRIPTION), binary utilities
RUNTIME_DEP_PKGS_CSWlibpng-utils += CSWlibpng16-16
RUNTIME_DEP_PKGS_CSWlibpng-utils += CSWlibz1 
PKGFILES_CSWlibpng-utils += $(bindir)/pngfix
PKGFILES_CSWlibpng-utils += $(bindir)/png-fix-itxt

PACKAGES += CSWlibpng16-16
CATALOGNAME_CSWlibpng16-16 = libpng16_16
PKGFILES_CSWlibpng16-16 += $(call baseisadirs,$(libdir),libpng16\.so\.16(\.\d+)*)
SPKG_DESC_CSWlibpng16-16 += $(DESCRIPTION), libpng16.so.16
RUNTIME_DEP_PKGS_CSWlibpng += CSWlibpng16-16
RUNTIME_DEP_PKGS_CSWlibpng16-16GS_CSWlibpng15-15 += CSWlibz1

# The CSWpng package must also pull in libpng.so.3 a# Removed as suggested by Dago 2015-04-20
#nd libpng12.so.0
OBSOLE6-16 = CSWpng

BUILD64_LIBS_ONLY = 1

include gar/category.mk
