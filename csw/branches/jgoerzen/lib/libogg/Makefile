GARNAME = libogg
GARVERSION = 1.1
CATEGORIES = lib

SPKG_PKGNAME = CSWlibogg
SPKG_BITNAME = libogg

DESCRIPTION = Ogg bitstream and framing library.
define BLURB
  libogg is the bitstream and framing library for the Ogg project. It provides
  functions which are necessary to codec libraries like libvorbis.
endef

MASTER_SITES = http://www.vorbis.com/files/1.0.1/unix/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LIBDEPS += lib/libao

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
