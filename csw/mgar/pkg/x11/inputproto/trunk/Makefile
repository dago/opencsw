GARNAME = inputproto
GARVERSION = 1.4.4
CATEGORIES = x11

DESCRIPTION = inputproto
define BLURB
inputproto
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES 	 = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST 	 = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWinputproto)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk


