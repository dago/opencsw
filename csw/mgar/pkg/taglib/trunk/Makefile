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

# CSWtaglibgcc is an empty stub to CSWtaglib
PACKAGES = CSWtaglib CSWtaglibgcc

CATALOGNAME_CSWtaglib    = taglib
CATALOGNAME_CSWtaglibgcc = taglib_gcc

SPKG_DESC_CSWtaglib    = $(DESCRIPTION)
SPKG_DESC_CSWtaglibgcc = Stub to CSWtaglib no longer compiled with gcc

ARCHALL_CSWtaglibgcc = 1

RUNTIME_DEP_PKGS_CSWtaglib = CSWzlib

RUNTIME_DEP_PKGS_CSWtaglibgcc = CSWtaglib
CHECKPKG_OVERRIDES_CSWtaglibgcc += surplus-dependency|CSWtaglib

PKGFILES_CSWtaglibgcc = NONE

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
