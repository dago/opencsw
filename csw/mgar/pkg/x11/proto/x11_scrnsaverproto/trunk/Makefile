VERSION = 1.2.2
CATEGORIES = x11
PROTONAME = scrnsaverproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org ScrnSaver protocol headers
define BLURB
  ScrnSaver protocol headers from modular X.org
endef
	
MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11scrnsaverproto += catalogname-does-not-match-pkgname|pkgname=CSWx11scrnsaverproto|catalogname=x11_scrnsaverproto|expected-catalogname=x11scrnsaverproto
CHECKPKG_OVERRIDES_CSWx11scrnsaverproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

