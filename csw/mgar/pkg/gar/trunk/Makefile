# $Id$

NAME = gar
VERSION = 2.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = The GAR package build system
define BLURB
endef

# No master sites, we already have GAR in the repository
MASTER_SITES = svn-http://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/
SVNHTTP_CO_ARGS = --no-auth-cache
DISTFILES += v1 v2
DISTFILES += COPYING
NOCHECKSUM = v1 v2

DISTFILES += garit

WORKSRC = $(WORKDIR)

SPKG_SOURCEURL = http://gar.opencsw.org

NOSOURCEPACKAGE = 1

RUNTIME_DEP_PKGS_CSWgar += $(PREREQUISITE_BASE_PKGS)
RUNTIME_DEP_PKGS_CSWgar += CSWruby
RUNTIME_DEP_PKGS_CSWgar += CSWnamazu

SPKG_DESC_CSWgar = The GAR package build system

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = gar

EXTRA_MERGE_EXCLUDE_FILES = .*/\.svn/.*

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWgar += surplus-dependency
# We know about them, they are okay.
CHECKPKG_OVERRIDES_CSWgar += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgar += archall-with-arch-paths|/opt/csw/src/gar/v2/etc/commondirs-i386

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/src/gar/v2/.gitignore

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(call _REVISION)

post-fetch:
	svn export https://opencsw.svn.sourceforge.net/svnroot/opencsw/gar-wrapper/mgar $(DOWNLOADDIR)/mgar
	@$(MAKECOOKIE)

install-gar:
	@echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)$(bindir)
	# garit seems to be not developed yet.  Not including for now.
	# rm -f $(DESTDIR)$(bindir)/garit
	# ginstall $(WORKSRC)/garit $(DESTDIR)$(bindir)/garit
	ginstall -d $(DESTDIR)$(prefix)/src/gar
	ginstall $(DOWNLOADDIR)/mgar $(DESTDIR)$(bindir)/mgar
	cd $(WORKSRC) && pax -r -w -v -s ,.*/\.svn.*,, v1 v2 $(DESTDIR)$(prefix)/src/gar
	@$(MAKECOOKIE)

# This is a workaround for builds that are done with umask 0027.  There's a
# problem in which pax does not preserve the access bits.
post-install-modulated:
	gfind $(DESTDIR) -type f -perm /u+x -exec chmod a+x,a+r,u+w {} \;
	gfind $(DESTDIR) -type d -perm /u+x -exec chmod a+x,a+r,u+w {} \;
	gfind $(DESTDIR) -type f -perm /u+r -exec chmod a+r,u+w     {} \;
	@$(MAKECOOKIE)
