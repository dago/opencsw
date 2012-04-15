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

PACKAGES = CSWlibsigc2-0-0
SPKG_DESC_CSWlibsigc2-0-0 = Typesafe signal and callback system for C++, libsigc-2.0.so.0
PKGFILES_CSWlibsigc2-0-0 += $(call pkgfiles_lib,libsigc-2.0.so.0)
OBSOLETED_BY_CSWlibsigc2-0-0 = CSWlibsigc++
# CSWsigc++ is the previous package name
INCOMPATIBLE_PKGS_CSWlibsigc++ = CSWsigc++

PACKAGES += CSWlibsigc-dev
SPKG_DESC_CSWlibsigc-dev = Header files for libsigc-2.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsigc-dev = CSWlibsigc2-0-0
OBSOLETED_BY_CSWlibsigc-dev = CSWlibsigc++devel
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel_stub

BUILD64_LIBS_ONLY = 1
EXTRA_CXXFLAGS += -norunpath
EXTRA_CONFIGURE_ENV = MAKE=gmake
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

# Do not strip -norunpath during libtool invocation
REINPLACE_MATCH = (\|-xarch=)
REINPLACE_WITH = |-norunpath$$1
REINPLACE_FILES = build/ltmain.sh

include gar/category.mk
