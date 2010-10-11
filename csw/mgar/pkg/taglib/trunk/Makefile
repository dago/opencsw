GARNAME = taglib
GARVERSION = 1.6.3
CATEGORIES = lib

DESCRIPTION = Library for reading and editing the meta-data of several popular audio formats
define BLURB
  TagLib is a library for reading and editing the meta-data of several popular audio formats.
  Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags
  and Vorbis comments in FLAC, MPC, Speex, WavPack and TrueAudio files.
endef

MASTER_SITES = http://developer.kde.org/~wheeler/files/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-Make-sure-m64-is-passed-to-the-linker.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.MPL

VENDOR_URL = http://developer.kde.org/~wheeler/taglib.html

PACKAGES = CSWtaglib CSWtaglibdevel

CATALOGNAME_CSWtaglib = taglib
CATALOGNAME_CSWtaglibdevel = taglib_devel

SPKG_DESC_CSWtaglib = $(DESCRIPTION)
SPKG_DESC_CSWtaglibdevel = Developer files for taglib

RUNTIME_DEP_PKGS_CSWtaglib = CSWzlib
RUNTIME_DEP_PKGS_CSWtaglibdevel = CSWtaglib
CHECKPKG_OVERRIDES_CSWtaglibdevel += surplus-dependency|CSWtaglib

PKGFILES_CSWtaglibdevel = $(PKGFILES_DEVEL)

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
