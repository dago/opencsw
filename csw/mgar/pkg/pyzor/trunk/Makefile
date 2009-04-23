GARNAME = pyzor
GARVERSION = 0.4.0
CATEGORIES = utils

DESCRIPTION = A collaborative, networked system to detect and block spam
define BLURB
  Pyzor is a collaborative, networked system to detect and block spam using
  identifying digests of messages.
endef

MASTER_SITES = http://www.pyzor.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PATCHFILES = client.py.diff
PATCHFILES += pyzor.diff
PATCHFILES += pyzord.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWpyzor
REQUIRED_PKGS = CSWpython
CATALOGNAME = pyzor
SPKG_DESC = A collaborative, networked system to detect and block spam

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk
