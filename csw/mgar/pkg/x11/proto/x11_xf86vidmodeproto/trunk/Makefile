VERSION = 2.3
CATEGORIES = x11
PROTONAME = xf86vidmodeproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org XF86VidMode protocol headers
define BLURB
  X.Org XF86VidMode protocol headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11xf86vidmdproto
CATALOGNAME_CSWx11xf86vidmdproto = x11_$(PROTONAME)

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

