GARNAME = inputproto
GARVERSION = 1.5.0

CATEGORIES = x11

DESCRIPTION = Input extension headers from X.org project
define BLURB
  This provides the input extension headers from modular X.org X11 project
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1
CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk

