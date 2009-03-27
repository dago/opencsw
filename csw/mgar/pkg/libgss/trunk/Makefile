GARNAME = gss
GARVERSION = 20090327
CATEGORIES = lib

DESCRIPTION = GNU Generic Security Service
define BLURB
endef

# Strangely enough, gss is not on $(GNU_MIRROR)
#MASTER_SITES = ftp://alpha.gnu.org/gnu/gss/
MASTER_SITES = http://daily.josefsson.org/gss/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTNAME = $(GARNAME)-0.1.0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibgss

PREREQUISITE_PKGS = 
REQUIRED_PKGS = CSWggettextrt

SPKG_SOURCEURL = http://www.gnu.org/software/$(GNU_PROJ)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

