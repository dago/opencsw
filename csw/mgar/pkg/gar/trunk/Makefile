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

NOSOURCEPACKAGE = 1

REQUIRED_PKGS_CSWgar = $(PREREQUISITE_BASE_PKGS)

SPKG_DESC_CSWgar = The GAR package build system

SPKG_VERSION_CSWgar = $(call _REVISION)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = gar

EXTRA_MERGE_EXCLUDE_FILES = .*/\.svn/.*

ARCHALL = 1

# Because the bad pathes are in the bad pathes check we cannot check ourselves
ENABLE_CHECK = 0

include gar/category.mk

install-gar:
	@echo " ==> Installing $(GARNAME)"

	rm -f $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/garit $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(prefix)/src/gar
	cd $(WORKSRC) && pax -r -w -v -s ,.*/\.svn.*,, v1 v2 $(DESTDIR)$(prefix)/src/gar
