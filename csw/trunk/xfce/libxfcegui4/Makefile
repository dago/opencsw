GARNAME = libxfcegui4
CATEGORIES = xfce

DESCRIPTION = Xfce Widget Library 
define BLURB
   Xfce Widget Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWlibxfcegui4.depend CSWlibxfcegui4.gspec CSWlibxfcegui4.prototype
DISTFILES += CSWlibxfcegui4doc.depend CSWlibxfcegui4doc.gspec CSWlibxfcegui4doc.prototype
DISTFILES += CSWlibxfcegui4devel.depend CSWlibxfcegui4devel.gspec CSWlibxfcegui4devel.prototype

LIBDEPS = xfce/libxfce4util

include ../category.mk

# Configure common options
CONFIGURE_ARGS += --enable-xinerama

