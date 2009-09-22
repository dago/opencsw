GARNAME = xextproto
GARVERSION = 7.0.5

CATEGORIES = x11

DESCRIPTION = XExt extension headers from X.org
define BLURB
  This provides the XExt extension headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

