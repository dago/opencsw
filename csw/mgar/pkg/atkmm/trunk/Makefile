NAME = atkmm
VERSION = 2.22.7
GARTYPE = v2

DESCRIPTION  = C++ bindings for ATK
define BLURB
endef

MASTER_SITES += $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz

PACKAGES += CSWlibatkmm1-6-1
SPKG_DESC_CSWlibatkmm1-6-1 = C++ bindings for ATK
PKGFILES_CSWlibatkmm1-6-1 += $(call pkgfiles_lib,libatkmm-1.6.so.1)
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibglibmm2-4-1
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibatkmm1-6-1 += CSWlibatk1-0-0
# Problematic -z ignore between sparc/i386
CHECKPKG_OVERRIDES_CSWlibatkmm1-6-1 += surplus-dependency|CSWlibintl8

PACKAGES += CSWlibatkmm-dev
SPKG_DESC_CSWlibatkmm-dev = Development files for libatkmm-1.6.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibatkmm-dev += CSWlibatkmm1-6-1

GARCOMPILER = GNU

BUILD64 = 1

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

include gar/category.mk


