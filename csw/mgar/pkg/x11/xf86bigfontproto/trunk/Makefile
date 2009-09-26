GARNAME = xf86bigfontproto
GARVERSION = 1.2.0
CATEGORIES = x11

DESCRIPTION = X.Org XF86BigFont protocol headers
define BLURB
  XF86BigFont protocol headersX protocol and ancillary headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

