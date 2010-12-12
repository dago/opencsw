VERSION = 2.0
PROTONAME = inputproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

CATEGORIES = x11

DESCRIPTION = Input extension headers from X.org project
define BLURB
  This provides the input extension headers from modular X.org X11 project
endef
	
MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

RUNTIME_DEP_PKGS = CSWx11common
INCOMPATIBLE_PKGS = CSWinputproto

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

