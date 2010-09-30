GARNAME = gource
GARVERSION = 0.28
CATEGORIES = apps

DESCRIPTION = Software version control visualization
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-Make-sure-we-have-a-prototype-for-sqrt.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_CXXFLAGS = -library=stlport4
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
