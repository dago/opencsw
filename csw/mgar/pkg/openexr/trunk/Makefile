GARNAME = openexr
GARVERSION = 1.6.1
CATEGORIES = lib

DESCRIPTION = high dynamic-range (HDR) image file format developed by Industrial Light & Magic
define BLURB
  high dynamic-range (HDR) image file format developed by Industrial Light & Magic
endef

MASTER_SITES = http://savannah.nongnu.org/download/openexr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWopenexr,)

REQUIRED_PKGS += CSWilmbase CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

LDFLAGS += -lCstd -lCrun -lc -lm
export LDFLAGS

TEST_SCRIPTS =

include gar/category.mk
