NAME = pangomm
VERSION = 2.28.4
GARTYPE = v2

DESCRIPTION = C++ interface to pango
define BLURB
endef

MASTER_SITES += $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz

PACKAGES += CSWlibpangomm1-4-1
SPKG_DESC_CSWlibpangomm1-4-1 = C++ interface to Pango
PKGFILES_CSWlibpangomm1-4-1 += $(call pkgfiles_lib,libpangomm-1.4.so.1)
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibcairomm1-0-1
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibglibmm2-4-1
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWpango
RUNTIME_DEP_PKGS_CSWlibpangomm1-4-1 += CSWlibgcc-s1

PACKAGES += CSWlibpangomm-dev
SPKG_DESC_CSWlibpangomm-dev = Development files for libpangomm-1.4.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpangomm-dev += CSWlibpangomm1-4-1

GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

include gar/category.mk
