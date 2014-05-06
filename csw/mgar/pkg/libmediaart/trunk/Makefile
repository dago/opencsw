# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmediaart
VERSION = 0.1.0
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

PATCHFILES += eba1a1f1276e40b68e7b7084863469a0c97ef41a.patch

PACKAGES += CSWlibmediaart0-2-0
CATALOGNAME_CSWlibmediaart0-2-0 = libmediaart0_2_0
SPKG_DESC_CSWlibmediaart0-2-0 += $(DESCRIPTION), libmediaart-0.2.so.0
PKGFILES_CSWlibmediaart0-2-0 += $(call baseisadirs,$(libdir),libmediaart-0\.2\.so\.0\.100\.0)
PKGFILES_CSWlibmediaart0-2-0 += $(call baseisadirs,$(libdir),libmediaart-0\.2\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_sparc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_sparc += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_sparc += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0 += $(RUNTIME_DEP_PKGS_CSWlibmediaart0-2-0_$(GARCH))
RUNTIME_DEP_PKGS_CSWlibmediaart-dev += CSWlibmediaart0-2-0

PACKAGES += CSWlibmediaart-dev
SPKG_DESC_CSWlibmediaart-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibmediaart-dev = $(PKGFILES_DEVEL)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

