NAME = libtorrent
VERSION = 0.16.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = BitTorrent library written in C++ for *nix
define BLURB
  BitTorrent library written in C++ for *nix, with a focus on high performance and good code.
  The library differentiates itself from other implementations by transfering directly from
  file pages to the network stack. On high-bandwidth connections it is able to seed at 3 times
  the speed of the official client. 
endef

MASTER_SITES += $(GOOGLE_MIRROR)
DISTNAME = libtorrent-rasterbar-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-More-Solaris-fixes.patch

PACKAGES += CSWlibtorrent-rasterbar6
SPKG_DESC_CSWlibtorrent-rasterbar6 = BitTorrent library written in C++, libtorrent-rasterbar.so.6
PKGFILES_CSWlibtorrent-rasterbar6 += $(call pkgfiles_lib,libtorrent-rasterbar.so.6)
RUNTIME_DEP_PKGS_CSWlibtorrent-rasterbar6 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibtorrent-rasterbar6 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtorrent-rasterbar6 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibtorrent-rasterbar6 += CSWlibboost-system1-49-0-gxx

PACKAGES += CSWlibtorrent-rasterbar-gxx-dev
SPKG_DESC_CSWlibtorrent-rasterbar-gxx-dev = Development files for libtorrent-rasterbar.so.6
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtorrent-rasterbar-gxx-dev += CSWlibtorrent-rasterbar6

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1

# This is neeed to enable Posix threads in boost gxx
EXTRA_CXXFLAGS += -pthreads

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --disable-libtool-lock
CONFIGURE_ARGS += --disable-debug

CONFIGURE_ARGS += --with-boost-libdir=$(libdir)

include gar/category.mk
