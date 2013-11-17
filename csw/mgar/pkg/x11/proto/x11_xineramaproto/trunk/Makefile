VERSION = 1.2.1
CATEGORIES = x11
PROTONAME = xineramaproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION =  X.Org Xinerama protocol headers
define BLURB
  Prototype headers for Xinerama extension to X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11xineramaproto += catalogname-does-not-match-pkgname|pkgname=CSWx11xineramaproto|catalogname=x11_xineramaproto|expected-catalogname=x11xineramaproto
CHECKPKG_OVERRIDES_CSWx11xineramaproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

