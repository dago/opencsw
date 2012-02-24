# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = celt
VERSION = 0.11.1
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = The CELT ultra-low delay audio codec
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/celt/
DISTFILES  = $(DISTNAME).tar.gz

# Solaris 9 is lacking getopt_long
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibogg-dev

PACKAGES += CSWlibcelt0-2
SPKG_DESC_CSWlibcelt0-2 = The CELT ultra-low delay audio codec library, libcelt0.so.2
PKGFILES_CSWlibcelt0-2 += $(call pkgfiles_lib,libcelt0.so.2)
RUNTIME_DEP_PKGS_CSWcelt += CSWlibogg0

PACKAGES += CSWlibcelt0-dev
SPKG_DESC_CSWlibcelt0-dev = Development files for libcelt0.so.2
PKGFILES_CSWlibcelt0-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibcelt0-dev += CSWlibcelt0-2

PACKAGES += CSWcelt
SPKG_DESC_CSWcelt = The CELT ultra-low delay audio codec utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcelt += CSWlibcelt0-2

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

