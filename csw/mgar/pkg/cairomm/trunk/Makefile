NAME = cairomm
VERSION = 1.10.0
GARTYPE = v2

DESCRIPTION  = C++ bindings for Cairo
define BLURB
endef

MASTER_SITES += http://www.cairographics.org/releases/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibcairomm1-0-1
SPKG_DESC_CSWlibcairomm1-0-1 = C++ bindings for Cairo
PKGFILES_CSWlibcairomm1-0-1 += $(call pkgfiles_lib,libcairomm-1.0.so.1)
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibcairomm1-0-1 += CSWlibgcc-s1

PACKAGES += CSWlibcairomm-dev
SPKG_DESC_CSWlibcairomm-dev = Development files for libcairo-1.0.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS += CSWlibcairomm1-0-1

GARCOMPILER = GNU

BUILD64 = 1

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

include gar/category.mk


