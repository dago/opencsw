# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmediaart
VERSION = 0.6.0
GARTYPE = v2

DESCRIPTION = Libmediaart, manage, extract and handle media art caches
define BLURB
    Library tasked with managing, extracting and handling media art caches.
  The code for this project has been extracted from Tracker and inserted
  into its own library because there is call for this functionality in
  other places on the desktop.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
GARCOMPILER = GNU
# Tests fail left and right
SKIPTEST = 1

PACKAGES += CSWlibmediaart1-0-0
CATALOGNAME_CSWlibmediaart1-0-0 = libmediaart1_0_0
SPKG_DESC_CSWlibmediaart1-0-0 += $(DESCRIPTION), libmediaart-1.0.so.0
PKGFILES_CSWlibmediaart1-0-0 += $(call baseisadirs,$(libdir),libmediaart-1\.0\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0 += $(RUNTIME_DEP_PKGS_CSWlibmediaart1-0-0_$(GARCH))
RUNTIME_DEP_PKGS_CSWlibmediaart-dev += CSWlibmediaart1-0-0

PACKAGES += CSWlibmediaart-dev
SPKG_DESC_CSWlibmediaart-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibmediaart-dev = $(PKGFILES_DEVEL)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

