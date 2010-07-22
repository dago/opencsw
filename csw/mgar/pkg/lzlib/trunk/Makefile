GARNAME = lzlib
GARVERSION = 1.0
CATEGORIES = lib

DESCRIPTION = A lossless data compression library based on the LZMA algorithm
define BLURB
  The lzlib compression library provides in-memory LZMA compression and
  decompression functions, including integrity checking of the uncompressed
  data. The compressed data format used by the library is the lzip format. 
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/lzip/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Remove-Linux-specific-stuff-add-Solaris-specific-stu.patch
PATCHFILES += 0002-Change-linker-flags-for-shared-libs-to-be-Sun-Studio.patch
PATCHFILES += 0001-Do-not-do-ldconfig.patch
PATCHFILES += 0002-Use-ucb-echo-as-it-only-understands-n.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.nongnu.org/lzip/lzlib.html

EXTRA_CXXFLAGS = -xcode=pic32
EXTRA_LINKER_FLAGS = -lCrun

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

TEST_TARGET = check

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

include gar/category.mk

post-install-modulated:
	gln -s liblz.so.1 $(DESTDIR)$(libdir)/liblz.so
	@$(MAKECOOKIE)

