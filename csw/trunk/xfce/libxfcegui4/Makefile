GARNAME = libxfcegui4
CATEGORIES = xfce

DESCRIPTION = Xfce Widget Library 
define BLURB
   Xfce Widget Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibxfcegui4, depend)

LIBDEPS = xfce/libxfce4util

# Patch for the exo-mount.c file
PATCHFILES += configure.in.diff
PATCHFILES += configure.diff

include ../category.mk

# Configure common options
CONFIGURE_ARGS += --enable-xinerama

