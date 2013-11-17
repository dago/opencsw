VERSION = 0.11.1
CATEGORIES = x11
PROTONAME = renderproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = Render extension headers from modular X.org
define BLURB
  This provides the Render extension headers from modular X.org X11 project.
endef
	
MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11renderproto += catalogname-does-not-match-pkgname|pkgname=CSWx11renderproto|catalogname=x11_renderproto|expected-catalogname=x11renderproto
CHECKPKG_OVERRIDES_CSWx11renderproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common
INCOMPATIBLE_PKGS = CSWrenderproto

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

