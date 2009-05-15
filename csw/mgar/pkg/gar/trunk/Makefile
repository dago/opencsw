GARNAME = gar
GARVERSION = 2.0
CATEGORIES = utils

DESCRIPTION = The GAR package build system
define BLURB
endef

# No master sites, we already have GAR in the repository
MASTER_SITES = 
DISTFILES = garit

WORKSRC = $(WORKDIR)

SPKG_SOURCEURL = http://gar.sourceforge.net

PACKAGES = CSWgar CSWgar-v1 CSWgar-v2

SPKG_DESC_CSWgar = The mGAR package build system
SPKG_DESC_CSWgar-v1 = The mGAR v1 system files
SPKG_DESC_CSWgar-v2 = The mGAR v2 system files

REQUIRED_PKGS_CSWgar = $(PREREQUISITE_BASE_PKGS) CSWsvn
REQUIRED_PKGS_CSWgar-v1 = CSWgar
REQUIRED_PKGS_CSWgar-v2 = CSWgar

SPKG_VERSION_CSWgar = $(shell svnversion)
SPKG_VERSION_CSWgar-v1 = $(shell svnversion $(CURDIR)/gar-base/v1)
SPKG_VERSION_CSWgar-v2 = $(shell svnversion $(CURDIR)/gar-base/v2)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = gar

PKGFILES_CSWgar-v1 = $(prefix)/src/gar/v1/.*
PKGFILES_CSWgar-v2 = $(prefix)/src/gar/v2/.*

# Because the bad pathes are in the bad pathes check we cannot check ourselves
ENABLE_CHECK = 0

include gar/category.mk

install-gar:
	@echo " ==> Installing $(GARNAME)"

	rm -f $(DESTIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/garit $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(prefix)/src/gar
	cd $(CURDIR)/gar-base && pax -r -w -v -s ,.*/\.svn.*,, . $(DESTDIR)$(prefix)/src/gar
