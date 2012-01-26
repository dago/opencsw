NAME = taglib
VERSION = 1.6.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library for reading and editing the meta-data of several popular audio formats
define BLURB
  TagLib is a library for reading and editing the meta-data of several popular audio formats.
  Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags
  and Vorbis comments in FLAC, MPC, Speex, WavPack and TrueAudio files.
endef

MASTER_SITES = http://developer.kde.org/~wheeler/files/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.MPL

VENDOR_URL = http://developer.kde.org/~wheeler/taglib.html

PACKAGES = CSWtaglibgcc
CATALOGNAME = taglib_gcc

RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWzlib
RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWgcc3corert
RUNTIME_DEP_PKGS_CSWtaglibgcc += CSWgcc3g++rt

# This does not work with gcc4 as the kde-gcc stuff is compiled
# with gcc3 and the runtime libs for gcc3 and gcc4 are slightly
# incompatib√le.
GARCOMPILER = GCC3

EXTRA_LD_FLAGS = -lc -lm

# Do not use -O2, see below.
OPT_FLAGS_GCC = -pipe

prefix = $(BUILD_PREFIX)/kde-gcc
CONFIGURE_ARGS = $(DIRPATHS)

# This is a legacy lib, don't care too much about the naming for now.
CHECKPKG_OVERRIDES_CSWtaglibgcc += shared-lib-package-contains-so-symlink|file=/opt/csw/kde-gcc/lib/libtag.so
CHECKPKG_OVERRIDES_CSWtaglibgcc += shared-lib-package-contains-so-symlink|file=/opt/csw/kde-gcc/lib/libtag_c.so
CHECKPKG_OVERRIDES_CSWtaglibgcc += non-uniform-lib-versions-in-package|sonames=['libtag.so.1',|'libtag_c.so.0']
CHECKPKG_OVERRIDES_CSWtaglibgcc += shared-lib-package-contains-so-symlink|file=/opt/csw/kde-gcc/lib/libtag.so
CHECKPKG_OVERRIDES_CSWtaglibgcc += shared-lib-package-contains-so-symlink|file=/opt/csw/kde-gcc/lib/libtag_c.so

include gar/category.mk

# Do not use any optimization or __sync_fetch_and_add_4 will be used which
# is undefined. -O2 is hardwired at many places, so dynamically rip it out.
pre-configure-modulated:
	perl -i -npe 's/-O2//' $(WORKSRC)/configure
	@$(MAKECOOKIE)
