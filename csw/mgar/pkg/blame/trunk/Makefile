# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = blame
VERSION = 1.3.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Displays the last modification for each line in an RCS file
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Do-not-force-Wall.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
