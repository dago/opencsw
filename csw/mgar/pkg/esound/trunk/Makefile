NAME = esound
VERSION = 0.2.41
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.tux.org/~ricdude/EsounD.html
LICENSE = COPYING.LIB

PACKAGES += CSWlibesd0
CATALOGNAME_CSWlibesd0 = libesd0
SPKG_DESC_CSWlibesd0 = The enlightened sound daemon library, libesd.so.0
PKGFILES_CSWlibesd0 = $(call pkgfiles_lib,libesd.so.0)
RUNTIME_DEP_PKGS_CSWlibesd0 += CSWlibaudiofile0

PACKAGES += CSWlibesd-dev
CATALOGNAME_CSWlibesd-dev = libesd_dev
SPKG_DESC_CSWlibesd-dev = Development files for libesd.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibesd-dev += CSWlibesd0

ESD_BINS += esd
ESD_BINS += esdcat
ESD_BINS += esdctl
ESD_BINS += esdfilt
ESD_BINS += esdloop
ESD_BINS += esdmon
ESD_BINS += esdplay
ESD_BINS += esdrec
ESD_BINS += esdsample

PACKAGES += CSWesound
CATALOGNAME_CSWesound = esound
SPKG_DESC_CSWesound = The enlightened sound daemon
PKGFILES_CSWesound += $(foreach B,$(ESD_BINS),$(bindir)/$B $(mandir)/man1/$(B).1)
PKGFILES_CSWesound += $(sysconfdir)/.*
RUNTIME_DEP_PKGS_CSWesound += CSWlibesd0
RUNTIME_DEP_PKGS_CSWesound += CSWlibaudiofile0

sysconfdir = /etc/opt/csw

PRESERVECONF = $(sysconfdir)/esd.conf
MIGRATE_FILES_CSWesound = esd.conf

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra += copy-relocated-only
MERGE_SCRIPTS_isa-extra += copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
