GARNAME = libao
GARVERSION = 0.8.4
CATEGORIES = lib

DESCRIPTION = Cross-platform audio library
define BLURB
  libao is a way to easily add cross-platform audio output to your program.
  Output devices are implemented as dynamic plugins, and support for OSS, ESD,
  ALSA, aRTs, Solaris, and Irix outputs are currently supported.
endef

MASTER_SITES = http://www.xiph.org/ao/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibao,)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
