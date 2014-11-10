NAME = plzip
VERSION = 1.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A lossless data compressor based on the LZMA algorithm
define BLURB
  Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
  integrity checking and a user interface similar to the one of gzip or bzip2. Lzip
  decompresses almost as fast as gzip and compresses better than bzip2, which makes
  it well suited for software distribution and data archiving. 
  Currently only compression is performed in parallel. Parallel decompression is
  planned to be implemMASTER_SITES = http://download.savannah.gnu.org/releases/lzip/plzip/
DISTFILES += $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   http://lists.nongnu.org/archive/html/lzip-bug/2014-10/threads.html
PATCHFILES += 0001-Use-correct-signature-for-compress.patch

BUILD_DEP_PKGS += CSWliblz-dev

PACKAGES += CSWplzip
SPKG_DESC_CSWplzp = A lossless data compressor based on the LZMA algorithm
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWplzip += CSWliblz1DEP_PKGS = CSWlzlib

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