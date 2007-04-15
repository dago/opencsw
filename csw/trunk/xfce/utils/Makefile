GARNAME = xfce-utils
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities
define BLURB
   Xfce Utilities 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfceutils.depend CSWxfceutils.gspec CSWxfceutils.prototype
DISTFILES += CSWxfceutilsdoc.depend CSWxfceutilsdoc.gspec CSWxfceutilsdoc.prototype

include ../category.mk

CONFIGURE_ARGS += --enable-dbus
