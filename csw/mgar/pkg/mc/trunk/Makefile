# $Id$
GARNAME = mc
GARVERSION = 4.7.0.10
CATEGORIES = utils

DESCRIPTION = A curses-based visual shell and file manager
define BLURB
endef

MASTER_SITES = http://www.midnight-commander.org/downloads/
DISTFILES  = $(DISTNAME).tar.lzma

PATCHFILES = 0001-Honour-HAVE_STDINT_H.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
