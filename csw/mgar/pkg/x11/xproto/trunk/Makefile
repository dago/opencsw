GARNAME = xproto
GARVERSION = 7.0.14
CATEGORIES = x11

DESCRIPTION = xproto
define BLURB
xproto
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES 	 = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST 	 = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += $(call admfiles,CSWxproto)

include gar/category.mk

