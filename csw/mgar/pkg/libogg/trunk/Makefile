NAME = libogg
VERSION = 1.2.0
CATEGORIES = lib

DESCRIPTION = Ogg bitstream format support library
define BLURB
  libogg is the bitstream and framing library for the Ogg project. It provides
  functions which are necessary to codec libraries like libvorbis.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ogg/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
SKIPTEST = 1

include gar/category.mk
