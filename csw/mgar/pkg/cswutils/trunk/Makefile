GARNAME = cswutils
GARVERSION = 1.14.4
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 74

MASTER_SITES =
DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += compare_pkgs.py-r$(SVN_REV)
DISTFILES += opencsw_lib.py-r$(SVN_REV)

REQUIRED_PKGS = CSWtextutils CSWfakeroot CSWperl
REQUIRED_PKGS += CSWpmyaml CSWpmlibwww CSWpmhtmltree

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org/

ARCHALL = 1

# The package contains 'checkpkg', which checks for bad pathes. Of
# course the bad pathes are inside the package, because it is checked
# for them. So disable the test.
ENABLE_CHECK = 0

include gar/category.mk

download/compare_pkgs.py-r$(SVN_REV):
	svn export -r $(SVN_REV) $(SVNROOT)compare_pkgs.py
	mv compare_pkgs.py download/compare_pkgs.py-r$(SVN_REV)
	@$(MAKECOOKIE)

download/opencsw_lib.py-r$(SVN_REV):
	svn export -r $(SVN_REV) $(SVNROOT)opencsw_lib.py
	mv opencsw_lib.py download/opencsw_lib.py-r$(SVN_REV)
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/checkpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/cpan2pkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/createpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/stagepkg $(DESTDIR)$(bindir)
	@ginstall $(GARDIR)/bin/fixlibtool $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@ginstall $(WORKSRC)/checkpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/createpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/stagepkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall -d $(DESTDIR)$(libdir)/opencsw
	@ginstall $(WORKSRC)/compare_pkgs.py-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/opencsw/compare_pkgs.py
	@ginstall $(WORKSRC)/opencsw_lib.py-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/opencsw/opencsw_lib.py
	@ln -s ../lib/opencsw/compare_pkgs.py $(DESTDIR)$(bindir)/csw-pkg-diff
	@$(MAKECOOKIE)
