GARNAME = xfwm4
CATEGORIES = xfce

DESCRIPTION = Xfce Window Manager 
define BLURB
   Xfce Window Manager
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_xfwm4, depend)

include ../category.mk

CONFIGURE_ARGS +=  --enable-xsync --enable-render --enable-randr --enable-xinerama
