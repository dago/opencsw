# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = giblib
VERSION = 1.2.4

DESCRIPTION = A library wrapper to imlib2

MASTER_SITES = http://linuxbrit.co.uk/downloads/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-add-Wall.patch

VENDOR_URL = http://freecode.com/projects/giblib

BUILD_DEP_PKGS += CSWimlib2

PACKAGES += CSWlibgiblib1
SPKG_DESC_CSWlibgiblib1 = A library wrapper to imlib2, libgiblib.so.1
PKGFILES_CSWlibgiblib1 += $(call pkgfiles_lib,libgiblib.so.1)
RUNTIME_DEP_PKGS_CSWlibgiblib1 += CSWimlib2

PACKAGES += CSWlibgiblib-dev
SPKG_DESC_CSWlibgiblib-dev = Development files for libgiblib.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgiblib-dev += CSWlibgiblib1

include gar/category.mk

