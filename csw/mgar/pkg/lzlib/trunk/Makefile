NAME = lzlib
VERSION = 1.1
CATEGORIES = lib

DESCRIPTION = A lossless data compression library based on the LZMA algorithm
define BLURB
  The lzlib compression library provides in-memory LZMA compression and
  decompression functions, including integrity checking of the uncompressed
  data. The compressed data format used by the library is the lzip format. 
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/lzip/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-gcc-to-sunstudio.patch
PATCHFILES = 0002-gcc-to-sunstudio-2.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

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

