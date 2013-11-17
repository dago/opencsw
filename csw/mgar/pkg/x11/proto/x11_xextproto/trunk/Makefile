VERSION = 7.2.1
PROTONAME = xextproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

CATEGORIES = x11

DESCRIPTION = XExt extension headers from X.org
define BLURB
  This provides the XExt extension headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11xextproto += catalogname-does-not-match-pkgname|pkgname=CSWx11xextproto|catalogname=x11_xextproto|expected-catalogname=x11xextproto
CHECKPKG_OVERRIDES_CSWx11xextproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common
INCOMPATIBLE_PKGS = CSWxextproto

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

