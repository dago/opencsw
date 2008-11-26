GARNAME = easytag
GARVERSION = 2.1.5
CATEGORIES = apps

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
EasyTAG is a utility for viewing and editing tags for MP3, MP2, MP4/AAC, FLAC, Ogg Vorbis, MusePack, Monkey's Audio and WavPack files. Its simple and nice GTK+ interface makes tagging easier under GNU/Linux or Windows.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWeasytag,depend)


GARCOMPILER = GNU

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

TEST_SCRIPTS =
include gar/category.mk
