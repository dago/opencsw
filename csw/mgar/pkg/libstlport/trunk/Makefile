NAME = libstlport
VERSION = 5.2.1
CATEGORIES = lib

DESCRIPTION = A multiplatform C++ standard library implementation
define BLURB
  STLport is a multiplatform C++ Standard Library implementation.
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = stlport
DISTNAME = STLport-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
