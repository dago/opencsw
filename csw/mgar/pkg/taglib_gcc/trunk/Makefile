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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.MPL

VENDOR_URL = http://developer.kde.org/~wheeler/taglib.html

PACKAGES = CSWtaglibgcc
CATALOGNAME = taglib_gcc

RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWzlib
RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWgcc4g++rt

GARCOMPILER = GCC4

EXTRA_LD_FLAGS = -lc -lm

prefix = $(BUILD_PREFIX)/kde-gcc
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
