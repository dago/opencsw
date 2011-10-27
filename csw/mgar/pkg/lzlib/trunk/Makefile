NAME = lzlib
VERSION = 1.2
CATEGORIES = lib

DESCRIPTION = A lossless data compression library based on the LZMA algorithm
define BLURB
  The lzlib compression library provides in-memory LZMA compression and
  decompression functions, including integrity checking of the uncompressed
  data. The compressed data format used by the library is the lzip format. 
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/lzip/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES =  0001-gcc-to-sunstudio.patch
PATCHFILES += 0002-gcc-to-sunstudio-2.patch

VENDOR_URL = http://www.nongnu.org/lzip/lzlib.html

PACKAGES += CSWliblz1
SPKG_DESC_CSWliblz1 = A lossless data compression library based on the LZMA algorithm, liblz.so.1
PKGFILES_CSWliblz1 = $(call pkgfiles_lib,liblz.so.1)
OBSOLETED_BY_CSWliblz1 = CSWlzlib

PACKAGES += CSWliblz-dev
SPKG_DESC_CSWliblz-dev = Development files for liblz.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliblz-dev = CSWliblz1

EXTRA_CXXFLAGS = -xcode=pic32
EXTRA_LINKER_FLAGS = -lCrun -norunpath

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_VARS = INSTALL LDCONFIG
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall
# This is close to a NOP
INSTALL_OVERRIDE_VAR_LDCONFIG = echo

include gar/category.mk

post-install-modulated:
	gln -s liblz.so.1 $(DESTDIR)$(libdir)/liblz.so
	@$(MAKECOOKIE)

