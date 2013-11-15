# $Id$
NAME = libsigc++
VERSION = 2.2.11
GARTYPE = v2
GARCOMPILER = GNU lib
GARTYPE = v2

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz

PACKAGES = CSWlibsigc2-0-0
SPKG_DESC_CSWlibsigc2-0-0 = Typesafe signal and callback system for C++, libsigc-2.0.so.0
PKGFILES_CSWlibsigc2-0-0 += $(call pkgfiles_lib,lRUNTIME_DEP_PKGS_CSWlibsigc2-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsigc2-0-0 += CSWlibstdc++6libsigc-2.0.so.0)
OBSOLETED_BY = CSWlibsigc++
OBSOLETED_BY_CSWlibsigc2-0-0 += CSWlibsigc2-0-0-gxx
CATALOGNAME_CSWlibsigc2-0-0-gxx = libsigc2_0_0_gxx_stub-0 = CSWlibsigc++
# CSWsigc++ is the previous package name
INCOMPATIBLE_PKGS_CSWlibsigc++ = CSWsigc++

PACKAGEoc
ARCHALL_CSWlibsigc-doc = 1
SPKG_DESC_CSWlibsigc-doc = Documentation for libsigc++
PKGFILES_CSWlibsigc-doc  = .*/doc/libsigc\+\+-2\.0/.*
PKGFILES_CSWlibsigc-doc += .*/devhelp/.*igc++ = CSWsigc++

PACKAGES += CSWlibsigc-dev
SPKG_DESC_CSWlibsigc-dev = Header files for libsigc-2.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsigc-dev = CSWlibsigc2-0-0
OBSOLETED_B = CSWlibsigc++devel
OBSOLETED_BY_CSWlibsigc-dev += CSWlibsigc-gxx-dev
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel_stub
CATALOGNAME_CSWlibsigc-gxx-dev = libsigc_gxx_dev= libsigc++_devel_stub

BUILD64_LIBSONFIGURE_ENV = MAKE=gmake
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

include gar/category.mk
