GARNAME = xproto
GARVERSION = 7.0.15
CATEGORIES = x11

DESCRIPTION = X protocol and ancillary headers from X.org X11
define BLURB
  X protocol and ancillary headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

