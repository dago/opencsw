# $Id$
GARNAME = gif2png
GARVERSION = 2.5.4
CATEGORIES = utils

DESCRIPTION = Converts files from GIF to PNG
define BLURB
endef

MASTER_SITES = http://www.catb.org/~esr/gif2png/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

RUNTIME_DEP_PKGS_CSWgif2png += CSWzlib
RUNTIME_DEP_PKGS_CSWgif2png += CSWpng

include gar/category.mk
