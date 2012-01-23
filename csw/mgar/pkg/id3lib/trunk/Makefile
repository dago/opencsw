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
PKGFILES_CSWlibid3-3-8-3 = $(call pkgfiles_lib,libid3-3.8.so.3)
RUNTIME_DEP_PKGS_CSWlibid3-3-8-3 += CSWzlib

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
OBSOLETED_BY_CSWlibid3-utils = CSWid3lib

EXTRA_LDFLAGS = -norunpath

# The following part is to make the library self-sufficient
# (that means a simple -lid3 is sufficient).
# We link with /usr/ccs/bin/ld which requires setting the path to libCstd.so,
# using CC as linker would have made this automatic.
SUBDIR64-sparc = v9
SUBDIR64-i386 = amd64
EXTRA_LINKER_FLAGS = -L$($(GARCOMPILER)_CC_HOME)/lib/$(SUBDIR$(MEMORYMODEL)-$(GARCH)) -lCstd -lz

BUILD64_LIBS_ONLY = 1

include gar/category.mk
