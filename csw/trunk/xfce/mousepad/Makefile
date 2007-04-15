GARNAME = mousepad
GARVERSION = 0.2.12
CATEGORIES = xfce

DESCRIPTION = Xfce Mousepad Text Editor
define BLURB
   Xfce Mousepad Text Editor 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfcemousepad, depend)

PATCHFILES += configure.in.diff
PATCHFILES += configure.diff

include ../category.mk

