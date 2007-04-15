GARNAME = xfprint
CATEGORIES = xfce

DESCRIPTION = Xfce Printing Helper
define BLURB
   Xfce Printing Helper 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfceprint.depend CSWxfceprint.gspec CSWxfceprint.prototype
DISTFILES += CSWxfceprintdoc.depend CSWxfceprintdoc.gspec CSWxfceprintdoc.prototype
DISTFILES += CSWlibxfceprint.depend CSWlibxfceprint.gspec CSWlibxfceprint.prototype
DISTFILES += CSWlibxfceprintdevel.depend CSWlibxfceprintdevel.gspec CSWlibxfceprintdevel.prototype

# DISTFILES += $(call admfiles,CSWxfceprint, depend)

include ../category.mk

CONFIGURE_ARGS += --enable-bsdlpr --enable-cups
