GARNAME = audiofile
GARVERSION = 0.2.6
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
