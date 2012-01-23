NAME = fileutils
VERSION = 4.1
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = File utilities
define BLURB
 #XXX: nwall package blurb goes here.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
