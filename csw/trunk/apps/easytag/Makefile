# Using GCC until I can work out how to exclude id3lib from being used.
# It's being pulled in and it cause the compile to fail with cc

GARNAME = easytag
GARVERSION = 2.1.2
CATEGORIES = applications

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
EasyTAG is a utility for viewing and editing tags for MP3, MP2, MP4/AAC, FLAC, Ogg Vorbis, MusePack, Monkey's Audio and WavPack files. Its simple and nice GTK+ interface makes tagging easier under GNU/Linux or Windows.
endef

SF_PROJ = easytag
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWeasytag,depend)

PATCHFILES = patch_easytag_212_213.diff

GARCOMPILER = GNU

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

include ../category.mk
