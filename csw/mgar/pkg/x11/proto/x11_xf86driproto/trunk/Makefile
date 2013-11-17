VERSION = 2.1.1
CATEGORIES = x11
PROTONAME = xf86driproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org XF86DRI protocol headers
define BLURB
  X.Org XF86DRI protocol headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11xf86driproto += catalogname-does-not-match-pkgname|pkgname=CSWx11xf86driproto|catalogname=x11_xf86driproto|expected-catalogname=x11xf86driproto
CHECKPKG_OVERRIDES_CSWx11xf86driproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

