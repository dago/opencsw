GARNAME = libxi
GARVERSION = 1.2.99.4
CATEGORIES = x11

DESCRIPTION = Client library for XInput
define BLURB
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXi-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
