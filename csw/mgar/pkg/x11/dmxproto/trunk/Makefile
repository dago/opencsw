GARNAME = dmxproto
GARVERSION = 2.2.2
CATEGORIES = x11

DESCRIPTION = Distributed Multi-headed X protocol headers for X11
define BLURB
  Distributed Multi-headed X protocol headers from modular X.org : "your networked Xinerama".
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

