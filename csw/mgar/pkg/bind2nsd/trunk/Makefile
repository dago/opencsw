GARNAME = bind2nsd
GARVERSION = 0.7.2
CATEGORIES = utils

DESCRIPTION = scripts to translate DNS information in BIND format to NSD format
define BLURB
  This project builds scripts that translate DNS information in BIND format to NSD
  format, and then copy that translation to an NSD server. The goal is to make it
  simple to run redundant BIND and NSD servers and keep them in sync, using only
  the BIND configuration files. 
endef

MASTER_SITES = http://bind2nsd.sourceforge.net/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = setup.py.diff
PATCHFILES += Config.py.diff
PATCHFILES += Utils.py.diff
PATCHFILES += nsd-sync.diff
PATCHFILES += s64-sync.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWbind2nsd
REQUIRED_PKGS = CSWpython CSWpydes
CATALOGNAME = bind2nsd
SPKG_DESC = scripts to translate DNS information in BIND format to NSD format

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

post-configure-modulated:
	@echo " ==> Fixing Shebang"
	@cd $(WORKSRC)
	@perl -pi -e 's/\/usr\/bin\/env\ python/\/opt\/csw\/bin\/python/g' `find . -name '*.py'`
	@$(MAKECOOKIE)

include gar/category.mk
