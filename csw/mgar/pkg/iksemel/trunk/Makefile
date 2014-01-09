# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = iksemel
VERSION = 1.4
GARTYPE = v2

DESCRIPTION = Fast and portable XML parser and Jabber protocol library

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Adjust-alignment.patch

PACKAGES += CSWlibiksemel3
SPKG_DESC_CSWlibiksemel3 = Fast and portable XML parser and Jabber protocol library, libiksemel.so.3
PKGFILES_CSWlibiksemel3 += $(call pkgfiles_lib,libiksemel.so.3)

PACKAGES += CSWlibiksemel-dev
SPKG_DESC_CSWlibiksemel-dev = Development files for libiksemel.so.3
PKGFILES_CSWlibiksemel-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibiksemel-dev += CSWlibiksemel3

PACKAGES += CSWiksemel
SPKG_DESC_CSWiksemel = Jabber protocol utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWiksemel += CSWlibiksemel3

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

