NAME = libgnugetopt
VERSION = 1.3
CATEGORIES = lib

DESCRIPTION = Library containing getopt_long
define BLURB
endef

MASTER_SITES = http://distfiles.macports.org/libgnugetopt/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
