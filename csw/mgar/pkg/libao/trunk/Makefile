GARNAME = libao
GARVERSION = 0.8.8
CATEGORIES = lib

DESCRIPTION = Cross-platform audio library
define BLURB
  libao is a way to easily add cross-platform audio output to your program.
  Output devices are implemented as dynamic plugins, and support for OSS, ESD,
  ALSA, aRTs, Solaris, and Irix outputs are currently supported.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ao/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.xiph.org/ao/

REQUIRED_PKGS = CSWaudiofile CSWesound

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
