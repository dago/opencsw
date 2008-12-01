GARNAME = libvorbis
GARVERSION = 1.2.0
CATEGORIES = lib

DESCRIPTION = Vorbis codec library.
define BLURB
  Ogg Vorbis is a high-quality lossy audio codec that is free of intellectual
  property restrictions. libvorbis is the main vorbis codec library. It depends
  on libogg for bitstream and framing support.
endef

MASTER_SITES = http://downloads.xiph.org/releases/vorbis/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibvorbis,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LIBDEPS += lib/libogg

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
