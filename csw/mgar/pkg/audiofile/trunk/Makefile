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

PACKAGES += CSWlibaudiofile0
CATALOGNAME_CSWlibaudiofile0 = libaudiofile0
SPKG_DESC_CSWlibaudiofile0 = Silican Graphics audio file library, libaudiofile.so.0
PKGFILES_CSWlibaudiofile0 = $(call pkgfiles_lib,libaudiofile.so.0)
OBSOLETES_CSWlibaudiofile0 = CSWaudiofile

PACKAGES += CSWlibaudiofile-utils
CATALOGNAME_CSWlibaudiofile-utils = libaudiofile_utils
SPKG_DESC_CSWlibaudiofile-utils = Utility programs from Silicon Graphics audio file library
PKGFILES_CSWlibaudiofile-utils = $(call baseisadirs,$(bindir),.*)
RUNTIME_DEP_PKGS_CSWlibaudiofile-utils += CSWlibaudiofile0
OBSOLETES_CSWlibaudiofile-utils = CSWaudiofile

PACKAGES += CSWlibaudiofile-dev
CATALOGNAME_CSWlibaudiofile-dev = libaudiofile_dev
SPKG_DESC_CSWlibaudiofile-dev = Development files for libaudiofile.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibaudiofile-dev = CSWlibaudiofile0

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra += copy-config-only
MERGE_SCRIPTS_isa-extra += copy-relocated-only
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
