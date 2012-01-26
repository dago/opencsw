NAME = clzip
VERSION = 1.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = a lossless data compressor based on the LZMA algorithm
define BLURB
endef

MASTER_SITES = http://mirrors.zerg.biz/nongnu/lzip/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0001-Do-not-use-gcc-CFLAGS.patch
PATCHFILES += 0002-Do-not-use-gcc-CFLAGS.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

NODIRPATHS = --includedir
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += CXX="$(CXX)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

include gar/category.mk
