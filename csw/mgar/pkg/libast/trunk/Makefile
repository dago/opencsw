GARNAME = libast
GARVERSION = 0.7
CATEGORIES = lib

DESCRIPTION = The Library of Assorted Spiffy Things (LibAST - formerly libmej)
define BLURB
endef

MASTER_SITES = http://www.eterm.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Fix-unknown-Sun-Studio-directive.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

STRIP_LIBTOOL = 1

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
