# $Id$
NAME = xorriso
VERSION = 1.0.0
CATEGORIES = utils

DESCRIPTION = ISO 9660 Rock Ridge Filesystem Manipulator
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Use-inttypes.h-when-stdint.h-is-not-available.patch
PATCHFILES += 0002-Add-linkage-to-librt.so-for-nanosleep-if-necessary.patch
PATCHFILES += 0003-Use-timegm-substitute-which-does-not-use-setenv.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWxorriso += CSWiconv
RUNTIME_DEP_PKGS_CSWxorriso += CSWreadline
RUNTIME_DEP_PKGS_CSWxorriso += CSWbzip2
RUNTIME_DEP_PKGS_CSWxorriso += CSWzlib

include gar/category.mk
