GARNAME = gd
GARVERSION = 2.0.35
CATEGORIES = lib

DESCRIPTION = A library used to create PNG images
define BLURB
  gd is a library used to create PNG, JPEG, or WBMP images. It has many nice
  features and can be used in scripts (e.g. PHP) for dynamic image generation.
endef

MASTER_SITES = http://www.libgd.org/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgd,depend prototype)
DISTFILES += $(call admfiles,CSWgd-devel,depend prototype)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
