VERSION = 2.3
CATEGORIES = x11
PROTONAME = dmxproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = Distributed Multi-headed X protocol headers for X11
define BLURB
  Distributed Multi-headed X protocol headers from modular X.org : "your networked Xinerama".
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

