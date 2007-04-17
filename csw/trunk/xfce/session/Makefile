GARNAME = xfce4-session
CATEGORIES = xfce

DESCRIPTION = Xfce Session Manager
define BLURB
   Xfce Session Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcesession.depend CSWxfcesession.gspec CSWxfcesession.prototype
DISTFILES += CSWlibxfcesession.depend CSWlibxfcesession.gspec CSWlibxfcesession.prototype
DISTFILES += CSWxfcesessiondoc.depend CSWxfcesessiondoc.gspec CSWxfcesessiondoc.prototype
DISTFILES += CSWlibxfcesessiondev.depend CSWlibxfcesessiondev.gspec CSWlibxfcesessiondev.prototype

# DISTFILES += $(call admfiles,CSWxfcesession, depend)

include ../category.mk

CONFIGURE_ARGS += --enable-dbus
