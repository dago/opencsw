VERSION = 1.2.2
CATEGORIES = x11
PROTONAME = xcmiscproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org XCMisc extension headers
define BLURB
  XCMisc extension headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11xcmiscproto += catalogname-does-not-match-pkgname|pkgname=CSWx11xcmiscproto|catalogname=x11_xcmiscproto|expected-catalogname=x11xcmiscproto
CHECKPKG_OVERRIDES_CSWx11xcmiscproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

