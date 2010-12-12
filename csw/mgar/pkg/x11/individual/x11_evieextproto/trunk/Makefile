VERSION = 1.1.0
CATEGORIES = x11
PROTONAME = evieext
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org EvIE protocol headers
define BLURB
  EvIE protocol headers from modular X.org X11
endef

MASTER_SITES = $(X11_INDIVIDUAL_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)proto
CATALOGNAME_CSWx11$(PROTONAME)proto = x11_$(PROTONAME)proto

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

