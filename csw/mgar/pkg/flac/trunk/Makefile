GARNAME = libflac
GARVERSION = 1.2.1
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.1.4 1.2.1

MODULATIONS = isa-sparcv8-garversion-1.1.4
# There was no 64 bit legacy version. Do not provide it as new binaries should
# link against the new version.
#MODULATIONS += isa-sparcv9-garversion-1.1.4
MODULATIONS += isa-sparcv8-garversion-1.2.1
MODULATIONS += isa-sparcv9-garversion-1.2.1

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
DISTNAME = $(SF_PROJ)-$(GARVERSION)
DISTFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(SF_PROJ)-$(VERSION).tar.gz)

PATCHFILES_isa-sparcv8-garversion-1.1.4 = libtool-64bit.patch
PATCHFILES_isa-sparcv9-garversion-1.1.4 = libtool-64bit.patch
PATCHFILES_isa-sparcv8-garversion-1.2.1 = libtool-64bit.patch no-stdint.patch
PATCHFILES_isa-sparcv9-garversion-1.2.1 = libtool-64bit.patch no-stdint.patch

PACKAGES = CSWflac CSWxmmsflac
CATALOGNAME = libflac
CATALOGNAME = xmms_flac

REQUIRED_PKGS_CSWflac = CSWiconv CSWlibogg
REQUIRED_PKGS_CSWxmmsflac = CSWglib CSWgtk CSWxmms CSWflac

SPKG_DESC_CSWflac = Free lossless audio codec
SPKG_DESC_CSWxmmsflac = FLAC plugin for XMMS

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=13478
UPSTREAM_USE_SF = 1
UFILES_REGEX = flac-(\d+(?:\.\d+)*)-src

BUILD64 = 1

NODIRPATHS = --includedir
CPPFLAGS =

# Must be defined and empty or -I$(includedir) is added too early
EXTRA_CFLAGS = -D__inline=
EXTRA_BUILD_EXPORTS = AM_CFLAGS

EXTRA_CONFIGURE_ARGS_mm-64 = --disable-xmms-plugin
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_mm-$(MEMORYMODEL))

TEST_TARGET = check

MERGE_SCRIPTS_isa-i386-garversion-1.1.4 = copy-only
MERGE_DIRS_isa-i386-garversion-1.1.4 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-1.1.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.1.4 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-1.2.1 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-1.2.1 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.2.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.1.4 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-1.1.4 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.1.4 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.1.4 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.2.1 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-1.2.1 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.2.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWxmmsflac = $(libdir)/xmms/.*

include gar/category.mk

CC := $(abspath ./bin/cc)
CXX := $(abspath ./bin/CC)
PATH := ./bin:$(PATH):/usr/ccs/bin
