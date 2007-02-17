GARNAME = xfce-mcs-manager
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager 
define BLURB
   Xfce Settings Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_mcs_manager, depend)

LIBDEPS = xfce/libxfce4util

PATCHFILES += configure.in.diff
PATCHFILES += configure.diff

include ../category.mk
