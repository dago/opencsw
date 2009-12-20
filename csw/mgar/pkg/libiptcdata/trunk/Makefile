GARNAME = libiptcdata
GARVERSION = 1.0.4
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

SPKG_SOURCEURL = http://libiptcdata.sourceforge.net

LICENSE = COPYING

REQUIRED_PKGS = CSWggettextrt CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=130582
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Patch submitted to upstream, pending new release
#PATCHFILES = iptc-dataset.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
