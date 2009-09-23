GARNAME = kbproto
GARVERSION = 1.0.3

CATEGORIES = x11

DESCRIPTION = KB extension headers from X.org
define BLURB
  This provides the KB extension headers from modular X.org X11 project.
endef

MASTER_SITES  = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxkbproto

REQUIRED_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

