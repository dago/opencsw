GARNAME = fontsproto
GARVERSION = 2.1.0
CATEGORIES = x11

DESCRIPTION = Fonts extension headers
define BLURB
  Font-related prototype header files for X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

