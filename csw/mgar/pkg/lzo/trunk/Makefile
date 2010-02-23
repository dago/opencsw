GARNAME = lzo
GARVERSION = 2.03
CATEGORIES = utils

DESCRIPTION = LZO compression library
define BLURB
  LZO is a portable lossless data compression library written in ANSI C.
endef

MASTER_SITES = http://www.oberhumer.com/opensource/lzo/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.oberhumer.com/opensource/lzo/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
