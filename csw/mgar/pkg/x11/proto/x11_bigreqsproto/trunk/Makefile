PROTONAME = bigreqsproto
CATEGORIES = x11
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)
VERSION = 1.1.2

DESCRIPTION = Prototype headers for BigReqs extension to X11
define BLURB
  Prototype headers for BigReqs extension to X11 for modular X.org project
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11bigreqsproto
CATALOGNAME_CSWx11bigreqsproto = x11_bigreqsproto

CHECKPKG_OVERRIDES_CSWx11bigreqsproto += catalogname-does-not-match-pkgname|pkgname=CSWx11bigreqsproto|catalogname=x11_bigreqsproto|expected-catalogname=x11bigreqsproto
CHECKPKG_OVERRIDES_CSWx11bigreqsproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

