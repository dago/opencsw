GARNAME = libdvdread
GARVERSION = 0.9.7
CATEGORIES = lib

DESCRIPTION = provides a simple foundation for reading DVD-Video images
define BLURB
  libdvdread currently uses libdl to dynamically probe for libdvdcss at runtime.  If libdvdcss is found, then it will be used to decrypt the encrypted sections of a DVD.
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibdvdread, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
