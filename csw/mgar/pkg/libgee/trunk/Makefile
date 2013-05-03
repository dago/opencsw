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
DISTFILES  = $(NAME)-$(VERSION).tar.xz
GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWvala CSWpkgconfig CSWglib2devel
RUNTIME_DEP_PKGS += CSWglib2

PACKAGES += CSWlibgee2
SPKG_DESC_CSWlibgee2 = $(DESCRIPTION), library
PKGFILES_CSWlibgee2 += $(call pkgfiles_lib,libgee.so)

PACKAGES += CSWlibgee-dev
SPKG_DESC_CSWlibgee-dev = $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibgee-dev += CSWlibgee2
PKGFILES_CSWlibgee-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibgee-dev += $(call baseisadirs,$(datadir),vala/vapi/gee-1\.0\.vapi)
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

