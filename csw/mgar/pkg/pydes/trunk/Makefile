GARNAME = pyDes
GARVERSION = 2.0.0
CATEGORIES = lang

DESCRIPTION = implementation of the DES encryption algorithm
define BLURB
  implementation of the DES encryption algorithm
endef

MASTER_SITES = http://pydes.sourceforge.net/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWpydes
REQUIRED_PKGS = CSWpython
CATALOGNAME = pydes
SPKG_DESC = implementation of the DES encryption algorithm

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)
include gar/category.mk
