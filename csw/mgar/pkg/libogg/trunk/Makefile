GARNAME = libogg
GARVERSION = 1.1.3
CATEGORIES = lib

DESCRIPTION = Ogg bitstream format support library
define BLURB
  libogg is the bitstream and framing library for the Ogg project. It provides
  functions which are necessary to codec libraries like libvorbis.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ogg/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibogg,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
