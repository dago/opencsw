GARNAME = pil
GARVERSION = 1.1.7
CATEGORIES = python
DISTNAME = Imaging-$(GARVERSION)


DESCRIPTION = Python Imaging Library
define BLURB
  Long description
endef

MASTER_SITES = http://effbot.org/downloads/
DISTFILES  = $(DISTNAME).tar.gz


RUNTIME_DEP_PKGS_CSWpil = CSWlcmsrt CSWftype2 CSWjpeg CSWtcl CSWzlib CSWtk


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = Imaging-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWpil += license-missing

include gar/category.mk

