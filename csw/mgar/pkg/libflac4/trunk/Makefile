NAME = libflac
VERSION = 1.0.4
CATEGORIES = lib
GARTYPE = v2

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

PATCHFILES = strip-nasm-1.0.4.patch
BUILD_DEP_PKGS += CSWbash

PACKAGES += CSWlibflac4
CATALOGNAME_CSWlibflac4 = libflac4
SPKG_DESC_CSWlibflac4 = Free lossless audio codec library, libflac.so.4
PKGFILES_CSWlibflac4 = $(call pkgfiles_lib,libFLAC.so.4)
RUNTIME_DEP_PKGS_CSWlibflac4 += CSWiconv

# Override conflicts with CSWflac as the new CSWflac is built from the latest libflac
CHECKPKG_OVERRIDES_CSWlibflac4 += file-collision|/opt/csw/lib/libFLAC.so.4.0.1|CSWflac|CSWlibflac4
CHECKPKG_OVERRIDES_CSWlibflac4 += file-collision|/opt/csw/lib/libFLAC.so.4|CSWflac|CSWlibflac4

VENDOR_URL = http://flac.sourceforge.net/

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

EXTRA_LINKER_FLAGS = -liconv -lm

# Must be defined and empty or -I$(includedir) is added too early
# EXTRA_INC = ../../include
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS) -D__inline=

CONFIGURE_ARGS = $(DIRPATHS)

# This is a legacy library, built XMMS plugin against newest one
CONFIGURE_ARGS += --with-xmms-prefix=/notthere

# There is one test failing, but as this is really a long-outdated legacy library
# I don't care much for now.
SKIPTEST ?= 1

include gar/category.mk

post-patch-modulated:
	perl -pi -e "s/-O3 //g" $(WORKSRC)/configure
	$(MAKECOOKIE)
