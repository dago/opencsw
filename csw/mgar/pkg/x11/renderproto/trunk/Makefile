GARNAME = renderproto
GARVERSION = 0.11

CATEGORIES = x11

DESCRIPTION = Render extension headers from modular X.org
define BLURB
  This provides the Render extension headers from modular X.org X11 project.
endef

MASTER_SITES  = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

