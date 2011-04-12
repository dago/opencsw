NAME = libflac
VERSION = 1.2.1
CATEGORIES = lib

DESCRIPTION = Free lossless audio codec
define BLURB
  FLAC stands for Free Lossless Audio Codec, an audio format similar
  to MP3, but lossless, meaning that audio is compressed in FLAC without
  any loss in quality. This is similar to how Zip works, except with FLAC
  you will get much better compression because it is designed specifically
  for audio, and you can play back compressed FLAC files in your favorite
  player (or your car or home stereo, see supported devices) just like you
  would an MP3 file.
endef

SF_PROJ = flac
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

PATCHFILES += libtool-64bit.patch
PATCHFILES += strip-nasm-1.2.1.patch
PATCHFILES += no-stdint.patch

BUILD_DEP_PKGS += CSWbash

PACKAGES += CSWlibflac8
CATALOGNAME_CSWlibflac8 = libflac8
SPKG_DESC_CSWlibflac8 = Free lossless audio codec library, libflac.so.8
PKGFILES_CSWlibflac8 = $(call pkgfiles_lib,libFLAC.so.8)
RUNTIME_DEP_PKGS_CSWlibflac8 += CSWiconv

# Override conflicts with CSWflac as the new CSWflac is built from the latest libflac
CHECKPKG_OVERRIDES_CSWlibflac7 += file-collision|/opt/csw/lib/libFLAC.so.7.0.0|CSWflac|CSWlibflac7
CHECKPKG_OVERRIDES_CSWlibflac7 += file-collision|/opt/csw/lib/libFLAC.so.7|CSWflac|CSWlibflac7

VENDOR_URL = http://flac.sourceforge.net/

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

# EXTRA_LINKER_FLAGS = -liconv -lm

# Must be defined and empty or -I$(includedir) is added too early
# EXTRA_INC = ../../include
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS) -D__inline=
# EXTRA_CFLAGS = -D__inline=

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CONFIGURE_ARGS_mm-64 = --disable-xmms-plugin
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# XXX: Assembler optimization just doesn't work. Disable for now.
CONFIGURE_ARGS += --disable-asm-optimizations

TEST_TARGET = check

# There is one test failing, but as this is really a long-outdated legacy library
# I don't care much for now.
# SKIPTEST ?= 1

include gar/category.mk
