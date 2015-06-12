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
VERSION = 1.5.22
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = The official library for Portable Network Graph
MASTER_SITES +tml
MASTER_SITES = $(SF_MIRROR)
MASTER_SITES += ftp://ftp.simplesystems.org/pub/libpng/pn+= $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.libpng.org/pub/png/libpng.html
LICENSE = LICENSE

EXTRA_BUILD_ISAS += sparcv8plus+vis
EXTRA_BUILD_ISAS += sparcv8plus+vis2AS#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
AS#we need a versioned developer package, since the pkg-config package is versioned 
#and has an unversioned symlink
PACKAGES = CSWlibpng15-dev
SPKG_DESC_CSWlibpng15-dev = $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibpng15-dev += CSWlibpng15-15

#we package in only certain versioned files
PKGFILES_CSWlibpng15-dev += $(call baseisadirs,$(libdir),libpng15-config)
PKGFILES_CSWlibpng15-dev += $(call baseisadirs,$(libdir),pkgconfig/libpng15.pc)
PKGFILES_CSWlibpng15-dev += $(call baseisadirs,$(libdir),include/libpng16/*)

#we obsolete the unversioned developer package
OBSOLETED_BY_CSWlibpng15-dev = CSWlibpng-dev+= CSWlibpng15-15

PACKAGES += CSWlibpng15-15
CATALOGNAME_CSWlibpng15-15 = libpng15_15
PKGFILES_CSWlibpng15-15 += $(call baseisadirs,$(libdir),libpng15\.so\.15(\.\d+)*)
SPKG_DESC_CSWlibpng15-15 += $(DESCRIPTION), libpng15.so.15
RUNTIME_DEP_PKGS_CSWlibpng += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpng15
BUILD64_LIBS_ONLY = 1

CHECKPKG_OVERRIDES_CSWlibpng15-dev += surplus-dependency|CSWlibpng15-15

include gar/category.mk

