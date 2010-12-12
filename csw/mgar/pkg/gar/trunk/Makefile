NAME = gar
VERSION = 2.0
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

RUNTIME_DEP_PKGS_CSWgar = $(PREREQUISITE_BASE_PKGS)

SPKG_DESC_CSWgar = The GAR package build system

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = gar

EXTRA_MERGE_EXCLUDE_FILES = .*/\.svn/.*

ARCHALL = 1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(call _REVISION)

install-gar:
	@echo " ==> Installing $(NAME)"

	rm -f $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/garit $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(prefix)/src/gar
	cd $(WORKSRC) && pax -r -w -v -s ,.*/\.svn.*,, v1 v2 $(DESTDIR)$(prefix)/src/gar

# This is a workaround for builds that are done with umask 0027.  There's a
# problem in which pax does not preserve the access bits.
post-install-modulated:
	gfind $(DESTDIR) -type f -perm /u+x -exec chmod a+x,a+r,u+w {} \;
	gfind $(DESTDIR) -type d -perm /u+x -exec chmod a+x,a+r,u+w {} \;
	gfind $(DESTDIR) -type f -perm /u+r -exec chmod a+r,u+w     {} \;
	@$(MAKECOOKIE)
