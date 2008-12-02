GARNAME = OpenEXR
GARVERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = high dynamic-range (HDR) image file format developed by Industrial Light & Magic
define BLURB
  high dynamic-range (HDR) image file format developed by Industrial Light & Magic
endef

MASTER_SITES = http://savannah.nongnu.org/download/openexr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWopenexr,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
