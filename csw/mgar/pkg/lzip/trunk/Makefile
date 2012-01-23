NAME = lzip
VERSION = 1.11
CATEGORIES = utils

DESCRIPTION = A lossless data compressor based on the LZMA algorithm
define BLURB
  Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
  integrity checking and a user interface similar to the one of gzip or bzip2. Lzip
  decompresses almost as fast as gzip and compresses better than bzip2, which makes
  it well suited for software distribution and data archiving. 
  Currently only compression is performed in parallel. Parallel decompression is
  planned to be implemented soon.
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/lzip/ 
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0001-inttypes.h-instead-of-stdint.h.patch
PATCHFILES += 0002-inttypes.h-instead-of-stdint.h.patch
# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.nongnu.org/lzip/lzip.html

NODIRPATHS = --includedir
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

include gar/category.mk
