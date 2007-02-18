GARNAME = xfce4-panel
CATEGORIES = xfce

DESCRIPTION = Xfce Panel
define BLURB
   Xfce Panel 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_panel, depend)

PATCHFILES += panel-item-manager.c.diff

include ../category.mk
