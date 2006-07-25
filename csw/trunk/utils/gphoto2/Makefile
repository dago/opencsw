GARNAME = gphoto2
GARVERSION = 2.2.0
CATEGORIES = utils

DESCRIPTION = gphoto2 is a command-line frontend to libgphoto2
define BLURB
  gPhoto2 is a free, redistributable, ready to use digital camera
  command-line application for Unix-like systems. It uses libgphoto2 and
  supports more than 700 cameras.
endef

MASTER_SITES = 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgphoto2,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
