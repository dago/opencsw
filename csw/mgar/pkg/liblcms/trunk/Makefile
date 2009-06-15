GARNAME = lcms
GARVERSION = 1.18a
CATEGORIES = lib
LCMS_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z]//g')
LCMS_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/[^a-z]//g')

DISTNAME = $(GARNAME)-$(LCMS_VERSION)
DESCRIPTION = A free color management engine in 100K.
define BLURB
	Little cms intends to be a small-footprint, speed optimized 
	color management engine in open source form. Since the initial release, 
	back in 1998, lcms has been continuously evolving, mostly thanks to 
	contributions done by skilled programmers, who generously donated 
	their valuable time to review the engine and the documentation. 
	For now, little cms has been ported to a big number of platforms and 
	is currently used in many open source and commercial products, 
	as well as being distributed in major linux environments. 
endef

MASTER_SITES = http://www.littlecms.com/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlcms 
CATALOGNAME_CSWlcms = liblcms
SPKG_DESC_CSWlcms = $(DESCRIPTION)

REQUIRED_PKGS_CSWlcms   = CSWjpeg CSWtiff CSWzlib

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ENABLE_CHECK = 0
BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
TEST_TARGET = check

include gar/category.mk
SPKG_VERSION  := $(LCMS_VERSION)
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(LCMS_RELEASE)

