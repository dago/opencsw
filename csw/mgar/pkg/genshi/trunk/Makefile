GARNAME = genshi
GARVERSION = 0.5.1
CATEGORIES = utils
DISTNAME = Genshi
DESCRIPTION = 
define BLURB
endef

MASTER_SITES = http://ftp.edgewall.com/pub/genshi/
DISTFILES  = $(DISTNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWgenshi

REQUIRED_PKGS_CSWgenshi = 
CATALOGNAME_CSWgenshi = $(GARNAME)
SPKG_DESC_CSWgenshi   = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(DISTNAME)-(\d+(?:\.\d+)*)


CONFIGURE_ARGS = $(DIRPATHS)

#ENABLE_CHECK = 0

# No test target
TEST_SCRIPTS =

include gar/category.mk

