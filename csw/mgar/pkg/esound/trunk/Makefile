GARNAME = esound
GARVERSION = 0.2.41
CATEGORIES = lib

DESCRIPTION = EsounD, The Enlightened Sound Daemon
define BLURB
  The Enlightened Sound Daemon mixes several audio streams for playback
  by a single audio device. You can also pre-load samples, and play them
  back without having to send all the data for the sound. Network
  transparency is also built in, so you can play sounds on one machine,
  and listen to them on another.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

REQUIRED_PKGS = CSWaudiofile

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
