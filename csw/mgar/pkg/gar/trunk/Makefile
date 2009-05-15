GARNAME = gar
GARVERSION = 2.0
CATEGORIES = utils

DESCRIPTION = The GAR package build system
define BLURB
endef

# No master sites, we already have GAR in the repository
MASTER_SITES = svn-http://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/
SVNHTTP_CO_ARGS = --no-auth-cache
DISTFILES = v1 v2
NOCHECKSUM = v1 v2

DISTFILES += garit

WORKSRC = $(WORKDIR)

SPKG_SOURCEURL = http://gar.opencsw.org

PACKAGES = CSWgar CSWgar-v1 CSWgar-v2

CATALOGNAME_CSWgar = gar
CATALOGNAME_CSWgar-v1 = gar_v1
CATALOGNAME_CSWgar-v2 = gar_v2

REQUIRED_PKGS_CSWgar = $(PREREQUISITE_BASE_PKGS) CSWsvn
REQUIRED_PKGS_CSWgar-v1 = CSWgar
REQUIRED_PKGS_CSWgar-v2 = CSWgar

SPKG_DESC_CSWgar = The mGAR package build system
SPKG_DESC_CSWgar-v1 = The mGAR v1 system files
SPKG_DESC_CSWgar-v2 = The mGAR v2 system files

SPKG_VERSION_CSWgar = $(call _REVISION)
SPKG_VERSION_CSWgar-v1 = $(shell svnversion $(DOWNLOADDIR)/v1)
SPKG_VERSION_CSWgar-v2 = $(shell svnversion $(DOWNLOADDIR)/v2)

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
	cd $(WORKSRC) && pax -r -w -v -s ,.*/\.svn.*,, v1 v2 $(DESTDIR)$(prefix)/src/gar
