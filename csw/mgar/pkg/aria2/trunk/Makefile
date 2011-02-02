# $Id$
NAME = aria2
VERSION = 1.10.9
CATEGORIES = utils

DESCRIPTION = The Next Generation Download Utility
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0001-Remove-tailing-commas-in-enum.patch
PATCHFILES += 0002-Use-inttypes-if-stdint-is-not-available.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.xz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
