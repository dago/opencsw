VERSION = 7.0.16
CATEGORIES = x11
PROTONAME = xproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)
GARTYPE = bts

DESCRIPTION = X protocol and ancillary headers from X.org X11
define BLURB
  X protocol and ancillary headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = NIMOSSx11$(PROTONAME)
CATALOGNAME_NIMOSSx11$(PROTONAME) = x11_$(PROTONAME)

RUNTIME_DEP_PKGS = NIMOSSx11common
INCOMPATIBLE_PKGS = NIMOSSxproto

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

