GARNAME = libvorbis
GARVERSION = 1.0.1
CATEGORIES = lib

SPKG_PKGNAME = CSWlibvorbis
SPKG_BITNAME = libvorbis

DESCRIPTION = Vorbis codec library.
define BLURB
  Ogg Vorbis is a high-quality lossy audio codec that is free of intellectual
  property restrictions. libvorbis is the main vorbis codec library. It depends
  on libogg for bitstream and framing support.
endef

MASTER_SITES = http://www.vorbis.com/files/1.0.1/unix/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LIBDEPS += lib/libogg

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
