GARNAME = xfprint
CATEGORIES = xfce

DESCRIPTION = Xfce Printing Helper
define BLURB
   Xfce Printing Helper 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_print, depend)

include ../category.mk

CONFIGURE_ARGS += --enable-bsdlpr --enable-cups
