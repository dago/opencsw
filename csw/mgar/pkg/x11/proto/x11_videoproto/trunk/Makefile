GARVERSION = 2.3.0
CATEGORIES = x11
PROTONAME = videoproto
GARNAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(GARVERSION)

DESCRIPTION = Video extension headers
define BLURB
  Video extension headers
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

