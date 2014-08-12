# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libuuid
VERSION = 1.0.2
GARTYPE = v2

DESCRIPTION = Portable uuid C library

MASTER_SITES += $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# Use patches until this is merged:
#   https://sourceforge.net/p/libuuid/code/merge-requests/1/
PATCHFILES += 0001-Use-inttypes.h-if-stdint.h-is-not-available.patch
PATCHFILES += 0002-Do-not-use-_SC_HOST_NAME_MAX-if-not-available.patch

# This is an optional lib for wget which we need for pkgutil and GAR
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWlibuuid1
SPKG_DESC_CSWlibuuid1 = Portable uuid C library, libuuid.so.1
PKGFILES_CSWlibuuid1 += $(call pkgfiles_lib,libuuid.so.1)

PACKAGES += CSWlibuuid-dev
SPKG_DESC_CSWlibuuid-dev = Development files for libuuid.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibuuid-dev += CSWlibuuid1

BUILD64 = 1

include gar/category.mk

post-patch:
	cd $(WORKSRC) && autoreconf
	@$(MAKECOOKIE)
