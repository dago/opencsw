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

#MASTER_SITES = http://libtorrent.rakshasa.no/downloads/
MASTER_SITES += $(GOOGLE_MIRROR)
DISTNAME = libtorrent-rasterbar-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# Patches from http://cr.opensolaris.org/~alz/bittorrent/raw_files/new/usr/src/lib/libtorrent/
#PATCHFILES = rlibtorrent-04-sunpro.diff rlibtorrent-01-madvise.diff rlibtorrent-03-dh-generate.diff
#PATCHFILES += rlibtorrent-05-tracker-usable.diff

#PATCHFILES += 0001-Ignore-__UNUSED.patch

#PATCHFILES += 0001-Use-correct-m4-quoting-for-code-in-autoconf.patch

#PATCHFILES += 0002-Use-posix_memalign-only-when-available.patch

#PATCHFILES += 0003-Fix-the-signature-instead-of-using-sig_t.patch

PATCHFILES += 0001-More-Solaris-fixes.patch

# As we have patches autoconf we need to autotools bootstrap and that requires
# cppunit (although it is optional for afterwards building we need it now for the
# AC macros).
BUILD_DEP_PKGS += CSWcppunit-gxx-dev

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
# XXX: Can alternatively -pthreads be set?
EXTRA_CXXFLAGS += -D_PTHREADS

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --disable-libtool-lock
CONFIGURE_ARGS += --disable-debug

CONFIGURE_ARGS += --with-boost-libdir=$(libdir)

# The testsuite has a linker error with mangled C++ symbols, skip for now
# SKIPTEST ?= 1

include gar/category.mk

#post-patch-modulated:
#	-cd $(WORKSRC) && ./autogen.sh
#	@$(MAKECOOKIE)

#pre-configure-modulated:
##	cd $(WORKSRC) && aclocal-1.10 -I./scripts -I. && autoheader \
## && libtoolize --automake --copy --force && automake-1.10 && autoconf
#	cd $(WORKSRC) && aclocal-1.10 -I scripts && \
#  automake-1.10 --gnu && autoconf
#
#	$(MAKECOOKIE)


#post-configure-modulated:
#	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
#	@$(MAKECOOKIE)
