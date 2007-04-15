GARNAME = Thunar
GARVERSION = 0.8.0
CATEGORIES = xfce

DESCRIPTION = Xfce Thunar File Manager
define BLURB
   Xfce Thunar File Manager 
endef

DISTFILES   = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES  += $(call admfiles,CSWxfcethunar, depend)

PATCHFILES  = thunar-vfs-path-private.h.diff 
PATCHFILES += thunar-vfs-thumb-jpeg.c.diff

include ../category.mk

CONFIGURE_ARGS += --with-x --enable-dbus
