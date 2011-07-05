NAME = easytag
VERSION = 2.1.6
CATEGORIES = apps

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
  EasyTAG is a utility for viewing and editing tags for MP3, MP2, MP4/AAC, FLAC,
  Ogg Vorbis, MusePack, Monkey's Audio and WavPack files. Its simple and nice GTK+
  interface makes tagging easier under GNU/Linux or Windows.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES += patch_easytag_216_cddb_manual_search_fix.diff

BUILD_DEP_PKGS += CSWlibogg-dev
BUILD_DEP_PKGS += CSWlibvorbis-dev
BUILD_DEP_PKGS += CSWlibflac-dev
BUILD_DEP_PKGS += CSWlibspeex-dev

RUNTIME_DEP_PKGS_CSWeasytag += CSWlibintl8
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibogg0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibflac8
RUNTIME_DEP_PKGS_CSWeasytag += CSWfconfig
RUNTIME_DEP_PKGS_CSWeasytag += CSWpango
RUNTIME_DEP_PKGS_CSWeasytag += CSWftype2
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWeasytag += CSWzlib
RUNTIME_DEP_PKGS_CSWeasytag += CSWgtk2
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibatk
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibwavpack1
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWeasytag += CSWglib2

RUNTIME_DEP_PKGS_CSWeasytag += CSWgcc3g++rt

# Needed for gethostbyname
EXTRA_LINKER_FLAGS =  -lnsl

include gar/category.mk
