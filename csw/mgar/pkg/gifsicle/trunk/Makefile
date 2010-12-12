# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = gifsicle
VERSION = 1.59
CATEGORIES = utils

DESCRIPTION = Tool for creating, editing, and getting information about GIF images
define BLURB
endef

MASTER_SITES = http://www.lcdf.org/gifsicle/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
