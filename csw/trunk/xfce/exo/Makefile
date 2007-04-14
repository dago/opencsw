GARNAME = exo
CATEGORIES = xfce

DESCRIPTION = Xfce Extensions Library 
define BLURB
   Xfce Extensions Library 
endef

GARVERSION = 0.3.2
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfceexo.depend CSWxfceexo.gspec CSWxfceexo.prototype
DISTFILES += CSWxfceexodoc.depend CSWxfceexodoc.gspec CSWxfceexodoc.prototype
DISTFILES += CSWxfceexodevel.depend CSWxfceexodevel.gspec CSWxfceexodevel.prototype
# DISTFILES += $(call admfiles,CSWxfce_exo, depend)

#  Patch for the exo-mount.c file
PATCHFILES = exo.diff

include ../category.mk

CONFIGURE_ARGS += --enable-python
