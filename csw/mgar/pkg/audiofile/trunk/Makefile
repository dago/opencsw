NAME = audiofile
VERSION = 0.2.7
CATEGORIES = lib

DESCRIPTION = Silicon Graphics Audio File Library
define BLURB
  The Audio File Library provides a uniform and elegant
  API for accessing a variety of audio file formats, such
  as AIFF/AIFF-C, WAVE, NeXT/Sun .snd/.au, Berkeley/IRCAM/CARL
  Sound File, Audio Visual Research, Amiga IFF/8SVX, and NIST
  SPHERE. Supported compression formats are currently G.711
  mu-law and A-law and IMA and MS ADPCM.
endef

MASTER_SITES = http://www.68k.org/~michael/audiofile/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Delivered from the Michael Pruett (upstream author)
PATCHFILES = 0001-Add-missing-headers-for-C99.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# amd64 on i386
CHECKPKG_OVERRIDES_CSWaudiofile += soname-not-found|libm.so.2
CHECKPKG_OVERRIDES_CSWaudiofile += soname-not-found|libm.so.2
CHECKPKG_OVERRIDES_CSWaudiofile += soname-not-found|libm.so.2

include gar/category.mk
