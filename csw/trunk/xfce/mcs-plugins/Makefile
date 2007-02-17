GARNAME = xfce-mcs-plugins
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager Plugins
define BLURB
   Xfce Settings Manager Plugins
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_mcs_plugins, depend)

# Patch for the exo-mount.c file
PATCHFILES += configure.in.diff
PATCHFILES += configure.diff

include ../category.mk

