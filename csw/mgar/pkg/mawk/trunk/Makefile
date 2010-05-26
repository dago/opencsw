# $Id$
GARNAME = mawk
GARVERSION = 1.3.4
CATEGORIES = utils

DESCRIPTION = Fast, bytecode-based AWK
define BLURB
endef

MASTER_SITES = ftp://invisible-island.net/mawk/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://invisible-island.net/mawk/mawk.html

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
