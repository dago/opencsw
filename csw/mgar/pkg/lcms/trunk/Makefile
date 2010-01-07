GARNAME = lcms
GARVERSION = 1.19
GARSUBREV = 
CATEGORIES = lib

DESCRIPTION = The little color management system and tools
define BLURB
	LittleCMS is a CMM, a color management engine; it implements fast transforms
	between ICC profiles. "Little" stands for its small overhead. With a typical
	footprint of about 100K including C runtime, you can color-enable your
	application without the pain of ActiveX, OCX, redistributables or binaries
	of any kind. We are using little cms in several commercial projects, however,
	we are offering lcms library free for anybody under an extremely liberal
	open source license.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION)$(GARSUBREV).tar.gz
#DISTFILES  = $(GARNAME)-$(GARVERSION)$(GARSUBREV).tar.gz

PACKAGES = CSWlcms CSWlcmsdevel
CATALOGNAME_CSWlcms = lcms
CATALOGNAME_CSWlcmsdevel = lcms_devel

SPKG_DESC_CSWlcms += The little color management system and tools
SPKG_DESC_CSWlcmsdevel += The little color management system and tools - developer package

REQUIRED_PKGS_CSWlcms += CSWjpeg CSWtiff CSWzlib
REQUIRED_PKGS_CSWlcmsdevel += CSWlcms

PKGFILES_CSWlcmsdevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://www.littlecms.com

LICENSE = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=26279
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

TEST_TARGET = check

include gar/category.mk

#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)
