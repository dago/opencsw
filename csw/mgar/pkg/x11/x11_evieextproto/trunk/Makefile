GARVERSION = 1.1.0
CATEGORIES = x11
PROTONAME = evieext
GARNAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(GARVERSION)

DESCRIPTION = X.Org EvIE protocol headers
define BLURB
  EvIE protocol headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)proto
CATALOGNAME_CSWx11$(PROTONAME)proto = x11_$(PROTONAME)proto

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

