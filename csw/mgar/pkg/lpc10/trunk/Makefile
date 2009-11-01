GARNAME = lpc10
GARVERSION = 1.5
CATEGORIES = apps

DESCRIPTION = LPC-10 speech coder software
define BLURB
endef

MASTER_SITES = http://www.arl.wustl.edu/~jaf/lpc/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.arl.wustl.edu/~jaf/lpc/

BUILD64 = 1

# Some way to go for the manual build

CONFIGURE_SCRIPTS =

include gar/category.mk
