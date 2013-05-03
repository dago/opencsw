# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libgee
# 0.6.8 is the latest version who's pkg-config name is gee-1.0, dconf depends on gee-1.0
VERSION = 0.6.8
GARTYPE = v2

DESCRIPTION = GObject collection library
define BLURB
  GObject collection library
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWvala
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWglib2devel

RUNTIME_DEP_PKGS += CSWglib2

PACKAGES += CSWlibgee2
SPKG_DESC_CSWlibgee2 = $(DESCRIPTION), library
PKGFILES_CSWlibgee2 += $(call pkgfiles_lib,libgee.so)

PACKAGES += CSWlibgee-dev
SPKG_DESC_CSWlibgee-dev = $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibgee-dev += CSWlibgee2
# PKGFILES is catchall

CONFIGURE_ARGS = $(DIRPATHS)

# Testsuite runs 10 mins, please SKIPTEST as needed

include gar/category.mk
