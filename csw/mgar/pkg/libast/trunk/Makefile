NAME = libast
VERSION = 0.7
CATEGORIES = lib

DESCRIPTION = The Library of Assorted Spiffy Things (LibAST - formerly libmej)
define BLURB
endef

MASTER_SITES = http://www.eterm.org/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Fix-unknown-Sun-Studio-directive.patch
PATCHFILES += 0001-Fix-unknown-Sun-Studio-directive-more.patch
PATCHFILES += 0002-Fix-check-for-C99.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

STRIP_LIBTOOL = 1

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
