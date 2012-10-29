NAME = zutils
VERSION = 1.0-rc3
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Utilities to deal with compressed and non-compressed files
define BLURB
  Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
  integrity checking and a user interface similar to the one of gzip or bzip2. Lzip
  decompresses almost as fast as gzip and compresses better than bzip2, which makes
  it well suited for software distribution and data archiving. 
  Currently only compression is performed in parallel. Parallel decompression is
  planned to be implemented soon.
endef


MASTER_SITES = http://download.savannah.gnu.org/releases/zutils/
DISTFILES = $(DISTNAME).tar.lz
PATCHFILES  = 0001-Use-inttypes.h-instead-of-stdint.h-and-add-signal.h.patch
PATCHFILES += 0003-Use-Zutils-instead-of-zutils.patch
PATCHFILES += 0004-Avoid-ambiguity-between-char-and-unsigned-long-on-sp.patch

BUILD_DEP_PKGS += CSWhelp2man
BUILD_DEP_PKGS += CSWlzip

# The lzip binary is used from the scripts which is not detected by checkpkg
RUNTIME_DEP_PKGS = CSWlzip
CHECKPKG_OVERRIDES_CSWzutils += surplus-dependency|CSWlzip

VENDOR_URL = http://www.nongnu.org/zutils/zutils.html

EXTRA_LINKER_FLAGS = -norunpath

BUILD64 = 1
ISAEXEC = 1

NODIRPATHS = --includedir
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

EXTRA_PAX_ARGS = -s ",/z,/Z,p"

TEST_ENV_PATH = $(bindir):$(prefix)/gnu:$(PATH)

include gar/category.mk

post-extract-modulated:
	-gln -s zutils $(WORKSRC)/Zutils
	@$(MAKECOOKIE)
