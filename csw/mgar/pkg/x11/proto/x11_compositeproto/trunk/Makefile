VERSION = 0.4.2
CATEGORIES = x11
PROTONAME = compositeproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org Composite protocol headers
define BLURB
  Composite protocol headers from modular X.org X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11compositeproto += catalogname-does-not-match-pkgname|pkgname=CSWx11compositeproto|catalogname=x11_compositeproto|expected-catalogname=x11compositeproto
CHECKPKG_OVERRIDES_CSWx11compositeproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

