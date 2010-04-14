# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = minicom
GARVERSION = 2.4
CATEGORIES = apps

DESCRIPTION = Serial communication program
define BLURB
endef

WGET_OPTS = --no-check-certificate
MASTER_SITES = https://alioth.debian.org/frs/download.php/3195/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://alioth.debian.org/projects/minicom/

# Compilation doesn't work unless this is fixed:
Ã#   https://alioth.debian.org/tracker/index.php?func=detail&aid=312462&group_id=30018&atid=100031

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
