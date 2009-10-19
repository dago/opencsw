# $Id$

GARNAME = cswutils
GARVERSION = 1.14.5
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 93

MASTER_SITES =
SVN_FILES = submit_to_newpkgs.py compare_pkgs.py opencsw_lib.py
DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += $(foreach F,$(SVN_FILES),$(F)-r$(SVN_REV))

REQUIRED_PKGS = CSWtextutils CSWfakeroot CSWperl
REQUIRED_PKGS += CSWpmyaml CSWpmlibwww CSWpmhtmltree
REQUIRED_PKGS += CSWpython

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

# This target doesn't work when defined as $(DOWNLOADDIR)/%-r$(SVN_REV)
$(foreach F,$(SVN_FILES),$(DOWNLOADDIR)/$(F)-r$(SVN_REV)):
	svn export -r $(SVN_REV) $(SVNROOT)$(subst -r$(SVN_REV),,$(notdir $@))
	mv $(subst -r$(SVN_REV),,$(notdir $@)) $@
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
	@ginstall -d $(DESTDIR)$(libdir)/python/csw
	@ginstall -m 644 $(WORKSRC)/opencsw_lib.py-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/python/csw/opencsw_lib.py
	@for f in compare_pkgs.py submit_to_newpkgs.py; do \
		ginstall -m 755 $(WORKSRC)/$${f}-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/python/csw/$${f}; \
	done
	@ln -s ../lib/python/csw/compare_pkgs.py $(DESTDIR)$(bindir)/comparepkg
	@ln -s ../lib/python/csw/submit_to_newpkgs.py $(DESTDIR)$(bindir)/submitpkg
	@$(MAKECOOKIE)
