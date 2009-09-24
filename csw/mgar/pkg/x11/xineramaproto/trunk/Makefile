GARNAME = xineramaproto
GARVERSION = 1.1.2
CATEGORIES = x11

DESCRIPTION =  X.Org Xinerama protocol headers
define BLURB
  Prototype headers for Xinerama extension to X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

