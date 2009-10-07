GARNAME = fribidi
GARVERSION = 0.19.2
CATEGORIES = lib

DESCRIPTION = An implementation of the Unicode Bidirectional Algorithm (bidi)
define BLURB
endef

MASTER_SITES = http://fribidi.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.fribidi.org/

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
