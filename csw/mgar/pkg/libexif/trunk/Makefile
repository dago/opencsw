GARNAME = libexif
GARVERSION = 0.6.17
CATEGORIES = lib

DESCRIPTION = EXIF Tag Parsing Library
define BLURB
  libexif is a library for parsing, editing, and saving EXIF data. It is
	intended to replace lots of redundant implementations in command-line
	utilities and programs with GUIs.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibexif,)

REQUIRED_PKGS += CSWggettext CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
