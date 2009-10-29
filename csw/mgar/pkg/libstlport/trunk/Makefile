GARNAME = libstlport
GARVERSION = 5.2.1
CATEGORIES = lib

DESCRIPTION = A multiplatform C++ standard library implementation
define BLURB
  STLport is a multiplatform C++ Standard Library implementation.
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = stlport
DISTNAME = STLport-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
