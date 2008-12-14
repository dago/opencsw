GARNAME = renderproto
GARVERSION = 0.9.3
CATEGORIES = x11

DESCRIPTION = renderproto
define BLURB
renderproto
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES 	 = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST 	 = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += $(call admfiles,CSWrenderproto)

include gar/category.mk


