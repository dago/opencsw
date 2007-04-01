GARNAME = xfce-utils
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities
define BLURB
   Xfce Utilities 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_utils, depend)

PATCHFILES  = startxfce4.in.patch

include ../category.mk

CONFIGURE_ARGS += --enable-dbus
