GARNAME = slang
GARVERSION = 2.2.2
CATEGORIES = lib

DESCRIPTION = Library primarily to provide an alternative to libcurses
define BLURB
endef

MASTER_SITES = ftp://space.mit.edu/pub/davis/slang/v2.2/
MASTER_SITES += ftp://ftp.fu-berlin.de/pub/unix/misc/slang/v2.2/
MASTER_SITES += ftp://ftp.ntua.gr/pub/lang/slang/slang/v2.2/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.s-lang.org/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
