GARNAME = exo
CATEGORIES = xfce

DESCRIPTION = Xfce Extensions Library 
define BLURB
   Xfce Extensions Library 
endef

GARVERSION = 0.3.2
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_exo, depend)

#  Patch for the exo-mount.c file
PATCHFILES = exo.diff

include ../category.mk

CONFIGURE_ARGS += --enable-python
