PROTONAME = applewmproto
GARVERSION = 1.0.3
CATEGORIES = x11
GARNAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(GARVERSION)

DESCRIPTION = AppleWM extension headers from X.org
define BLURB
  AppleWM extension headers from modular X.org X11 project
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11applewmproto
CATALOGNAME_CSWx11applewmproto = x11_applewmproto

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

