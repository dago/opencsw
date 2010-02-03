GARNAME = faad2
GARVERSION = 2.7
CATEGORIES = lib

DESCRIPTION = Freeware Advanced Audio (AAC) Decoder including SBR decoding
define BLURB
  FAAD2 is an open source MPEG-4 and MPEG-2 AAC decoder, it is licensed
  under the GPLv2 license.
endef

SF_PROJ = faac
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES  = 0001-Remove-iquote-from-CFLAGS-unknown-to-SS.patch
PATCHFILES += 0002-Use-inline-suitable-for-SS.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch

PACKAGES = CSWfaad2
CATALOGNAME = faad2

SPKG_SOURCEURL = http://www.audiocoding.com/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
