GARNAME = xf86vidmodeproto
GARVERSION = 2.2.2
CATEGORIES = x11

DESCRIPTION = X.Org XF86VidMode protocol headers
define BLURB
  X.Org XF86VidMode protocol headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

