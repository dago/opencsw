GARNAME = gd
GARVERSION = 2.0.22
CATEGORIES = lib

DESCRIPTION = A library used to create PNG images
define BLURB
  gd is a library used to create PNG, JPEG, or WBMP images. It has many nice
  features and can be used in scripts (e.g. PHP) for dynamic image generation.
endef

MASTER_SITES = http://www.boutell.com/gd/http/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWgd,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
