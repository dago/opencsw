# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = rc
VERSION = 1.7.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A reimplementation of the Plan 9 shell
define BLURB
endef

MASTER_SITES = http://www.libra-aries-books.co.uk/software/download/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.libra-aries-books.co.uk/software/rc

DEP_PKGS = CSWreadline

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-readline

include gar/category.mk
