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

# TODO on next release:
# - Move config file from /opt/csw/etc to /etc/opt/csw
# - Document the location in esd(1)
# - Skip 64 binaries

sysconfdir = /etc/opt/csw

PRESERVECONF = $(sysconfdir)/esd.conf
MIGRATE_FILES = esd.conf

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
