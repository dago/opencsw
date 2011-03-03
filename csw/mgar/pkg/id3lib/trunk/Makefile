# $Id$
NAME = id3lib
VERSION = 3.8.3
CATEGORIES = lib

DESCRIPTION = Library for manipulating ID3v1/v1.1 and ID3v2 tags
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Make-pointer-types-match.patch
PATCHFILES += 0002-Do-not-use-Wall.patch
PATCHFILES += 0003-Work-around-conversion-in-iostream.patch

PACKAGES += CSWlibid3-3-8-3
CATALOGNAME_CSWlibid3-3-8-3 = libid3_3_8_3
SPKG_DESC_CSWlibid3-3-8-3 = Library for manipulating ID3v1/v1.1 and ID3v2 tags, libid3-3.8.so.3
PKGFILES_CSWlibid3-3-8-3 = $(call baseisadirs,$(libdir),libid3-3\.8\.so\.3(\.\d+)*)

PACKAGES += CSWlibid3-dev
CATALOGNAME_CSWlibid3-dev = libid3_dev
SPKG_DESC_CSWlibid3-dev = Development files for libid3.so
PKGFILES_CSWlibid3-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibid3-dev += CSWlibid3-3-8-3

PACKAGES += CSWlibid3-utils
CATALOGNAME_CSWlibid3-utils = libid3_utils
SPKG_DESC_CSWlibid3-utils = Utilities for manipulating ID3v2 tags
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibid3-3-8-3 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibid3-utils += CSWlibid3-3-8-3
RUNTIME_DEP_PKGS_CSWlibid3-utils += CSWiconv
RUNTIME_DEP_PKGS_CSWlibid3-utils += CSWzlib
OBSOLETES_CSWlibid3-utils = CSWid3lib

EXTRA_LDFLAGS = -norunpath

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
