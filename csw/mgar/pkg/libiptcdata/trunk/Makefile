GARNAME = libiptcdata
GARVERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = IPTC Tag Parsing Library
define BLURB
   libiptcdata is a library for manipulating the International Press
   Telecommunications Council (IPTC) metadata stored within multimedia
   files such as images.  The library provides routines for parsing,
   viewing, modifying, and saving this metadata.
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibiptcdata,)

REQUIRED_PKGS = CSWggettext CSWggettextrt CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Patch submitted to upstream, pending new release
PATCHFILES = iptc-dataset.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
