GARNAME = speex
GARVERSION = 1.2rc1
CATEGORIES = lib

DESCRIPTION = Speex audio codec support library
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/speex/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWspeex
CATALOGNAME = libspeex

SPKG_SOURCEURL = http://www.speex.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
