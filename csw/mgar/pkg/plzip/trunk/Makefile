NAME = plzip
VERSION = 0.7
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A lossless data compressor based on the LZMA algorithm
define BLURB
  Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
  integrity checking and a user interface similar to the one of gzip or bzip2. Lzip
  decompresses almost as fast as gzip and compresses better than bzip2, which makes
  it well suited for software distribution and data archiving. 
  Currently only compression is performed in parallel. Parallel decompression is
  planned to be implemented soECTon.
endef

GNU_PROJ = lzip
MASTER_SITES = $(GNU_NMIRROR)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES  = 0001-Add-prototype-for-kill-2.patch
PATCHFILES += 0002-Use-ucb-echo.patch

DEP_PKGS = CSWlzlib

VENDOR_URL = http://www.nongnu.org/lzip/lzlib.html

EXTRA_CXXFLAGS = -xcode=pic32
EXTRA_LINKER_FLAGS = -norunpath

NOISALIST = 1
NODIRPATHS = --includedir
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

inclu