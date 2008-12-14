GARNAME = xcb-proto
GARVERSION = 1.1
CATEGORIES = x11

DESCRIPTION = xcb-proto
define BLURB
xcb-proto
endef

MASTER_SITES =http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += $(call admfiles,CSWxcb-proto)

include gar/category.mk


