GARNAME = recordproto
GARVERSION = 1.13.2
CATEGORIES = x11

DESCRIPTION = Record extension headers
define BLURB
  Record extension headers
endef

MASTER_SITES  = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

