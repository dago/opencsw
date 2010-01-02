GARNAME = mpeg4ip
GARVERSION = 1.6.1
CATEGORIES = lib

DESCRIPTION = Libraries for MPEG-4/H.261/MPEG-2/H.263 MP3/AAC/AMR
define BLURB
  Provided are a live MPEG-4/H.261/MPEG-2/H.263 MP3/AAC/AMR broadcaster
  and file recorder, command line utilities such as an MP4 file creator
  and hinter, and an player that can both stream and playback from local file.
endef

SF_PROJ = mpeg4ip
MASTER_SITES = http://download.m0k.org/handbrake/contrib/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTNAME = $(GARNAME)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
