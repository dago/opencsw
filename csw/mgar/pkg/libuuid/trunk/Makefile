# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libuuid
VERSION = 1.0.2
GARTYPE = v2

DESCRIPTION = Portable uuid C library

MASTER_SITES += $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibuuid1
SPKG_DESC_CSWlibuuid1 = Portable uuid C library, libuuid.so.1
PKGFILES_CSWlibuuid1 += $(call pkgfiles_lib,libuuid.so.1)

PACKAGES += CSWlibuuid-dev
SPKG_DESC_CSWlibuuid-dev = Development files for libuuid.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibuuid-dev += CSWlibuuid1

BUILD64 = 1

include gar/category.mk

