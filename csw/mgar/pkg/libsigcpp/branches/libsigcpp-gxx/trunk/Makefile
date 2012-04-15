# $Id$
NAME = libsigc++
VERSION = 2.2.10
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz

PACKAGES = CSWlibsigc2-0-0-gxx
SPKG_DESC_CSWlibsigc2-0-0-gxx = Typesafe signal and callback system for C++, libsigc-2.0.so.0
PKGFILES_CSWlibsigc2-0-0-gxx += $(call pkgfiles_lib,libsigc-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibsigc2-0-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsigc2-0-0-gxx += CSWlibstdc++6

PACKAGES += CSWlibsigc-gxx-dev
SPKG_DESC_CSWlibsigc-gxx-dev = Header files for libsigc-2.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsigc-gxx-dev += CSWlibsigc2-0-0-gxx

prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1
EXTRA_CONFIGURE_ENV = MAKE=gmake
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

include gar/category.mk
