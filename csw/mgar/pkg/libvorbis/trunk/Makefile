NAME = libvorbis
VERSION = 1.3.1
CATEGORIES = lib

DESCRIPTION = Vorbis codec library.
define BLURB
  Ogg Vorbis is a high-quality lossy audio codec that is free of intellectual
  property restrictions. libvorbis is the main vorbis codec library. It depends
  on libogg for bitstream and framing support.
endef

MASTER_SITES = http://downloads.xiph.org/releases/vorbis/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWvorbis
CATALOGNAME = libvorbis
RUNTIME_DEP_PKGS = CSWlibogg CSWsunmath

SPKG_SOURCEURL = http://www.vorbis.com/

BUILD64 = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_LD_FLAGS = -L$(libdir) -lsunmath -lm

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
